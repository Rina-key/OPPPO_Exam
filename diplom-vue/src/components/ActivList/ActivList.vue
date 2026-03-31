<template>
  <!-- Заголовок и кнопка добавления -->
  <div class="table-header d-flex justify-space-between align-center mb-4">
    <h2 class="text-h5 font-weight-bold text-primary">Список активистов</h2>
    <v-btn
      color="#2D32FF"
      prepend-icon="mdi-plus"
      @click="addActivist"
      class="text-none"
    >
      Добавить активиста
    </v-btn>
  </div>

  <v-data-table-server
    locale="ru"
    v-model:items-per-page="itemsPerPage"
    :headers="headers"
    :items="serverItems"
    :items-length="totalItems"
    :loading="loading"
    :search="search"
    item-value="id"
    @update:options="loadItems"
    class="table-3d"
    fixed-header
    height="700"
  >
    <template v-slot:item.actions="{ item }">
      <div class="action-buttons">
        <v-btn
          icon="mdi-pencil"
          size="small"
          variant="text"
          color="primary"
          @click="editItem(item)"
          title="Редактировать"
        />
        <v-btn
          icon="mdi-delete"
          size="small"
          variant="text"
          color="error"
          @click="deleteItem(item)"
          title="Удалить"
        />
      </div>
    </template>
  </v-data-table-server>

  <DeleteDialog 
    ref="deleteDialogRef" 
    @confirm="handleDeleteConfirm"
  />
  <EditDialog 
    ref="editDialogRef" 
    @confirm="handleEditConfirm"
  />
  <CreateDialog 
    ref="addDialogRef" 
    @confirm="handleAddConfirm"
  />
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { activistApi } from '@/api/activist'
import type { Activist, ActivistCreate } from '@/types/activist'
import DeleteDialog from '@/components/ActivList/DeleteDialog.vue'
import EditDialog from '@/components/ActivList/EditDialog.vue'
import CreateDialog from '@/components/ActivList/CreateDialog.vue'
import apiClient from '@/api/axios'

// 🔹 Рефы для диалогов
const deleteDialogRef = ref<InstanceType<typeof DeleteDialog> | null>(null)
const editDialogRef = ref<InstanceType<typeof EditDialog> | null>(null)
const addDialogRef = ref<InstanceType<typeof CreateDialog> | null>(null)

// 🔹 Состояние таблицы
const itemsPerPage = ref(10)
const serverItems = ref<Activist[]>([])
const totalItems = ref(0)
const loading = ref(false)
const search = ref('')



// 🔹 Заголовки таблицы (key должен совпадать с полями в Activist)
const headers = [
  { title: 'ФИО', key: 'name', sortable: true },
  { title: 'Никнейм', key: 'username', sortable: true },
  { title: 'Группа', key: 'group', sortable: true },
  { title: 'Телефон', key: 'phone', sortable: false },
  { title: 'Почта', key: 'email', sortable: false },
  { title: 'Дата рождения', key: 'birth', sortable: true },
  { title: 'Форма обучения', key: 'education', sortable: true },
  { title: 'ВК', key: 'vk', sortable: false },
  { title: 'ТГ', key: 'tg', sortable: false },
  { title: 'Действия', key: 'actions', sortable: false, align: 'center', width: 120 },
]

// 🔹 Загрузка данных с бэкенда (пагинация/сортировка/поиск на фронте)
const loadItems = async ({ page, itemsPerPage, sortBy }: { 
  page: number, itemsPerPage: number, sortBy: Array<{ key: string, order: 'asc' | 'desc' }> 
}) => {
  loading.value = true
  try {
    // Получаем ВСЕ данные с бэка
    const allData = await activistApi.getAll()
    
    // 1. Поиск (фильтрация)
    let filtered = [...allData]
    if (search.value) {
      const s = search.value.toLowerCase()
      filtered = filtered.filter(item => 
        item.name?.toLowerCase().includes(s) ||
        item.group?.toLowerCase().includes(s) ||
        item.email?.toLowerCase().includes(s) ||
        item.username?.toLowerCase().includes(s) ||
        item.phone?.toLowerCase().includes(s)
      )
    }
    
    // 2. Сортировка
    if (sortBy.length && sortBy[0]) {
      const { key, order } = sortBy[0]
      filtered.sort((a, b) => {
        const aVal = a[key as keyof Activist]
        const bVal = b[key as keyof Activist]
        
        // Обработка null/undefined
        if (aVal == null && bVal == null) return 0
        if (aVal == null) return order === 'asc' ? -1 : 1
        if (bVal == null) return order === 'asc' ? 1 : -1
        
        // Строковая сортировка с поддержкой русского алфавита
        if (typeof aVal === 'string' && typeof bVal === 'string') {
          return order === 'asc' 
            ? aVal.localeCompare(bVal, 'ru') 
            : bVal.localeCompare(aVal, 'ru')
        }
        
        // Числовая сортировка
        if (typeof aVal === 'number' && typeof bVal === 'number') {
          return order === 'asc' ? aVal - bVal : bVal - aVal
        }
        
        // Сортировка по дате (если поле строковое)
        if (key === 'birth') {
          const dateA = new Date(aVal as string).getTime()
          const dateB = new Date(bVal as string).getTime()
          return order === 'asc' ? dateA - dateB : dateB - dateA
        }
        
        return 0
      })
    }
    
    // 3. Пагинация на фронте
    const start = (page - 1) * itemsPerPage
    const paginated = filtered.slice(start, start + itemsPerPage)
    
    serverItems.value = paginated
    totalItems.value = filtered.length
    
  } catch (err: any) {
    console.error('❌ Ошибка загрузки:', err)
    const msg = err.response?.data?.detail || err.message || 'Неизвестная ошибка'
    alert(`Не удалось загрузить список: ${msg}`)
    serverItems.value = []
    totalItems.value = 0
  } finally {
    loading.value = false
  }
}

// 🔹 Добавление активиста
const addActivist = () => {
  addDialogRef.value?.open()
}

const handleAddConfirm = async (newItem: ActivistCreate) => {
  try {
    // Валидация обязательных полей
    if (!newItem.username?.trim() || !newItem.password)  {
      alert('❌ Заполните обязательные поля: логин, пароль, ФИО')
      return
    }

    await activistApi.create(newItem)
    alert('✅ Активист успешно добавлен')
    
    // Перезагружаем таблицу с первой страницы
    loadItems({ page: 1, itemsPerPage: itemsPerPage.value, sortBy: [] })
    
  } catch (err: any) {
    console.error('❌ Ошибка создания:', err)
    const msg = err.response?.data?.detail || 'Ошибка при добавлении'
    alert(`❌ ${msg}`)
  }
}

// 🔹 Редактирование активиста
const editItem = (item: Activist) => {
  editDialogRef.value?.open(item)
}

const handleEditConfirm = async (updatedItem: Activist) => {
  try {
    await activistApi.update(updatedItem.id, updatedItem)
    alert('✅ Данные обновлены')
    loadItems({ page: 1, itemsPerPage: itemsPerPage.value, sortBy: [] })
  } catch (err: any) {
    console.error('❌ Ошибка обновления:', err)
    const msg = err.response?.data?.detail || 'Ошибка обновления'
    alert(`❌ ${msg}`)
  }
}

// 🔹 Удаление активиста
const deleteItem = (item: Activist) => {
  deleteDialogRef.value?.open(item)
}

const handleDeleteConfirm = async (item: Activist) => {
  try {
    await activistApi.delete(item.id)
    alert('✅ Активист удалён')
    loadItems({ page: 1, itemsPerPage: itemsPerPage.value, sortBy: [] })
  } catch (err: any) {
    console.error('❌ Ошибка удаления:', err)
    const msg = err.response?.data?.detail || 'Ошибка удаления'
    alert(`❌ ${msg}`)
  }
}

// 🔹 Загрузка при монтировании
onMounted(() => {
  loadItems({ page: 1, itemsPerPage: itemsPerPage.value, sortBy: [] })
})
</script>

<style lang="scss" scoped>
.table-header {
  padding: 0 8px;
}

/* 3D-обёртка для таблицы */
.table-3d-wrapper {
  padding: 4px;
  background: linear-gradient(145deg, #e6e6e6, #ffffff);
  border-radius: 16px;
  box-shadow: 
    0 20px 60px rgba(0, 0, 0, 0.15),
    inset 0 1px 0 rgba(255, 255, 255, 0.8),
    inset 0 -1px 0 rgba(0, 0, 0, 0.1);
  position: relative;
}

/* Объёмная рамка через псевдоэлементы */
.table-3d-wrapper::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border-radius: 16px;
  padding: 2px;
  background: linear-gradient(
    135deg,
    rgba(1, 113, 188, 0.6) 0%,
    rgba(41, 182, 246, 0.4) 50%,
    rgba(1, 113, 188, 0.6) 100%
  );
  -webkit-mask: 
    linear-gradient(#fff 0 0) content-box, 
    linear-gradient(#fff 0 0);
  mask: 
    linear-gradient(#fff 0 0) content-box, 
    linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}

/* Стили самой таблицы */
.table-3d {
  border-radius: 14px !important;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
}

/* Убираем стандартные границы Vuetify */
.table-3d :deep(.v-table__wrapper) {
  border: none !important;
}

/* Стили заголовков */
.table-3d :deep(th) {
  background: linear-gradient(135deg, #2D32FF 0%, #29b6f6 100%) !important;
  color: white !important;
  font-weight: 800 !important;
  text-transform: uppercase;
  font-size: 0.95rem;
  letter-spacing: 0.5px;
  border: none !important;
}

/* Стили ячеек */
.table-3d :deep(td) {
  border-bottom: 1px solid rgba(1, 113, 188, 0.1) !important;
  transition: background 0.2s ease;
}

/* Hover-эффект для строк */
.table-3d :deep(tbody tr:hover) {
  background: linear-gradient(90deg, rgba(41, 182, 246, 0.1) 0%, transparent 100%) !important;
  transform: translateX(4px);
  transition: all 0.2s ease;
}

/* Анимация появления */
.table-3d-wrapper {
  animation: slideIn 0.4s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Адаптив для мобильных */
@media (max-width: 600px) {
  .table-3d-wrapper {
    border-radius: 12px;
    padding: 3px;
  }
  
  .table-3d :deep(th) {
    font-size: 0.75rem;
    padding: 8px 4px !important;
  }
  
  .table-3d :deep(td) {
    padding: 12px 4px !important;
    font-size: 0.9rem;
  }
}
</style>