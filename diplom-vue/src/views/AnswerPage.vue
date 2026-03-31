<template>
  <!-- Заголовок -->
  <div class="table-header d-flex justify-space-between align-center mb-4">
    <h2 class="text-h5 font-weight-bold text-primary">Результаты тестирования</h2>
    <v-btn 
      variant="outlined" 
      color="primary" 
      size="small"
      :loading="loading"
      @click="loadItems"
    >
      🔄 Обновить
    </v-btn>
  </div>

  <!-- Поиск -->
  <v-text-field
    v-model="search"
    prepend-inner-icon="mdi-magnify"
    label="Поиск по тесту или ФИО"
    variant="outlined"
    density="compact"
    class="mb-4"
    clearable
  />

  <!-- Загрузка -->
  <v-progress-linear v-if="loading && !serverItems.length" indeterminate color="primary" class="mb-4" />

  <!-- Пусто -->
  <v-alert v-else-if="!loading && !filteredItems.length" type="info" variant="tonal">
    Нет данных для отображения
  </v-alert>

  <!-- Таблица -->
  <v-expansion-panels v-else v-model="expandedPanels" multiple class="table-3d-wrapper">
    <v-expansion-panel
      v-for="item in paginatedItems"
      :key="item.id"
      :value="item.id"
      class="expansion-panel-item"
    >
      <v-expansion-panel-title class="panel-title">
        <v-row no-gutters align="center" class="w-100">
          <v-col cols="5" class="text-truncate pr-2">
            <strong>{{ item.name }}</strong>
          </v-col>
          <v-col cols="5" class="text-truncate">
            {{ item.fio }}
          </v-col>
          <v-col cols="2" class="text-center">
            <div class="action-buttons">
              <v-btn
                icon="mdi-delete"
                size="small"
                variant="text"
                color="error"
                @click.stop="openDeleteDialog(item)"
                title="Удалить"
              />
            </div>
          </v-col>
        </v-row>
      </v-expansion-panel-title>

      <v-expansion-panel-text>
        <div class="inner-table-wrapper">
          <v-table density="compact" class="inner-table">
            <thead>
              <tr>
                <th class="text-left">Вопрос</th>
                <th class="text-center">Ответ</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(qa, idx) in item.answers" :key="idx">
                <td class="font-weight-medium">{{ qa.question }}</td>
                <td class="text-center">
                  <span :class="`score-${getScoreClass(qa.answer)}`">
                    {{ qa.answer }}
                  </span>
                </td>
              </tr>
              <tr v-if="item.answers.length === 0">
                <td colspan="2" class="text-center text-grey">Нет данных</td>
              </tr>
            </tbody>
          </v-table>
          
          <v-divider class="my-3" />
          <v-row dense>
            <v-col cols="12" md="6">
              <small class="text-grey-darken-1">
                <v-icon size="small" class="mr-1">mdi-calendar</v-icon>
                Дата: {{ formatDate(item.created_at) }}
              </small>
            </v-col>
            <!-- <v-col cols="12" md="6">
              <small class="text-grey-darken-1">
                <v-icon size="small" class="mr-1">mdi-database</v-icon>
                ID отправки: {{ item.id }}
              </small>
            </v-col> -->
          </v-row>
        </div>
      </v-expansion-panel-text>
    </v-expansion-panel>
  </v-expansion-panels>

  <!-- Пагинация -->
  <div class="d-flex justify-center mt-4" v-if="totalPages > 1">
    <v-pagination
      v-model="currentPage"
      :length="totalPages"
      :total-visible="7"
      @update:model-value="onPageChange"
    />
  </div>

  <!-- Диалоги -->
  <TestDeleteDialog ref="deleteDialogRef" @confirm="handleDeleteConfirm" />
  
</template>

<script setup lang="ts">
import TestDeleteDialog from '@/views/Test/TestDeleteDialog.vue'
import { ref, onMounted, computed } from 'vue'

const API_BASE = 'http://127.0.0.1:8000/test'

// 🔹 Рефы для диалогов


// 🔹 Интерфейс: ТОЧНО как возвращает бэкенд
interface BackendSubmission {
  id: number
  section: string
  data: Record<string, any>
  created_at: string
}

// 🔹 Интерфейс: для отображения в таблице (после трансформации)
interface DisplayItem {
  id: number
  name: string
  fio: string
  answers: Array<{ question: string; answer: string }>
  created_at: string
}

// 🔹 Состояние
const itemsPerPage = ref(10)
const currentPage = ref(1)
const serverItems = ref<DisplayItem[]>([])
const totalItems = ref(0)
const loading = ref(false)
const search = ref('')
const expandedPanels = ref<number[]>([])

// 🔹 Загрузка и трансформация данных
const loadItems = async () => {
  loading.value = true
  try {
    const res = await fetch(`${API_BASE}/submissions?limit=100`)
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    
    const submissions: BackendSubmission[] = await res.json()
    console.log('📥 Получено с бэка:', submissions)
    
    // Трансформируем в формат для таблицы
    serverItems.value = submissions.map(sub => {
      // 1. Извлекаем ФИО
      let fio = 'Не указано'
      if (sub.data && typeof sub.data === 'object') {
        for (const [key, value] of Object.entries(sub.data)) {
          const k = String(key).toLowerCase()
          if (k.includes('фио') || k.includes('фамилия') || k.includes('name')) {
            fio = String(value)
            break
          }
        }
      }
      
      // 2. Превращаем объект ответов в массив {question, answer}
      const answersArray: Array<{ question: string; answer: string }> = []
      if (sub.data && typeof sub.data === 'object') {
        for (const [key, value] of Object.entries(sub.data)) {
          const k = String(key).toLowerCase()
          if (!k.includes('фио') && !k.includes('фамилия') && !k.includes('name')) {
            answersArray.push({
              question: String(key),
              answer: String(value)
            })
          }
        }
      }
      
      return {
        id: sub.id,
        name: sub.section,
        fio,
        answers: answersArray,
        created_at: sub.created_at
      }
    })
    
    totalItems.value = serverItems.value.length
    console.log('✅ Готово для отображения:', serverItems.value)
    
  } catch (err: any) {
    console.error('❌ Ошибка загрузки:', err)
    alert(`Не удалось загрузить: ${err.message}`)
  } finally {
    loading.value = false
  }
}

// 🔹 Вспомогательные функции
const formatDate = (isoString: string): string => {
  try {
    return new Date(isoString).toLocaleString('ru-RU', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    })
  } catch {
    return isoString
  }
}

const getScoreClass = (answer: string): string => {
  const a = String(answer).trim().toLowerCase()
  if (['5', 'пять', 'отлично', 'отл'].includes(a)) return '5'
  if (['4', 'четыре', 'хорошо', 'хор'].includes(a)) return '4'
  if (['3', 'три', 'удовл', 'уд'].includes(a)) return '3'
  if (['2', 'два', 'неуд', 'неудовл'].includes(a)) return '2'
  return ''
}

// 🔹 Фильтрация и пагинация
const filteredItems = computed(() => {
  let data = [...serverItems.value]
  if (search.value) {
    const s = search.value.toLowerCase()
    data = data.filter(item => 
      item.name?.toLowerCase().includes(s) ||
      item.fio?.toLowerCase().includes(s)
    )
  }
  return data
})

const totalPages = computed(() => 
  Math.ceil(filteredItems.value.length / itemsPerPage.value)
)

const paginatedItems = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value
  return filteredItems.value.slice(start, start + itemsPerPage.value)
})

// 🔹 Обработчики
const onPageChange = () => {
  expandedPanels.value = []
}



const deleteDialogRef = ref<any>(null)
const itemToDelete = ref<DisplayItem | null>(null)

const openDeleteDialog = (item: DisplayItem) => {
  itemToDelete.value = item
  deleteDialogRef.value?.open({
    title: 'Удаление отправки',
    text: `Вы уверены, что хотите удалить отправку "${item.name}" от ${item.fio}?`,
    confirmText: 'Удалить',
    cancelText: 'Отмена'
  })
}

// Подтверждение удаления
const handleDeleteConfirm = async () => {
  if (!itemToDelete.value) return
  
  try {
    const res = await fetch(`${API_BASE}/submissions/${itemToDelete.value.id}`, {
      method: 'DELETE'
    })
    
    if (!res.ok) {
      const err = await res.json().catch(() => ({}))
      throw new Error(err.detail || `HTTP ${res.status}`)
    }
    
    alert('✅ Отправка удалена')
    loadItems() // Перезагружаем список
    
  } catch (err: any) {
    alert(`❌ Ошибка удаления: ${err.message}`)
    console.error('Delete error:', err)
  } finally {
    itemToDelete.value = null
  }
}




onMounted(() => {
  loadItems()
})
</script>

<style lang="scss" scoped>
.table-header { padding: 0 8px; }

.score-5 {
  color: #4CAF50 !important;
  font-weight: 700;
  background: rgba(76, 175, 80, 0.1);
  padding: 2px 8px;
  border-radius: 12px;
  display: inline-block;
  min-width: 24px;
  text-align: center;
}
.score-4 {
  color: #2196F3 !important;
  font-weight: 600;
  background: rgba(33, 150, 243, 0.1);
  padding: 2px 8px;
  border-radius: 12px;
  display: inline-block;
  min-width: 24px;
  text-align: center;
}
.score-3 {
  color: #FF9800 !important;
  background: rgba(255, 152, 0, 0.1);
  padding: 2px 8px;
  border-radius: 12px;
  display: inline-block;
  min-width: 24px;
  text-align: center;
}
.score-2, .score-1 {
  color: #F44336 !important;
  font-weight: 600;
  background: rgba(244, 67, 54, 0.1);
  padding: 2px 8px;
  border-radius: 12px;
  display: inline-block;
  min-width: 24px;
  text-align: center;
}

.table-3d-wrapper {
  padding: 4px;
  background: linear-gradient(145deg, #e6e6e6, #ffffff);
  border-radius: 16px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.15), inset 0 1px 0 rgba(255,255,255,0.8);
  position: relative;
  overflow: hidden;
}
.table-3d-wrapper::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 16px;
  padding: 2px;
  background: linear-gradient(135deg, rgba(45,50,255,0.6), rgba(41,182,246,0.4), rgba(45,50,255,0.6));
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}

:deep(.v-expansion-panel) {
  background: transparent !important;
  box-shadow: none !important;
  margin: 0 !important;
}
:deep(.v-expansion-panel__shadow) { display: none !important; }

.panel-title {
  background: white !important;
  border-radius: 12px !important;
  margin: 4px 0 !important;
  transition: all 0.2s ease;
  border: 2px solid transparent;
  &:hover {
    border-color: rgba(45,50,255,0.3);
    background: rgba(45,50,255,0.03) !important;
  }
}
:deep(.v-expansion-panel-title--active) {
  border-color: rgba(45,50,255,0.6) !important;
  background: rgba(45,50,255,0.05) !important;
}
:deep(.v-expansion-panel-title__overlay) { display: none !important; }

.inner-table-wrapper {
  padding: 16px 24px;
  background: #fafafa;
  border-radius: 0 0 12px 12px;
}
.inner-table {
  background: white !important;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
.inner-table :deep(th) {
  background: linear-gradient(135deg, #2D32FF 0%, #29b6f6 100%) !important;
  color: white !important;
  font-weight: 700 !important;
  font-size: 0.8rem;
  text-transform: uppercase;
}
.inner-table :deep(td) {
  border-bottom: 1px solid #eee !important;
  font-size: 0.9rem;
}
.inner-table :deep(tr:last-child td) { border-bottom: none !important; }

.action-buttons {
  display: flex;
  gap: 2px;
  justify-content: center;
}

.table-3d-wrapper { animation: slideIn 0.4s ease-out; }
@keyframes slideIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 768px) {
  .panel-title :deep(.v-row) {
    flex-direction: column;
    align-items: flex-start !important;
    gap: 8px;
  }
  .inner-table-wrapper { padding: 12px 16px; }
}
</style>