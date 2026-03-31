<template>
  <div id="app">
    <!-- Таблица -->
    <TaskTable 
      :tasks="tasks" 
      @add="openModal" 
      @edit="openEditModal" 
      @delete="deleteTask" 
      @toggle="toggleTaskStatus" 
    />

    <!-- Модальное окно -->
    <TaskModal 
      :isOpen="isModalOpen" 
      :task="currentTask" 
      @close="closeModal" 
      @save="handleSave" 
    />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import TaskTable from '@/components/TaskList/TaskTable.vue';
import TaskModal from '@/components/TaskList/TaskModal.vue';
// Интерфейс задачи
interface Task {
  id: number;
  title: string;
  deadline: string;
  description: string;
  isCompleted: boolean;
}

// Состояние
const tasks = ref<Task[]>([
  { id: 1, title: 'Купить продукты', deadline: '2023-10-25', description: 'Молоко, хлеб', isCompleted: false },
  { id: 2, title: 'Сделать отчет', deadline: '2023-10-26', description: 'Отчет за квартал', isCompleted: true }
]);

const isModalOpen = ref(false);
const currentTask = ref<Task | null>(null);

// Методы
const openModal = () => {
  currentTask.value = null; // Новая задача
  isModalOpen.value = true;
};

const openEditModal = (task: Task) => {
  currentTask.value = { ...task }; // Копируем для редактирования
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
  currentTask.value = null;
};

const handleSave = (taskData: Omit<Task, 'id' | 'isCompleted'>) => {
  if (currentTask.value) {
    // Редактирование
    const index = tasks.value.findIndex(t => t.id === currentTask.value!.id);
    // if (index !== -1) {
    //   tasks.value[index] = { ...tasks.value[index], ...taskData };
    // }
  } else {
    // Создание
    const newTask: Task = {
      id: Date.now(), // Генерируем простой ID
      isCompleted: false,
      ...taskData
    };
    tasks.value.push(newTask);
  }
};

const deleteTask = (id: number) => {
  if(confirm('Удалить задачу?')) {
    tasks.value = tasks.value.filter(t => t.id !== id);
  }
};

const toggleTaskStatus = (task: Task) => {
  const index = tasks.value.findIndex(t => t.id === task.id);
//   if (index !== -1) {
//     tasks.value[index].isCompleted = !tasks.value[index].isCompleted;
//   }
};
</script>

<style>
#app { padding: 20px; background: #f5f5f5; min-height: 100vh; }
</style>