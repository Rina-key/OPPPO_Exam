<template>
  <v-expand-transition>
    <div v-if="tab.create">
      <v-form class="pa-2 inner-shadow" @submit.prevent="$emit('createNote', tab.id)">
        
        <!-- Тема -->
        <v-text-field 
          v-model="formTitleModel" 
          label="Тема" 
          required
          variant="outlined"
          density="comfortable"
          class="mb-3"
          hide-details="auto"
        />
        
        <!-- Описание -->
        <v-textarea 
          v-model="formContentModel" 
          label="Описание задачи" 
          required
          variant="outlined"
          density="comfortable"
          class="mb-3"
          hide-details="auto"
          rows="3"
        />
        
        <!-- Дедлайн -->
        <v-text-field
          v-model="formDeadlineModel"
          label="Дедлайн"
          type="date"
          variant="outlined"
          density="comfortable"
          class="mb-3"
          hide-details="auto"
          :min="today"
        />
        
        <!-- Ответственный -->
        <v-text-field
          v-model="formResponsibleModel"
          label="Ответственный"
          placeholder="Кто выполняет?"
          variant="outlined"
          density="comfortable"
          class="mb-4"
          hide-details="auto"
          prepend-inner-icon="mdi-account-outline"
        />
        
        <!-- Важность -->
        <v-radio-group 
          v-model="formImportanceModel" 
          inline
          class="mb-4"
        >
          <v-radio label="Важное" value="red" color="red"></v-radio>
          <v-radio label="Текущее" value="orange-darken-2" color="orange-darken-2"></v-radio>
          <v-radio label="Стороннее" value="green" color="green"></v-radio>
          <v-radio label="Другое" value="blue" color="blue"></v-radio>
        </v-radio-group>
        
        <!-- Кнопка -->
        <v-btn 
          variant="outlined" 
          block 
          class="save-btn"
          @click.prevent="onSubmit"
        >
          {{ props.tab.form.editingId ? 'Сохранить' : 'Добавить' }}
        </v-btn>
        
      </v-form>
    </div>
  </v-expand-transition>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
  tab: {
    type: Object,
    required: true
  }
})

const emit = defineEmits([
  'createNote', 
  'updateNote', 
  'updateTitle', 
  'updateContent', 
  'updateImportance',
  'updateDeadline',
  'updateResponsible'
])

const today = new Date().toISOString().substr(0, 10)

const formTitleModel = computed({
  get() {
    return props.tab.form.title
  },
  set(newValue) {
    emit('updateTitle', newValue)
  }
})

const formContentModel = computed({
  get() {
    return props.tab.form.content
  },
  set(newValue) {
    emit('updateContent', newValue)
  }
})

const formImportanceModel = computed({
  get() {
    return props.tab.form.importance
  },
  set(newValue) {
    emit('updateImportance', newValue)
  }
})

const formDeadlineModel = computed({
  get() {
    return props.tab.form.deadline || ''
  },
  set(newValue) {
    emit('updateDeadline', newValue)
  }
})

const formResponsibleModel = computed({
  get() {
    return props.tab.form.responsible || ''
  },
  set(newValue) {
    emit('updateResponsible', newValue)
  }
})

const onSubmit = () => {
  const editingId = props.tab.form.editingId
  if (editingId) {
    emit('updateNote', {
      id: editingId,
      title: props.tab.form.title,
      content: props.tab.form.content,
      importance: props.tab.form.importance,
      deadline: props.tab.form.deadline,
      responsible: props.tab.form.responsible
    })
  } else {
    emit('createNote', props.tab.id)
  }
}
</script>

<style scoped lang="scss">
.save-btn {
  background: linear-gradient(135deg, #2D32FF, #66B5F6);
  color: white;
  font-weight: 600;
  text-transform: none;
  border: none !important;
  
  &:hover {
    box-shadow: 0 4px 12px rgba(45, 50, 255, 0.3);
  }
}

:deep(.v-radio-group) {
  margin: 0;
}

:deep(.v-radio) {
  margin-right: 12px;
}

@media (max-width: 600px) {
  :deep(.v-radio-group) {
    flex-direction: column;
    align-items: flex-start;
  }
  
  :deep(.v-radio) {
    margin: 4px 0;
  }
}
</style>