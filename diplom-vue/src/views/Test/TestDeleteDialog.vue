<template>
  <v-dialog v-model="isOpen" max-width="400">
    <v-card>
      <v-card-title class="text-h6">{{ dialogData.title || 'Подтверждение' }}</v-card-title>
      <v-card-text>{{ dialogData.text || 'Вы уверены?' }}</v-card-text>
      <v-card-actions>
        <v-spacer />
		<v-btn
          color="error"
          variant="tonal"
          @click="confirm"
        >
          {{ dialogData.confirmText || 'Удалить' }}
        </v-btn>
        <v-btn
          variant="text"
          @click="close"
        >
          {{ dialogData.cancelText || 'Отмена' }}
        </v-btn>
        
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const isOpen = ref(false)
const dialogData = ref<any>({})
const emit = defineEmits(['confirm'])

const open = (data: any) => {
  dialogData.value = data
  isOpen.value = true
}

const close = () => {
  isOpen.value = false
  dialogData.value = {}
}

const confirm = () => {
  emit('confirm')
  close()
}

defineExpose({ open })
</script>