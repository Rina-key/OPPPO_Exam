<template>
  <v-container 
    class="rounded-xl mt-4 mt-md-6 py-4 py-md-6 px-2 px-md-6"
    :class="containerClass"
    max-width="1400"
  >
    
    <!-- HEADER -->
    <v-row class="mb-4 mb-md-6">
      <v-col cols="12" class="text-center">
        <div class="d-flex align-center justify-center mb-2">
          <v-avatar class="mr-3 header-avatar" color="primary" size="48">
            <v-icon color="white" size="28">mdi-playlist-check</v-icon>
          </v-avatar>
          <h1 class="text-h4 text-md-h3 font-weight-bold gradient-text mb-0">
            Мой список задач
          </h1>
        </div>
        <p class="text-body-2 text-medium-emphasis">
          Управляйте своими задачами эффективно
        </p>
      </v-col>
    </v-row>

    <!-- 🔍 Поле поиска -->
    <v-row class="mb-4 mb-md-6">
      <v-col cols="12">
        <v-text-field
          v-model="searchQuery"
          label="Поиск по теме..."
          prepend-inner-icon="mdi-magnify"
          clearable
          variant="outlined"
          density="comfortable"
          hide-details
          rounded="xl"
          class="search-field"
        ></v-text-field>
      </v-col>
    </v-row>

    <!-- Stats & Actions -->
    <v-row class="mb-4 align-center">
      <v-col cols="12" md="8" class="text-center text-md-left mb-4 mb-md-0">
        <div class="d-flex flex-column flex-md-row align-center align-md-start justify-center justify-md-start gap-3">
          <h2 class="text-h5 font-weight-bold gradient-text mb-0">
            Осталось задач:&nbsp;
            <v-fade-transition leave-absolute>
              <span :key="`remaining-${remainingInFiltered}`" class="text-primary">
                {{ remainingInFiltered }}
              </span>
            </v-fade-transition>
          </h2>
        </div>
      </v-col>
      <v-col cols="12" md="4" class="text-center text-md-right">
        <v-btn 
          class="gradient-btn font-weight-bold rounded-pill px-6" 
          @click="openCreate"
          size="large"
        >
          <v-icon start>mdi-plus</v-icon>
          Добавить задачу
        </v-btn>
      </v-col>
    </v-row>

    <!-- Progress Stats -->
    <v-card class="stats-card rounded-xl mb-4" variant="outlined">
      <v-card-text class="pa-4">
        <v-row class="align-center">
          <v-col cols="12" md="auto" class="text-center mb-3 mb-md-0">
            <div class="d-flex align-center justify-center gap-4">
              <div class="text-center">
                <div class="text-h6 font-weight-bold text-info">
                  {{ filteredRemaining }}
                </div>
                <div class="text-caption text-medium-emphasis">Осталось</div>
              </div>
              <v-divider vertical class="mx-2"></v-divider>
              <div class="text-center">
                <div class="text-h6 font-weight-bold text-success">
                  {{ filteredCompleted }}
                </div>
                <div class="text-caption text-medium-emphasis">Выполнено</div>
              </div>
            </div>
          </v-col>

          <v-col cols="12" md="6">
            <v-progress-linear
              v-model="filteredProgress"
              :color="progressColor"
              height="8"
              rounded
              class="rounded-pill"
              :class="{'animate-progress': allTasksCompleted}"
            ></v-progress-linear>
          </v-col>

          <v-col cols="12" md="auto" class="text-center mt-3 mt-md-0">
            <!-- ✅ Индикатор: прогресс или галочка -->
            <v-fade-transition mode="out-in">
              <v-progress-circular 
                v-if="!allTasksCompleted"
                :key="'progress'"
                :model-value="filteredProgress"
                :color="progressColor"
                :rotate="rotate"
                :size="48"
                :width="4"
              >
                <span class="text-caption font-weight-bold">{{ filteredProgress }}%</span>
              </v-progress-circular>
              <v-icon 
                v-else
                :key="'check'"
                icon="mdi-check-circle"
                color="success"
                size="48"
                class="animate-bounce"
              />
            </v-fade-transition>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <!-- ✅ Список задач с фильтрацией и сортировкой -->
    <v-card v-if="filteredTasks.length > 0" class="tasks-card rounded-xl" variant="flat">
      <v-list class="pa-2">
        <template v-for="(task, i) in filteredTasks" :key="task.id">
          <v-divider v-if="i !== 0" class="my-1"></v-divider>

          <v-list-item
            class="task-item rounded-lg mb-1"
            :class="{ 'task-completed': task.done }"
            density="comfortable"
          >
            <template #prepend>
              <v-checkbox-btn 
                v-model="task.done" 
                color="success"
                class="mr-3"
                hide-details
              ></v-checkbox-btn>
            </template>

            <v-list-item-title @click="toggleExpand(i)" class="cursor-pointer">
              <div class="d-flex align-center flex-wrap">
                <span :class="task.done ? 'text-grey text-decoration-line-through' : 'text-primary font-weight-medium'">
                  {{ task.topic }}
                </span>
                <!-- 📅 Бейдж срочности для невыполненных задач с дедлайном -->
                <v-chip 
                  v-if="!task.done && task.deadline" 
                  size="small" 
                  :color="getDeadlineUrgency(task.deadline)"
                  variant="tonal"
                  class="ml-2 rounded-pill"
                >
                  <v-icon start size="x-small" class="mr-1">mdi-clock</v-icon>
                  {{ formatDeadline(task.deadline) }}
                </v-chip>
                <v-chip 
                  v-if="task.done"
                  size="small"
                  color="success"
                  variant="tonal"
                  class="ml-2 rounded-pill"
                >
                  <v-icon start size="x-small">mdi-check</v-icon>
                  Выполнено
                </v-chip>
              </div>
              <div class="d-flex align-center mt-1">
                <small class="text-grey text-caption">
                  <v-icon size="x-small" class="mr-1">mdi-calendar</v-icon>
                  Дедлайн: {{ task.deadline ? formatDeadlineFull(task.deadline) : 'не указан' }}
                </small>
              </div>
            </v-list-item-title>

            <template #append>
              <div class="d-flex">
                <v-btn 
                  icon="mdi-pencil" 
                  color="primary"
                  variant="text" 
                  size="small"
                  @click.stop="editTaskByIndex(i)"
                  class="mr-1"
                  aria-label="Редактировать задачу"
                ></v-btn>
                <v-btn 
                  icon="mdi-delete" 
                  variant="text" 
                  size="small"
                  color="error"
                  @click.stop="confirmDelete(i)"
                  aria-label="Удалить задачу"
                ></v-btn>
              </div>
            </template>
          </v-list-item>

          <v-expand-transition>
            <div v-if="expanded === i" class="px-12 pb-3">
              <v-card variant="tonal" color="grey-lighten-4" class="rounded-lg pa-3">
                <div class="d-flex align-start">
                  <v-icon color="primary" class="mr-2 mt-1">mdi-text-box-outline</v-icon>
                  <div class="text-body-2 text-black">
                    {{ task.description || 'Нет описания' }}
                  </div>
                </div>
              </v-card>
            </div>
          </v-expand-transition>
        </template>
      </v-list>
    </v-card>

    <!-- Пустые состояния -->
    <v-card v-else class="rounded-xl pa-8 text-center" variant="outlined">
      <v-icon 
        size="64" 
        :color="searchQuery ? 'info' : 'primary'"
        class="mb-3"
      >
        {{ searchQuery ? 'mdi-search-off' : 'mdi-clipboard-text-outline' }}
      </v-icon>
      <v-alert 
        :type="searchQuery ? 'info' : 'success'" 
        variant="tonal"
        class="rounded-xl"
      >
        <div v-if="searchQuery">
          <strong>Ничего не найдено</strong><br>
          По запросу «{{ searchQuery }}» задач нет
        </div>
        <div v-else>
          <strong>Список задач пуст</strong><br>
          Добавьте первую задачу, чтобы начать!
        </div>
      </v-alert>
    </v-card>

    <!-- Диалог создания/редактирования -->
    <v-dialog v-model="dialog" max-width="600" >
      <v-card class="rounded-2xl dialog-card">
        <v-card-title class="dialog-header d-flex align-center">
          <v-icon class="mr-3" color="white">
            {{ editIndex !== null ? 'mdi-pencil' : 'mdi-plus-circle' }}
          </v-icon>
          <span class="text-h6 font-weight-bold">
            {{ editIndex !== null ? 'Редактировать задачу' : 'Новая задача' }}
          </span>
        </v-card-title>

        <v-card-text class="pt-4">
          <v-row>
            <v-col cols="12">
              <v-text-field 
                v-model="form.topic" 
                label="Тема *"
                variant="outlined"
                rounded="lg"
                hide-details
                :rules="[v => !!v || 'Тема обязательна']"
                class="mb-3"
              ></v-text-field>
            </v-col>

            <v-col cols="12">
              <v-textarea
                v-model="form.description"
                label="Описание"
                rows="3"
                variant="outlined"
                rounded="lg"
                hide-details
                class="mb-3"
              ></v-textarea>
            </v-col>

            <v-col cols="12">
              <v-text-field
                v-model="form.deadline"
                label="Дедлайн"
                type="date"
                variant="outlined"
                rounded="lg"
                hide-details
                prepend-inner-icon="mdi-calendar"
              ></v-text-field>
            </v-col>
          </v-row>
        </v-card-text>

        <v-card-actions class="pa-4">
          <v-spacer></v-spacer>
          <v-btn 
            variant="text" 
            @click="dialog = false"
            class="rounded-pill px-4"
          >
            Отмена
          </v-btn>
          <v-btn 
            color="primary" 
            @click="saveTask"
            class="rounded-pill px-6 font-weight-bold"
            variant="flat"
          >
            Сохранить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Диалог подтверждения удаления -->
    <v-dialog v-model="deleteDialog" max-width="420" >
      <v-card class="text-center pa-4 rounded-2xl delete-dialog">
        <div class="delete-icon-wrapper mb-3">
          <v-icon size="64" color="error" class="rounded-circle">mdi-delete</v-icon>
        </div>

        <v-card-title class="text-h6 font-weight-bold mb-2">
          Удаление задачи
        </v-card-title>

        <v-card-text class="text-body-1 mb-4">
          Вы действительно хотите удалить задачу:<br>
          <strong class="text-primary">"{{ tasks[deleteIndex ?? 0]?.topic }}"</strong>?
        </v-card-text>

        <v-card-actions class="justify-center">
          <v-btn
            variant="outlined"
            @click="deleteDialog = false"
            class="rounded-pill px-6 mr-2"
          >
            Отмена
          </v-btn>
          <v-btn
            color="error"
            variant="flat"
            @click="deleteTask"
            class="rounded-pill px-6"
          >
            Удалить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- 🎉 Тост: поздравление при завершении всех задач -->
    <v-snackbar 
      v-model="showCongrats" 
      :timeout="4000" 
      color="success" 
      location="top"
      class="rounded-pill"
    >
      <div class="d-flex align-center">
        <v-icon class="mr-2">mdi-party-popper</v-icon>
        <span>🎉 Все задачи выполнены! Отличная работа!</span>
      </div>
    </v-snackbar>

  </v-container>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'

/* ====== Типы ====== */
interface Task {
  id: string
  topic: string
  description: string
  deadline: string | null
  done: boolean
}

type TaskForm = Omit<Task, 'id' | 'done'>

/* ====== State ====== */
const tasks = ref<Task[]>([])
const searchQuery = ref<string>('')

const dialog = ref<boolean>(false)
const editIndex = ref<number | null>(null)
const expanded = ref<number | null>(null)

// Удаление
const deleteDialog = ref(false)
const deleteIndex = ref<number | null>(null)

// 🎉 Снэкбар поздравления
const showCongrats = ref(false)

const form = ref<TaskForm>({
  topic: '',
  description: '',
  deadline: null,
})

/* ====== Вспомогательные функции ====== */

function generateId(): string {
  if (typeof crypto !== 'undefined' && crypto.randomUUID) {
    return crypto.randomUUID()
  }
  return Date.now().toString(36) + Math.random().toString(36).slice(2)
}

function parseDeadline(deadline: string | null): number {
  if (!deadline) return Infinity
  const time = new Date(deadline).getTime()
  return isNaN(time) ? Infinity : time
}

function getDeadlineUrgency(deadline: string): 'error' | 'warning' | 'success' {
  const diff = new Date(deadline).getTime() - Date.now()
  const days = Math.ceil(diff / (1000 * 60 * 60 * 24))
  
  if (days < 0) return 'error'
  if (days <= 3) return 'warning'
  return 'success'
}

function formatDeadline(deadline: string): string {
  const date = new Date(deadline)
  return date.toLocaleDateString('ru-RU', { day: 'numeric', month: 'short' })
}

function formatDeadlineFull(deadline: string): string {
  const date = new Date(deadline)
  return date.toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' })
}

/* ====== Computed: фильтрация + сортировка ====== */

const filteredTasks = computed<Task[]>(() => {
  let result = [...tasks.value]
  
  if (searchQuery.value.trim()) {
    const query = searchQuery.value.toLowerCase()
    result = result.filter(task => 
      task.topic.toLowerCase().includes(query)
    )
  }
  
  return result.sort((a, b) => {
    if (a.done !== b.done) {
      return a.done ? 1 : -1
    }
    if (!a.done) {
      return parseDeadline(a.deadline) - parseDeadline(b.deadline)
    }
    return 0
  })
})

const remainingInFiltered = computed(() => 
  filteredTasks.value.filter(t => !t.done).length
)

const filteredCompleted = computed(() => 
  filteredTasks.value.filter(t => t.done).length
)
const filteredRemaining = computed(() => 
  filteredTasks.value.filter(t => !t.done).length
)

const filteredProgress = computed(() => {
  if (filteredTasks.value.length === 0) return 0
  return Math.round((filteredCompleted.value / filteredTasks.value.length) * 100)
})

// ✅ Все задачи выполнены?
const allTasksCompleted = computed(() => {
  return filteredTasks.value.length > 0 && filteredRemaining.value === 0
})

// 🎨 Цвет прогресс-бара в зависимости от прогресса
const progressColor = computed(() => {
  const p = filteredProgress.value
  if (p >= 100) return 'success'
  if (p >= 50) return 'primary'
  return 'warning'
})

// 🌀 Анимация вращения для прогресс-бара
const rotate = computed(() => {
  return allTasksCompleted.value ? 360 : 0
})

// Вычисляемый класс для контейнера с градиентом
const containerClass = computed(() => ({
  'bg-gradient': true
}))

/* ====== Методы ====== */

function openCreate(): void {
  form.value = { topic: '', description: '', deadline: null }
  editIndex.value = null
  dialog.value = true
}

function saveTask(): void {
  if (!form.value.topic.trim()) return

  if (editIndex.value !== null) {
    const existing = tasks.value[editIndex.value]
    if (existing) {
      tasks.value[editIndex.value] = { 
        ...existing, 
        ...form.value 
      }
    }
  } else {
    tasks.value.push({
      id: generateId(),
      ...form.value,
      done: false,
    })
  }
  dialog.value = false
}

const getOriginalIndex = (filteredIndex: number): number => {
  if (!searchQuery.value.trim()) return filteredIndex
  const task = filteredTasks.value[filteredIndex]
  if (!task) return -1
  return tasks.value.findIndex(t => t.id === task.id)
}

function editTaskByIndex(filteredIndex: number): void {
  const originalIndex = getOriginalIndex(filteredIndex)
  if (originalIndex === -1) return
  const task = tasks.value[originalIndex]
  if (!task) return
  form.value = {
    topic: task.topic,
    description: task.description,
    deadline: task.deadline,
  }
  editIndex.value = originalIndex
  dialog.value = true
}

function confirmDelete(filteredIndex: number): void {
  const originalIndex = getOriginalIndex(filteredIndex)
  if (originalIndex === -1) return
  deleteIndex.value = originalIndex
  deleteDialog.value = true
}

function deleteTask(): void {
  if (deleteIndex.value !== null) {
    if (expanded.value !== null) {
      const expandedOriginal = getOriginalIndex(expanded.value)
      if (expandedOriginal === deleteIndex.value) {
        expanded.value = null
      }
    }
    tasks.value.splice(deleteIndex.value, 1)
    deleteDialog.value = false
    deleteIndex.value = null
  }
}

function toggleExpand(index: number): void {
  expanded.value = expanded.value === index ? null : index
}

/* ====== Watch: поздравление при 100% ====== */
watch(allTasksCompleted, (newValue, oldValue) => {
  // Показываем тост, когда только что завершили все задачи
  if (newValue && !oldValue && filteredTasks.value.length > 0) {
    showCongrats.value = true
  }
})
</script>

<style scoped lang="scss">
// Цвета брендбука
$primary: #2D32FF;
$secondary: #66B5F6;
$accent: #FF25B8;
$light-pink: #FF80D6;

// Фон контейнера с легким градиентом
.bg-gradient {
  background: linear-gradient(180deg, #fafafa 0%, #f0f4ff 100%);
}

// Градиентный текст
.gradient-text {
  background: linear-gradient(135deg, $primary 0%, $secondary 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

// Градиентная кнопка
.gradient-btn {
  background: linear-gradient(135deg, $primary 0%, $secondary 100%) !important;
  color: white !important;
  box-shadow: 0 4px 15px rgba(45, 50, 255, 0.3) !important;
  transition: all 0.3s ease !important;
  
  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(45, 50, 255, 0.4) !important;
  }
}

// Аватар в заголовке
.header-avatar {
  background: linear-gradient(135deg, $primary 0%, $secondary 100%);
}

// Поле поиска
.search-field {
  :deep(.v-field) {
    border-color: rgba(45, 50, 255, 0.2);
    transition: all 0.3s ease;
    
    &:hover {
      border-color: $primary;
    }
    
    &.v-field--focused {
      border-color: $primary;
      box-shadow: 0 0 0 3px rgba(45, 50, 255, 0.1);
    }
  }
}

// Карточка статистики
.stats-card {
  border-color: rgba(45, 50, 255, 0.1) !important;
  background: linear-gradient(135deg, rgba(45, 50, 255, 0.03) 0%, #ff25b808 100%);
}

// Карточка задач
.tasks-card {
  box-shadow: 0 4px 20px rgba(45, 50, 255, 0.08);
  border: 1px solid rgba(45, 50, 255, 0.05);
}

// Элемент задачи
.task-item {
  transition: all 0.3s ease;
  border: 1px solid rgba(45, 50, 255, 0.08);
  
  &:hover {
    background: linear-gradient(135deg, rgba(45, 50, 255, 0.05) 0%, rgba(102, 181, 246, 0.05) 100%) !important;
    transform: translateX(4px);
    box-shadow: 0 2px 8px rgba(45, 50, 255, 0.1);
  }
  
  &.task-completed {
    opacity: 0.7;
    background: rgba(0, 0, 0, 0.02) !important;
  }
}

// Курсор для заголовка
.cursor-pointer {
  cursor: pointer;
  user-select: none;
  
  &:hover {
    opacity: 0.9;
  }
}

// Диалог
.dialog-card {
  overflow: hidden;
}

.dialog-header {
  background: linear-gradient(135deg, $primary 0%, $accent 100%);
  color: white;
  padding: 20px 24px;
}

// Диалог удаления
.delete-dialog {
  border: 2px solid rgba(255, 37, 184, 0.1);
}

.delete-icon-wrapper {
  background: linear-gradient(135deg, rgba(255, 37, 184, 0.1) 0%, rgba(255, 128, 214, 0.1) 100%);
  width: 100px;
  height: 100px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
}

// Gap utility
.gap-3 {
  gap: 12px;
}

.gap-4 {
  gap: 16px;
}

// Анимация прогресса
.animate-progress {
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.7;
  }
}

// 🎉 Анимация появления галочки
.animate-bounce {
  animation: bounce 0.5s ease-out;
}

@keyframes bounce {
  0% {
    transform: scale(0);
    opacity: 0;
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}

// Адаптивность
@media (max-width: 600px) {
  .stats-card {
    .v-row {
      flex-direction: column;
    }
    
    .v-col-md-auto {
      width: 100% !important;
      margin-bottom: 16px;
    }
  }
}
</style>