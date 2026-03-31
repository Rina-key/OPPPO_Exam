<template>
  <v-dialog v-model="dialog" max-width="650" persistent>
    <v-card title="Добавление активиста" prepend-icon="mdi-account-plus">
      <v-card-text>
        <v-form ref="formRef" v-model="isValid">
          <v-row dense>
            <v-col cols="12" md="6">
              <v-text-field v-model="form.username" label="Логин*" :rules="[v => !!v || 'Обязательно']" />
            </v-col>
            <v-col cols="12" md="6">
              <v-text-field v-model="form.password" label="Пароль*" type="password" :rules="[v => !!v || 'Обязательно']" />
            </v-col>
            <v-col cols="12">
              <v-text-field v-model="form.name" label="ФИО" />
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="form.group" label="Группа" />
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="form.phone" label="Телефон" mask="+7 (###) ###-##-##" />
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="form.email" label="Email" type="email" :rules="[v => !v || /.+@.+\..+/.test(v) || 'Некорректный email']" />
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="form.birth" label="Дата рождения" type="date" />
            </v-col>
            <v-col cols="12" md="4">
              <v-select v-model="form.education" label="Форма обучения" :items="['Очная', 'Заочная', 'Очно-заочная']" />
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="form.vk" label="ВКонтакте" placeholder="https://vk.com/id..." />
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field v-model="form.tg" label="Telegram" placeholder="https://t.me/..." />
            </v-col>
          </v-row>
        </v-form>
        <small class="text-caption">* — обязательные поля</small>
      </v-card-text>
      <v-divider />
      <v-card-actions>
        <v-spacer />
        <v-btn text="Отмена" variant="plain" :disabled="loading" @click="cancel" />
        <v-btn color="primary" text="Сохранить" variant="tonal" :loading="loading" @click="save" />
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const emit = defineEmits<{
  confirm: [item: any]
  cancel: []
}>()

const dialog = ref(false)
const loading = ref(false)
const isValid = ref(false)
const formRef = ref<any>(null)

const form = ref({
  username: '',
  password: '',
  name: '',
  group: '',
  phone: '',
  email: '',
  birth: '',
  education: '',
  vk: '',
  tg: ''
})

const open = (item?: any) => {
  // Сброс формы
  form.value = {
    username: '', password: '', name: '', group: '', phone: '',
    email: '', birth: '', education: '', vk: '', tg: ''
  }
  dialog.value = true
}

const cancel = () => {
  dialog.value = false
  emit('cancel')
}

const save = async () => {
  const { valid } = await formRef.value?.validate() || { valid: false }
  if (!valid) return

  loading.value = true
  try {
    // Отправляем данные родителю, который сделает запрос к API
    emit('confirm', { ...form.value })
    dialog.value = false
  } finally {
    loading.value = false
  }
}

defineExpose({ open })
</script>