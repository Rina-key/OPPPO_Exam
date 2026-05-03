<template>
  <v-container fluid class="settings-page pa-6">
    <h1 class="mb-6 highlight">Настройки аккаунта</h1>

    <v-row>
      <!-- ===== ЛЕВАЯ КОЛОНКА: АВАТАР И ПАРОЛЬ ===== -->
      <v-col cols="12" md="4" class="d-flex flex-column ga-4">
        
        <!-- Карточка с аватаром -->
        <v-card class="pa-5 settings-card">
          <div class="avatar-section mb-4">
            <div class="avatar-wrapper" @click="triggerFile">
              <v-avatar size="120" class="avatar-container">
                <img :src="avatarPreview || defaultAvatar" class="avatar-image" />
              </v-avatar>
              <div class="avatar-overlay">
                <v-icon color="white">mdi-camera</v-icon>
              </div>
            </div>

            <input
              ref="fileInput"
              type="file"
              accept="image/*"
              hidden
              @change="onFileChange"
            />

            <v-btn variant="text" size="small" class="mt-3" @click="triggerFile">
              Изменить фото
            </v-btn>

            <v-list-item-title class="mt-2 font-weight-bold">Арина</v-list-item-title>
            <v-chip size="small" color="primary" class="mt-1">Председатель</v-chip>
          </div>
        </v-card>

        <!-- Карточка со сменой пароля -->
        <v-card class="pa-5 settings-card flex-grow-1">
          <h2 class="text-h6 mb-4">Смена пароля</h2>

          <v-form ref="passwordForm" v-model="validPassword">
            <v-text-field
              v-model="password.old"
              label="Текущий пароль"
              type="password"
              variant="outlined"
              density="comfortable"
            />

            <v-text-field
              v-model="password.new"
              label="Новый пароль"
              type="password"
              variant="outlined"
              density="comfortable"
            />

            <v-text-field
              v-model="password.repeat"
              label="Повторите пароль"
              type="password"
              variant="outlined"
              density="comfortable"
            />

            <v-btn
              class="mt-2 save-btn"
              block
              :disabled="!validPassword || loadingPassword"
              :loading="loadingPassword"
              @click="changePassword"
            >
              Обновить пароль
            </v-btn>
          </v-form>
        </v-card>
      
      </v-col>

      <!-- ===== ПРАВАЯ КОЛОНКА: НАСТРОЙКИ ПРОФИЛЯ ===== -->
      <v-col cols="12" md="8">
        <v-card class="pa-6 settings-card">
          <h2 class="text-h6 mb-4">Основные данные</h2>

          <v-form ref="profileForm" v-model="validProfile">
            <v-text-field 
              v-model="form.username" 
              label="Логин" 
              variant="outlined"
              density="comfortable"
            />
            
            <v-text-field 
              v-model="form.fullname" 
              label="ФИО" 
              variant="outlined"
              density="comfortable"
            />
            
            <v-text-field 
              v-model="form.group" 
              label="Группа" 
              variant="outlined"
              density="comfortable"
            />

            <v-row>
              <v-col cols="12" md="6">
                <v-text-field 
                  v-model="form.phone" 
                  label="Телефон" 
                  variant="outlined"
                  density="comfortable"
                />
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field 
                  v-model="form.email" 
                  label="Email" 
                  variant="outlined"
                  density="comfortable"
                />
              </v-col>
            </v-row>

            <v-text-field
              v-model="form.birthdate"
              label="Дата рождения"
              type="date"
              variant="outlined"
              density="comfortable"
            />

            <v-select
              v-model="form.education"
              :items="['Бюджетная', 'Платная']"
              label="Форма обучения"
              variant="outlined"
              density="comfortable"
            />

            <v-row>
              <v-col cols="12" md="6">
                <v-text-field 
                  v-model="form.vk" 
                  label="VK" 
                  variant="outlined"
                  density="comfortable"
                />
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field 
                  v-model="form.tg" 
                  label="Telegram" 
                  variant="outlined"
                  density="comfortable"
                />
              </v-col>
            </v-row>

            <v-btn
              class="mt-4 save-btn"
              :disabled="!validProfile || loading"
              :loading="loading"
              @click="saveProfile"
            >
              Сохранить изменения
            </v-btn>
          </v-form>
        </v-card>
      </v-col>
    </v-row>

    <!-- Уведомления -->
    <v-snackbar v-model="snackbar.show" :color="snackbar.color">
      {{ snackbar.text }}
    </v-snackbar>
  </v-container>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import axios from 'axios'

const API_BASE = 'http://localhost:8000'

/* ===== FORMS ===== */
const profileForm = ref()
const passwordForm = ref()

const validProfile = ref(false)
const validPassword = ref(false)

/* ===== STATE ===== */
const loading = ref(false)
const loadingPassword = ref(false)

const snackbar = reactive({
  show: false,
  text: '',
  color: 'success'
})

/* ===== PROFILE ===== */
const form = reactive({
  username: '',
  fullname: '',
  group: '',
  phone: '',
  email: '',
  birthdate: '',
  education: '',
  vk: '',
  tg: '',
})

/* ===== AVATAR ===== */
const fileInput = ref<HTMLInputElement | null>(null)
const avatarFile = ref<File | null>(null)
const avatarPreview = ref<string | null>(null)
const defaultAvatar = '/default-avatar.png'

const triggerFile = () => {
  fileInput.value?.click()
}

const onFileChange = (e: Event) => {
  const target = e.target as HTMLInputElement
  const file = target.files?.[0]

  if (!file) return

  if (!file.type.startsWith('image/')) {
    showSnackbar('Только изображения', 'error')
    return
  }

  if (file.size > 2 * 1024 * 1024) {
    showSnackbar('Максимум 2MB', 'error')
    return
  }

  avatarFile.value = file
  avatarPreview.value = URL.createObjectURL(file)
}

/* ===== PASSWORD ===== */
const password = reactive({
  old: '',
  new: '',
  repeat: '',
})

/* ===== ACTIONS ===== */
const showSnackbar = (text: string, color = 'success') => {
  snackbar.text = text
  snackbar.color = color
  snackbar.show = true
}

const saveProfile = async () => {
  loading.value = true

  try {
    const formData = new FormData()

    Object.entries(form).forEach(([key, value]) => {
      formData.append(key, value as string)
    })

    if (avatarFile.value) {
      formData.append('avatar', avatarFile.value)
    }

    await axios.put(`${API_BASE}/user/profile`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    })

    showSnackbar('Профиль обновлён')

  } catch (e) {
    showSnackbar('Ошибка сохранения', 'error')
  } finally {
    loading.value = false
  }
}

const changePassword = async () => {
  if (password.new !== password.repeat) {
    showSnackbar('Пароли не совпадают', 'error')
    return
  }

  loadingPassword.value = true

  try {
    await axios.post(`${API_BASE}/user/change-password`, password)
    showSnackbar('Пароль обновлён')

    password.old = ''
    password.new = ''
    password.repeat = ''

  } catch (e) {
    showSnackbar('Ошибка смены пароля', 'error')
  } finally {
    loadingPassword.value = false
  }
}
</script>

<style scoped lang="scss">
.settings-page::before {
  content: '';
  position: fixed;
  inset: 0;
  background: url('/FonEntrence.jpeg') center/cover no-repeat;
  filter: blur(8px);
  transform: scale(1.05);
  z-index: -2;
}

.settings-card {
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
}

/* ===== AVATAR ===== */
.avatar-section {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.avatar-wrapper {
  position: relative;
  cursor: pointer;

  &:hover .avatar-overlay {
    opacity: 1;
  }
}

.avatar-container {
  overflow: hidden;
  background: #f5f5f5;
}

.avatar-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center top; /* Показывает лицо, а не макушку */
}

.avatar-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: 0.2s;
}

/* ===== BUTTON ===== */
.save-btn {
  background: linear-gradient(135deg, #2D32FF, #66B5F6);
  color: white;
  font-weight: 600;
}

.highlight {
    background: linear-gradient(135deg, #2D32FF 0%, #66B5F6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

</style>