<!-- components/DeleteDialog.vue -->
<template>
  <v-dialog v-model="dialog" max-width="400">
    <v-card>
      <v-card-title class="text-h6 text-white" style="background-color: #2D32FF;">
        <v-icon start icon="mdi-delete" /> Подтверждение
      </v-card-title>
      
      <v-card-text class="pt-4">
        Вы действительно хотите удалить активиста 
        <strong>"{{ itemName }}"</strong>?
      </v-card-text>
      
      <v-card-actions>
        <v-spacer />
        
        <v-btn 
          color="error" 
          text="Удалить" 
          variant="tonal" 
          @click="confirm"
        />
        <v-btn text="Отмена" variant="plain" @click="cancel" />
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue'

// 🔹 Сначала объявляем эмиты (ВАЖНО: до использования!)
const emit = defineEmits<{
  confirm: [item: any]
  cancel: []
}>()

const dialog = ref(false)
const itemName = ref('')
const itemData = ref<any>(null)

// 🔹 Метод открытия диалога
const open = (item: any) => {
  console.log('🔔 [DeleteDialog] open() вызван:', item) // 👈 Отладка
  itemData.value = item
  itemName.value = item?.name || 'эту запись'
  dialog.value = true
}

// 🔹 Отмена
const cancel = () => {
  dialog.value = false
  emit('cancel')
}

// 🔹 Подтверждение
const confirm = () => {
  console.log('✅ [DeleteDialog] confirm() вызван') // 👈 Отладка
  dialog.value = false
  emit('confirm', itemData.value)
}

// 🔹 Делаем open доступным извне
defineExpose({ open })
</script>