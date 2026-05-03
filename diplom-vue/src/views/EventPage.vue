<template>
  <v-container 
    class="rounded-xl mt-4 mt-md-6 py-4 py-md-6 px-2 px-md-6"
    :class="containerClass"
    max-width="1400"
  >

    <!-- HEADER -->
    <div class="table-header d-flex flex-column flex-md-row justify-space-between align-center mb-4 mb-md-6">
      <h2 class="text-h5 text-md-h4 font-weight-bold gradient-text mb-3 mb-md-0">
        Мероприятия
      </h2>

      <v-btn 
        class="gradient-btn font-weight-bold rounded-pill px-6" 
        @click="openCreateDialog"
        size="large"
      >
        <v-icon start>mdi-plus</v-icon>
        Создать
      </v-btn>
    </div>

    <!-- SEARCH -->
    <v-text-field
      v-model="search"
      prepend-inner-icon="mdi-magnify"
      label="Поиск мероприятий..."
      variant="outlined"
      density="comfortable"
      class="mb-4 mb-md-6 search-field"
      clearable
      hide-details
      rounded="xl"
    />

    <!-- EMPTY -->
    <v-alert 
      v-if="!filteredEvents.length" 
      type="info" 
      variant="tonal"
      class="rounded-xl"
      color="primary"
    >
      <div class="text-center py-4">
        <v-icon size="48" class="mb-2">mdi-calendar-blank</v-icon>
        <div>Нет мероприятий</div>
      </div>
    </v-alert>

    <!-- TABLE -->
    <v-expansion-panels 
      multiple 
      class="table-3d-wrapper"
      variant="accordion"
    >

      <v-expansion-panel
        v-for="event in filteredEvents"
        :key="event.id"
        class="mb-3"
      >

        <!-- ROW -->
        <v-expansion-panel-title class="panel-title rounded-xl">
          <v-row class="w-100" align="center">

            <!-- Mobile View -->
            <v-col cols="12" class="d-md-none">
              <div class="d-flex justify-space-between align-start">
                <div>
                  <strong class="text-h6">{{ event.title }}</strong>
                  <div class="text-caption text-medium-emphasis mt-1">
                    <v-icon size="small" class="mr-1">mdi-calendar</v-icon>
                    {{ formatDate(event.date) }}
                  </div>
                  <div class="text-caption text-medium-emphasis">
                    <v-icon size="small" class="mr-1">mdi-account</v-icon>
                    {{ event.owner }}
                  </div>
                </div>
                <div class="action-buttons">
                  <v-btn
                    icon="mdi-pencil"
                    size="small"
                    variant="text"
                    color="primary"
                    @click.stop="editEvent(event)"
                  />
                  <v-btn
                    icon="mdi-delete"
                    size="small"
                    variant="text"
                    color="error"
                    @click.stop="openDeleteDialog(event)"
                  />
                </div>
              </div>
            </v-col>

            <!-- Desktop View -->
            <v-col cols="12" md="4" class="d-none d-md-block">
              <div class="d-flex align-center">
                <v-avatar class="mr-3 event-avatar" color="primary" size="40">
                  <v-icon color="white">mdi-calendar-month</v-icon>
                </v-avatar>
                <div>
                  <strong class="text-body-1">{{ event.title }}</strong>
                </div>
              </div>
            </v-col>

            <v-col cols="3" class="d-none d-md-block">
              <v-chip 
                size="small" 
                variant="tonal" 
                color="secondary"
                class="rounded-pill"
              >
                <v-icon start size="small">mdi-calendar</v-icon>
                {{ formatDate(event.date) }}
              </v-chip>
            </v-col>

            <v-col cols="3" class="d-none d-md-block">
              <div class="d-flex align-center">
                <v-avatar size="28" color="accent" class="mr-2">
                  <v-icon size="small" >mdi-account</v-icon>
                </v-avatar>
                <span class="text-body-2">{{ event.owner }}</span>
              </div>
            </v-col>

            <v-col cols="2" class="text-center d-none d-md-block">
              <div class="action-buttons">
                <v-btn
                  icon="mdi-pencil"
                  size="small"
                  variant="text"
                  color="primary"
                  class="mr-2"
                  @click.stop="editEvent(event)"
                />
                <v-btn
                  icon="mdi-delete"
                  size="small"
                  variant="text"
                  color="error"
                  @click.stop="openDeleteDialog(event)"
                />
              </div>
            </v-col>

          </v-row>
        </v-expansion-panel-title>

        <!-- EXPANDED -->
        <v-expansion-panel-text>
          <div class="inner-table-wrapper rounded-b-xl">

            <!-- ОПИСАНИЕ -->
            <div class="description-card rounded-lg pa-4 mb-4">
              <div class="d-flex align-center mb-2">
                <v-icon color="primary" class="mr-2">mdi-text-box-outline</v-icon>
                <strong>Описание</strong>
              </div>
              <p class="mb-0 text-body-2">
                {{ event.description || 'Нет описания' }}
              </p>
            </div>

            <!-- СОСТАВ -->
            <v-row dense class="mb-4">
              <v-col cols="12" md="6">
                <div class="team-card rounded-lg pa-3 h-100">
                  <div class="d-flex align-center mb-2">
                    <v-icon color="accent" class="mr-2">mdi-account-group</v-icon>
                    <strong>Организаторы</strong>
                  </div>
                  <div v-if="event.organizers?.length" class="d-flex flex-wrap gap-1">
                    <v-chip 
                      v-for="(org, index) in event.organizers" 
                      :key="index"
                      size="small" 
                      color="primary" 
                      variant="tonal"
                      class="mr-1 mb-1 rounded-pill"
                    >
                      {{ org }}
                    </v-chip>
                  </div>
                  <div v-else class="text-grey text-body-2">Не указаны</div>
                </div>
              </v-col>

              <v-col cols="12" md="6">
                <div class="team-card rounded-lg pa-3 h-100">
                  <div class="d-flex align-center mb-2">
                    <v-icon color="secondary" class="mr-2">mdi-hand-heart</v-icon>
                    <strong>Волонтёры</strong>
                  </div>
                  <div v-if="event.volunteers?.length" class="d-flex flex-wrap gap-1">
                    <v-chip 
                      v-for="(vol, index) in event.volunteers" 
                      :key="index"
                      size="small" 
                      color="secondary" 
                      variant="tonal"
                      class="mr-1 mb-1 rounded-pill"
                    >
                      {{ vol }}
                    </v-chip>
                  </div>
                  <div v-else class="text-grey text-body-2">Не указаны</div>
                </div>
              </v-col>
            </v-row>

            <v-divider class="mb-4" />

            <!-- КАНБАН -->
            <v-row>
              <v-col
                v-for="tab in event.tabs"
                :key="tab.id"
                cols="12"
                md="4"
                class="mb-4 mb-md-0"
              >
                <PanelComponent
                  :tab="tab"
                  @updateTitle="tab.form.title = $event"
                  @updateContent="tab.form.content = $event"
                  @updateImportance="tab.form.importance = $event"
                  @updateDeadline="tab.form.deadline = $event"
                  @updateResponsible="tab.form.responsible = $event"
                  @openTabCreate="tab.create = !tab.create"
                  @createNote="createNote(event, tab.id)"
                  @updateNote="updateNote(event, tab.id, $event)"
                  @requestEdit="startEdit(event, tab.id, $event)"
                  @deleteNote="deleteNote(event, tab.id, $event)"
                />
              </v-col>
            </v-row>

          </div>
        </v-expansion-panel-text>

      </v-expansion-panel>

    </v-expansion-panels>

    <!-- DIALOG -->
    <v-dialog v-model="dialog" width="600" max-width="95vw">
      <v-card class="rounded-2xl dialog-card">
        <v-card-title class="dialog-header d-flex align-center">
          <v-icon class="mr-3" color="white">mdi-calendar-plus</v-icon>
          <span class="text-h6 font-weight-bold">
            {{ editingId ? 'Редактировать мероприятие' : 'Создать мероприятие' }}
          </span>
        </v-card-title>

        <v-card-text class="pt-4">
          <v-row>
            <v-col cols="12">
              <v-text-field 
                v-model="form.title" 
                label="Название *" 
                variant="outlined"
                rounded="lg"
                hide-details
                class="mb-3"
              />
            </v-col>

            <v-col cols="12" md="6">
              <v-text-field 
                v-model="form.date" 
                type="date" 
                label="Дата" 
                variant="outlined"
                rounded="lg"
                hide-details
                class="mb-3"
              />
            </v-col>

            <v-col cols="12" md="6">
              <v-text-field 
                v-model="form.owner" 
                label="Главный организатор" 
                variant="outlined"
                rounded="lg"
                hide-details
                class="mb-3"
              />
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
              />
            </v-col>

            <v-col cols="12" md="6">
              <v-textarea
                v-model="form.organizersText"
                label="Организаторы (через запятую)"
                rows="2"
                variant="outlined"
                rounded="lg"
                hide-details
                class="mb-3"
              />
            </v-col>

            <v-col cols="12" md="6">
              <v-textarea
                v-model="form.volunteersText"
                label="Волонтёры (через запятую)"
                rows="2"
                variant="outlined"
                rounded="lg"
                hide-details
                class="mb-3"
              />
            </v-col>
          </v-row>
        </v-card-text>

        <v-card-actions class="pa-4">
          <v-spacer />
          <v-btn 
            variant="text" 
            @click="dialog = false"
            class="rounded-pill px-4"
          >
            Отмена
          </v-btn>
          <v-btn 
            color="primary" 
            @click="saveEvent"
            class="rounded-pill px-6 font-weight-bold"
            variant="flat"
          >
            Сохранить
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

  </v-container>

  <v-dialog v-model="deleteDialog" width="420" max-width="95vw">
    <v-card class="text-center pa-4 rounded-2xl delete-dialog">
      <div class="delete-icon-wrapper mb-3">
        <v-icon size="64" color="error" class="rounded-circle">mdi-delete</v-icon>
      </div>

      <v-card-title class="text-h6 font-weight-bold mb-2">
        Удаление мероприятия
      </v-card-title>

      <v-card-text class="text-body-1 mb-4">
        Вы уверены, что хотите удалить 
        <strong class="text-primary">{{ eventToDelete?.title }}</strong>?
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
          @click="confirmDelete"
          class="rounded-pill px-6"
        >
          Удалить
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
  
</template>

<script setup>
import { ref, computed } from 'vue'
import PanelComponent from '@/components/KanbanTable/PanelComponent.vue'

const events = ref([])
const search = ref('')
const dialog = ref(false)
const editingId = ref(null)

const deleteDialog = ref(false)
const eventToDelete = ref(null)

const openDeleteDialog = (event) => {
  eventToDelete.value = event
  deleteDialog.value = true
}

const confirmDelete = () => {
  if (!eventToDelete.value) return

  events.value = events.value.filter(
    e => e.id !== eventToDelete.value.id
  )

  deleteDialog.value = false
  eventToDelete.value = null
}

const form = ref({
  title: '',
  date: '',
  owner: '',
  description: '',
  organizersText: '',
  volunteersText: ''
})

// ===== UTILS =====
const parseList = (text) => {
  if (!text) return []
  return text
    .split(/[\n,]/)
    .map(i => i.trim())
    .filter(i => i.length)
}

const listToText = (arr) => {
  if (!arr) return ''
  return arr.join(', ')
}

// ===== КАНБАН =====
const defaultTabs = () => ([
  { id:0, name:'В планах', notes:[], create:false, form:{ title:'', content:'', importance:'red', editingId:null, deadline:'', responsible:'' }},
  { id:1, name:'В работе', notes:[], create:false, form:{ title:'', content:'', importance:'red', editingId:null, deadline:'', responsible:'' }},
  { id:2, name:'Сделано', notes:[], create:false, form:{ title:'', content:'', importance:'red', editingId:null, deadline:'', responsible:'' }}
])

// ===== CRUD =====
const openCreateDialog = () => {
  form.value = {
    title: '',
    date: '',
    owner: '',
    description: '',
    organizersText: '',
    volunteersText: ''
  }
  editingId.value = null
  dialog.value = true
}

const saveEvent = () => {
  if (!form.value.title) return

  const payload = {
    title: form.value.title,
    date: form.value.date,
    owner: form.value.owner,
    description: form.value.description,
    organizers: parseList(form.value.organizersText),
    volunteers: parseList(form.value.volunteersText)
  }

  if (editingId.value) {
    const e = events.value.find(e => e.id === editingId.value)
    Object.assign(e, payload)
  } else {
    events.value.push({
      id: Date.now(),
      ...payload,
      tabs: defaultTabs()
    })
  }

  dialog.value = false
}

const editEvent = (event) => {
  form.value = {
    title: event.title,
    date: event.date,
    owner: event.owner,
    description: event.description,
    organizersText: listToText(event.organizers),
    volunteersText: listToText(event.volunteers)
  }
  editingId.value = event.id
  dialog.value = true
}

const deleteEvent = (id) => {
  events.value = events.value.filter(e => e.id !== id)
}

// ===== FILTER =====
const filteredEvents = computed(() => {
  if (!search.value) return events.value
  const s = search.value.toLowerCase()
  return events.value.filter(e =>
    e.title.toLowerCase().includes(s) ||
    e.owner.toLowerCase().includes(s)
  )
})

// ===== KANBAN =====
const createNote = (event, tabId) => {
  const tab = event.tabs[tabId]
  if (!tab.form.title) return

  tab.notes.push({
    id: Date.now(),
    title: tab.form.title,
    content: tab.form.content,
    color: tab.form.importance,
    deadline: tab.form.deadline,
    responsible: tab.form.responsible,
    openContent: false
  })

  tab.form = { title:'', content:'', importance:'red', editingId:null, deadline:'', responsible:'' }
  tab.create = false
}

const deleteNote = (event, tabId, noteId) => {
  const tab = event.tabs[tabId]
  tab.notes = tab.notes.filter(n => n.id !== noteId)
}

const startEdit = (event, tabId, note) => {
  const tab = event.tabs[tabId]
  tab.form = {
    title: note.title,
    content: note.content,
    importance: note.color,
    deadline: note.deadline,
    responsible: note.responsible,
    editingId: note.id
  }
  tab.create = true
}

const updateNote = (event, tabId, payload) => {
  const tab = event.tabs[tabId]
  const note = tab.notes.find(n => n.id === payload.id)

  Object.assign(note, payload)

  tab.form = { title:'', content:'', importance:'red', editingId:null, deadline:'', responsible:'' }
  tab.create = false
}

const formatDate = (d) => {
  if (!d) return ''
  return new Date(d).toLocaleDateString('ru-RU')
}

// Вычисляемый класс для контейнера с градиентом
const containerClass = computed(() => ({
  'bg-gradient': true
}))
</script>

<style scoped lang="scss">
// Цвета брендбука
$primary: #2D32FF;
$secondary: #66B5F6;
$accent: #FF25B8;
$light-pink: #FF80D6;

.table-header { 
  padding: 0 4px;
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
  box-shadow: 0 4px 15px #2d30ff86 !important;
  transition: all 0.3s ease !important;
  
  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px #2d32ff66 !important;
  }
}

// Фон контейнера с легким градиентом
// .bg-gradient {
//   background: linear-gradient(180deg, #fafafa 0%, #f0f4ff 100%);
// }

// 3D обертка таблицы
.table-3d-wrapper {
  padding: 8px;
  background: white;
  border-radius: 20px;
  box-shadow: 0 10px 40px rgba(45, 50, 255, 0.1);
  border: 1px solid rgba(45, 50, 255, 0.05);
}

// Заголовок панели
.panel-title {
  background: white !important;
  border-radius: 16px !important;
  margin: 4px 0;
  transition: all 0.3s ease;
  border: 1px solid rgba(45, 50, 255, 0.08);
  
  &:hover {
    box-shadow: 0 4px 12px rgba(45, 50, 255, 0.1);
    transform: translateY(-1px);
  }
}

// Аватар события
.event-avatar {
  background: linear-gradient(135deg, $primary 0%, $secondary 100%);
}

// Внутренняя обертка
.inner-table-wrapper {
  padding: 20px;
  background: linear-gradient(180deg, #fafafa 0%, #ffffff 100%);
  border-radius: 0 0 16px 16px;
}

// Карточка описания
.description-card {
  background: linear-gradient(135deg, rgba(45, 50, 255, 0.05) 0%, rgba(255, 37, 184, 0.05) 100%);
  border: 1px solid rgba(45, 50, 255, 0.1);
}

// Карточка команды
.team-card {
  background: white;
  border: 1px solid rgba(102, 181, 246, 0.2);
  transition: all 0.3s ease;
  
  &:hover {
    box-shadow: 0 4px 12px rgba(102, 181, 246, 0.15);
  }
}

// Кнопки действий
.action-buttons {
  display: flex;
  gap: 4px;
  justify-content: flex-end;
  align-items: center;
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

// Диалог
.dialog-card {
  overflow: hidden;
}

.dialog-header {
  background: linear-gradient(135deg, $primary 0%, $secondary 100%);
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
.gap-1 {
  gap: 4px;
}

// Адаптивность
@media (max-width: 600px) {
  .table-3d-wrapper {
    padding: 4px;
  }
  
  .inner-table-wrapper {
    padding: 12px;
  }
  
  .panel-title {
    padding: 12px !important;
  }
}

// Анимации
.v-expansion-panel {
  transition: all 0.3s ease;
}
</style>