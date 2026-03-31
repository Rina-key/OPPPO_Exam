<template>
  <div class="task-list-container">
    <!-- Шапка -->
    <div class="header">
      <h1>Мои задачи</h1>
      <button class="btn-add" @click="$emit('add')">Добавить задачу</button>
    </div>

    <table class="table">
      <thead>
        <tr>
          <th style="width: 50px;">✔</th>
          <th>Дедлайн</th>
          <th>Название</th>
          <th style="width: 100px;">Действия</th>
        </tr>
      </thead>
      <tbody>
        <!-- Блок 1: В процессе (Сделать) -->
        <template v-if="activeTasks.length > 0">
          <tr v-for="task in activeTasks" :key="task.id" class="task-row">
            <td>
              <input type="checkbox" @change="toggleStatus(task)" />
            </td>
            <td>{{ task.deadline || '—' }}</td>
            <td>
              <div class="task-title">{{ task.title }}</div>
              <div class="task-desc">{{ task.description }}</div>
            </td>
            <td class="actions">
              <button class="icon-btn" @click="$emit('edit', task)">✏️</button>
              <button class="icon-btn delete" @click="$emit('delete', task.id)">🗑️</button>
            </td>
          </tr>
        </template>
        <tr v-else>
          <td colspan="4" class="empty-state">Нет активных задач</td>
        </tr>

        <!-- Разделитель -->
        <tr v-if="completedTasks.length > 0" class="separator">
          <td colspan="4"><strong>Готовые задачи</strong></td>
        </tr>

        <!-- Блок 2: Готовые -->
        <template v-if="completedTasks.length > 0">
          <tr v-for="task in completedTasks" :key="task.id" class="task-row completed">
            <td>
              <input type="checkbox" :checked="true" @change="toggleStatus(task)" />
            </td>
            <td>{{ task.deadline || '—' }}</td>
            <td>
              <div class="task-title">{{ task.title }}</div>
              <div class="task-desc">{{ task.description }}</div>
            </td>
            <td class="actions">
              <button class="icon-btn" @click="$emit('edit', task)">✏️</button>
              <button class="icon-btn delete" @click="$emit('delete', task.id)">🗑️</button>
            </td>
          </tr>
        </template>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';

interface Task {
  id: number;
  title: string;
  deadline: string;
  description: string;
  isCompleted: boolean;
}

// Пропсы
const props = defineProps<{
  tasks: Task[]
}>();

// Эмиты
const emit = defineEmits<{
  (e: 'add'): void;
  (e: 'edit', task: Task): void;
  (e: 'delete', id: number): void;
  (e: 'toggle', task: Task): void;
}>();

// Разделяем задачи на активные и завершенные
const activeTasks = computed(() => props.tasks.filter((t: Task) => !t.isCompleted));
const completedTasks = computed(() => props.tasks.filter((t: Task) => t.isCompleted));

const toggleStatus = (task: Task) => {
  emit('toggle', task);
};
</script>

<style scoped>
.task-list-container { max-width: 800px; margin: 0 auto; font-family: sans-serif; }
.header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
.btn-add { background: #42b983; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-size: 14px; }

.table { width: 100%; border-collapse: collapse; background: white; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
th, td { padding: 12px; text-align: left; border-bottom: 1px solid #eee; }
th { background: #f9f9f9; font-weight: 600; }

.task-row.completed .task-title { text-decoration: line-through; color: #888; }
.task-row.completed .task-desc { text-decoration: line-through; color: #aaa; }

.task-title { font-weight: bold; }
.task-desc { font-size: 0.85em; color: #666; margin-top: 4px; }

.actions { display: flex; gap: 8px; }
.icon-btn { background: none; border: none; cursor: pointer; font-size: 16px; padding: 4px; }
.icon-btn.delete:hover { color: red; }

.separator td { background: #f0f0f0; font-size: 0.9em; color: #555; }
.empty-state { text-align: center; color: #999; padding: 20px; }
</style>