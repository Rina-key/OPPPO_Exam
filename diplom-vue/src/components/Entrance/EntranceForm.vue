<template>
  <v-container fluid class="auth-page">
    <v-row no-gutters class="fill-height">
      
      <!-- ЛЕВАЯ КОЛОНКА: Приветствие -->
      <v-col cols="12" lg="6" md="6" class="d-flex align-center justify-center welcome-col ">
        <div class="welcome-content">
          
          <h1 class="welcome-title mb-4">
            Добро пожаловать<br />
            в <span class="highlight">ПРОЕКТ+</span>
          </h1>

          <p class="welcome-description mb-8">
            Единая платформа для организации мероприятий,<br />
            управления командами и развития студенческих инициатив.
          </p>

          
            <div class="features-list">
              <div class="feature-item mb-4">
                <div class="feature-icon bg-purple" >
                  <v-icon icon="mdi-calendar-check" color="white" size="24" />
                </div>
                <div class="feature-text">
                  <h3 class="feature-title">Мероприятия</h3>
                  <p class="feature-subtitle">Планируйте и проводите события</p>
                </div>
              </div>

              <div class="feature-item mb-4">
                <div class="feature-icon bg-blue">
                  <v-icon icon="mdi-account-group" color="white" size="24" />
                </div>
                <div class="feature-text">
                  <h3 class="feature-title">Команда</h3>
                  <p class="feature-subtitle">Работайте вместе над проектами</p>
                </div>
              </div>

              <div class="feature-item">
                <div class="feature-icon bg-indigo">
                  <v-icon icon="mdi-file-document-outline" color="white" size="24" />
                </div>
                <div class="feature-text">
                  <h3 class="feature-title">Справочный ресурс</h3>
                  <p class="feature-subtitle">Узнавайте всё в одном месте</p>
                </div>
              </div>
            </div>
         

        </div>
      </v-col>

      <!-- ПРАВАЯ КОЛОНКА: Форма входа -->
      <v-col cols="12" lg="6" md="6" class="d-flex align-center justify-center form-col">
        <v-card class="register-card elevation-6 pa-5">
          
          <!-- Логотип -->
          <div class="logo-container mb-6">
            <div class="logo-circle">
              <img src="/logo_pos_ikit_vektor.ico" alt="Logo" class="logo-icon" />
            </div>
          </div>

          <v-card-title class="titleform">Вход</v-card-title>
          
          <p class="subtitle text-center mb-8">
            Введите свои данные для входа в систему
          </p>

          <v-alert v-if="serverErrors.main" type="error" class="mb-4" closable>
            {{ serverErrors.main }}
          </v-alert>

          <v-alert v-if="successMessage" type="success" class="mb-4" closable>
            {{ successMessage }}
          </v-alert>

          <v-card-text>
            <v-form ref="form" v-model="valid" @submit.prevent="submit">
              <v-text-field
                v-model="logindata.username"
                label="Логин"
                variant="outlined"
                :rules="[rules.require]"
                required
                class="mb-4"
                prepend-inner-icon="mdi-account-outline"
                :disabled="loading"
                density="comfortable"
              />

              <v-text-field
                v-model="logindata.password"
                label="Пароль"
                
                variant="outlined"
                :rules="[rules.require, rules.passwordmin]"
                required
                prepend-inner-icon="mdi-lock-outline"
                :disabled="loading"
                density="comfortable"
                :append-inner-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append-inner="showPassword = !showPassword"
                :type="showPassword ? 'text' : 'password'"
              />

              <!-- Чекбокс и ссылка -->
              <div class="d-flex align-center justify-center mb-6">
              
                <v-btn
                  variant="text"
                  color="primary"
                  size="small"
                  class="text-none"
                  @click="forgotPassword"
                >
                  Забыли пароль?
                </v-btn>
              </div>

              <v-btn
                class="reg__btn mb-4"
                block
                height="48"
                type="submit"
                :loading="loading"
                :disabled="!valid"
              >
                Войти
              </v-btn>
            </v-form>
          </v-card-text>

          
          <v-divider class="my-6" color="white"/>
        </v-card>
      </v-col>

    </v-row>
  </v-container>
</template>

<script lang="ts" setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const API_BASE = 'http://localhost:8000'

const form = ref()
const valid = ref(false)
const loading = ref(false)
const successMessage = ref('')
const showPassword = ref(false)
const rememberMe = ref(false)
const router = useRouter()

const logindata = reactive({
  username: '',
  password: '',
})

const serverErrors = reactive<{ main?: string }>({})

const rules = {
  require: (u: string) => !!u || 'Поле нужно заполнить',
  passwordmin: (u: string) => u?.length >= 5 || 'Минимальная длина - 5 символов пппркеикпик',
}

const submit = async () => {
  serverErrors.main = undefined
  successMessage.value = ''
  loading.value = true

  const { valid: isValid } = await form.value?.validate()
  if (!isValid) {
    loading.value = false
    return
  }

  try {
    const formData = new URLSearchParams()
    formData.append('username', logindata.username)
    formData.append('password', logindata.password)

    const res = await axios.post(`${API_BASE}/user/login`, formData, {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    })

    const token = res.data.access_token
    localStorage.setItem('token', token)
    localStorage.setItem('token_type', res.data.token_type)

    if (!rememberMe.value) {
      localStorage.setItem('token_expiry', (Date.now() + 24 * 60 * 60 * 1000).toString())
    } else {
      localStorage.removeItem('token_expiry')
    }

    localStorage.setItem('login_time', Date.now().toString())
    successMessage.value = 'Успешный вход! Перенаправление...'
    window.dispatchEvent(new Event('auth-updated'))

    setTimeout(() => router.push('/'), 500)
  } catch (err: any) {
    if (err.response?.status === 404) {
      serverErrors.main = 'Пользователь не найден'
    } else if (err.response?.status === 401) {
      serverErrors.main = 'Неверный логин или пароль'
    } else if (err.response?.status === 500) {
      serverErrors.main = 'Ошибка сервера. Попробуйте позже'
    } else if (err.code === 'ERR_NETWORK') {
      serverErrors.main = 'Нет соединения с сервером'
    } else {
      serverErrors.main = err.response?.data?.detail || 'Ошибка входа'
    }
  } finally {
    loading.value = false
  }
}

const goToRegistration = () => router.push({ path: '/register' })
const forgotPassword = () => router.push({ path: '/forgot-password' })
</script>

<style scoped lang="scss">
/* ===== ОБЩИЕ СТИЛИ СТРАНИЦЫ ===== */
.auth-page {
  min-height: 100vh;
  width: 100vw;
  margin: 0;
  padding: 0;
  position: relative;
  font-family: 'Montserrat', sans-serif;

  &::before,
  &::after {
    content: '';
    position: absolute;
    border-radius: 50%;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.08) 0%, rgba(118, 75, 162, 0.08) 100%);
    pointer-events: none;
    z-index: 0;
  }

  &::before {
    width: 500px;
    height: 500px;
    top: -150px;
    left: -100px;
  }

  &::after {
    width: 400px;
    height: 400px;
    bottom: -100px;
    right: -50px;
  }
}

/* ===== ЛЕВАЯ КОЛОНКА: ПРИВЕТСТВИЕ ===== */
.welcome-col {
  padding: 60px 40px;
  position: relative;
}

.welcome-content {
  max-width: 520px;
}

.welcome-title {
  font-size: 40px;
  font-weight: 800;
  color: #1a1a1a;
  line-height: 1.2;
  margin-bottom: 24px;

  .highlight {
    background: linear-gradient(135deg, #2D32FF 0%, #66B5F6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
}

.welcome-description {
  font-size: 15px;
  color: #6b7280;
  line-height: 1.6;
}

.features-card {
  padding: 24px;
  border-radius: 20px;

  background: rgba(255, 255, 255, 0.166);
  backdrop-filter: blur(12px);

  border: 1px solid rgba(255, 255, 255, 0.4);

  clip-path: polygon(
    0 0,
    calc(100% - 20px) 0,
    100% 20px,
    100% 100%,
    0 100%
  );

  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
}

.features-list {
  margin-top: 48px;
}

.feature-item {
  display: flex;
  align-items: center; 
  gap: 16px;
  padding: 12px 16px; 
  border-radius: 16px; 
  background: rgba(255, 255, 255, 0.503); 
  backdrop-filter: blur(8px); 
  border: 1px solid rgba(255, 255, 255, 0.4); 
  transition: transform 0.2s ease, background 0.2s ease, box-shadow 0.2s ease;

  &:hover {
    transform: translateX(8px);
    background: rgba(255, 255, 255, 0.85);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
  }
}

.feature-icon {
  width: 56px;
  height: 56px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  background: #FF25B8;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);

  &.bg-purple {
    background: linear-gradient(135deg, #FF25B8 0%, rgba(137, 47, 179, 0.853) 100%);
  }
  &.bg-blue {
    background: linear-gradient(135deg, #66B5F6 0%, rgba(79, 172, 254, 0.05) 100%);
  }
  &.bg-indigo {
    background: linear-gradient(135deg, #2D32FF 0%, #764ba26e 100%);
  }
}

.feature-text {
  flex: 1;
  min-width: 0; 
}

.feature-title {
  font-size: 16px;
  font-weight: 700;
  color: #1a1a1a;
  margin: 0 0 4px 0;
  line-height: 1.3;
}

.feature-subtitle {
  font-size: 14px;
  color: #6b7280;
  margin: 0;
  line-height: 1.4;
}

/* ===== ПРАВАЯ КОЛОНКА: ФОРМА ===== */
.form-col {
  padding: 40px;
  position: relative;
  z-index: 1;
  display: flex;
  align-items: flex-start; 
  justify-content: center;
  // padding-top: 100px; 
}

.register-card {
  width: 100%;
  max-width: 530px;
  margin-top: 40px;
  border-radius: 24px;
  backdrop-filter: blur(12px);
  background: rgba(255, 255, 255, 0.92); /* 👈 Чуть более прозрачный фон */
  border: 1px solid rgba(255, 255, 255, 0.6); /* 👈 Лёгкая обводка */
  position: relative;
  z-index: 1;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08); /* 👈 Мягкая тень */
}

/* Логотип */
.logo-container {
  display: flex;
  justify-content: center;
}

.logo-circle {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: linear-gradient(135deg, #66B5F6 0%, #2D32FF 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);
}

.logo-icon {
  width: 40px;
  height: 40px;
  object-fit: contain;
}

.titleform {
  text-align: center;
  font-size: 28px;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 8px;
  padding: 0;
}

.subtitle {
  font-size: 14px;
  color: #6b7280;
  margin-top: 0;
}

/* Поля формы */
.v-input__slot {
  background-color: #f9fafb !important;
  border-radius: 12px !important;
  padding-left: 4px !important;
  border: 1px solid #e5e7eb !important;
  transition: background-color 0.25s ease, border-color 0.25s ease;

  &:focus-within {
    background-color: #f0f9ff !important;
    border-color: #667eea !important;
  }
}

.remember-checkbox {
  :deep(.v-label) {
    font-size: 14px;
    color: #4b5563;
  }
}

/* Кнопка входа */
.reg__btn {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
  color: #fff !important;
  font-size: 16px;
  font-weight: 600;
  border-radius: 12px;
  transition: transform 0.2s ease, box-shadow 0.2s ease;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
  }

  &:disabled {
    opacity: 0.6;
    cursor: not-allowed;
    transform: none !important;
  }
}

/* Разделитель */
.divider-container {
  display: flex;
  align-items: center;
  gap: 16px;
  color: #9ca3af;
  font-size: 14px;

  :deep(.v-divider) {
    border-color: #e5e7eb;
    flex: 1;
  }

  .divider-text {
    white-space: nowrap;
    color: #6b7280;
    font-size: 13px;
  }
}

.social-btn {
  width: 56px;
  height: 56px;
  border-radius: 12px !important;
  border: 1px solid #e5e7eb !important;
  color: #4b5563 !important;
  transition: all 0.2s ease;

  &:hover {
    border-color: #667eea !important;
    color: #667eea !important;
    background-color: #f0f9ff !important;
    transform: translateY(-2px);
  }

  :deep(.v-icon) {
    font-size: 24px;
  }
}

.agreement-text {
  font-size: 12px;
  color: #6b7280;
  line-height: 1.6;
  margin-bottom: 0;

  .link {
    color: #667eea;
    text-decoration: none;
    font-weight: 500;

    &:hover {
      text-decoration: underline;
    }
  }
}

.log__btn {
  background: transparent !important;
  color: #667eea !important;
  font-size: 14px;
  font-weight: 500;
  text-transform: none;
  
  &:hover {
    background: rgba(102, 126, 234, 0.04) !important;
  }
}

/* ===== АДАПТИВНОСТЬ ===== */
@media (max-width: 1200px) {
  
  
  .welcome-title {
    font-size: 40px;
  }
  .welcome-description {
    font-size: 16px;
  }
}
@media (max-width: 960px) {
  .welcome-col {
    display: none;
  }
  
  .form-col {
    width: 100%;
    padding: 32px 24px;
  }
  
  .register-card {
    max-width: 100%;
  }
}

@media (max-width: 600px) {
  .auth-page::before,
  .auth-page::after {
    display: none;
  }
  
  .welcome-title {
    font-size: 32px;
  }
  
  .feature-item {
    gap: 12px;
  }
  
  .feature-icon {
    width: 48px;
    height: 48px;
  }
  
  .logo-circle {
    width: 64px;
    height: 64px;
  }
  
  .logo-icon {
    width: 32px;
    height: 32px;
  }
  
  .social-btn {
    width: 48px;
    height: 48px;
  }
}
</style>