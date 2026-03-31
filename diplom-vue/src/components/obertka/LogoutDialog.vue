<template>
  <v-dialog v-model="isOpen" max-width="400">
    <v-card>
      <v-card-title>Подтверждение выхода</v-card-title>
      <v-card-text>
        Вы уверены, что хотите выйти из системы?
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" variant="text" @click="onCancel">
          Отмена
        </v-btn>
        <v-btn color="red" variant="text" @click="onConfirm">
          Выйти
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
  modelValue: {
    type: Boolean,
    required: true,
  },
})

const emit = defineEmits(['update:modelValue', 'confirm'])

const isOpen = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value),
})

const onCancel = () => {
  isOpen.value = false
}

const onConfirm = () => {
  isOpen.value = false
  emit('confirm')
}
</script>
