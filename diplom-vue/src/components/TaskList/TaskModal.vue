<template>
  <div v-if="isOpen" class="modal-overlay" @click.self="close">
    <div class="modal-content">
      <h2>{{ isEditing ? 'Редактировать задачу' : 'Новая задача' }}</h2>
      
      <div class="form-group">
        <label>Название:</label>
        <input v-model="form.title" type="text" placeholder="Введите название" />
      </div>

      <div class="form-group">
        <label>Дедлайн:</label>
        <input v-model="form.deadline" type="date" />
      </div>

      <div class="form-group">
        <label>Описание:</label>
        <textarea v-model="form.description" rows="4"></textarea>
      </div>

      <div class="modal-actions">
        <button class="btn btn-secondary" @click="close">Закрыть</button>
        <button class="btn btn-primary" @click="save">Сохранить</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, computed } from 'vue';

// Определяем интерфейс задачи
interface Task {
  id: number;
  title: string;
  deadline: string;
  description: string;
  isCompleted: boolean;
}

// Типизация пропсов
interface Props {
  isOpen: boolean;
  task: Task | null; // null если создаем новую
}

const props = withDefaults(defineProps<Props>(), {
  task: null
});

// Типизация событий (emits)
const emit = defineEmits<{
  (e: 'close'): void;
  (e: 'save', task: Omit<Task, 'id' | 'isCompleted'>): void; // При сохранении отправляем данные без ID и статуса
}>();

// Локальная форма
const form = ref({
  title: '',
  deadline: '',
  description: ''
});

// Проверяем, редактируем ли мы
const isEditing = computed(() => !!props.task);

// Следим за изменениями пропсов, чтобы заполнить форму при открытии
watch(() => props.task, (newTask) => {
  if (newTask) {
    form.value = {
      title: newTask.title,
      deadline: newTask.deadline,
      description: newTask.description
    };
  } else {
    // Сброс формы
    form.value = { title: '', deadline: '', description: '' };
  }
}, { immediate: true });

const close = () => {
  emit('close');
};

const save = () => {
  if (!form.value.title) return alert('Введите название задачи');
  
  emit('save', {
    title: form.value.title,
    deadline: form.value.deadline,
    description: form.value.description
  });
};
</script>

<style scoped>
/* Базовые стили для модального окна */
.modal-overlay {
  position: fixed; top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.5);
  display: flex; justify-content: center; align-items: center;
  z-index: 100;
}
.modal-content {
  background: white; padding: 20px; border-radius: 8px; width: 400px;
}
.form-group { margin-bottom: 15px; display: flex; flex-direction: column; }
.form-group label { margin-bottom: 5px; font-weight: bold; }
.form-group input, .form-group textarea { padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
.modal-actions { display: flex; justify-content: flex-end; gap: 10px; }
.btn { padding: 8px 16px; border: none; border-radius: 4px; cursor: pointer; }
.btn-primary { background: #42b983; color: white; }
.btn-secondary { background: #e0e0e0; }
</style>