<template>
  <v-container fluid class="register-page d-flex align-center justify-center">
    <v-card class="register-card elevation-5 pa-10">
      <v-card-title class="titleform">Вход</v-card-title>

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
            class="mb-6"
            prepend-inner-icon="mdi-account-outline"
            :disabled="loading"
          />

          <v-text-field
            v-model="logindata.password"
            label="Пароль"
            type="password"
            variant="outlined"
            :rules="[rules.require, rules.passwordmin]"
            required
            prepend-inner-icon="mdi-lock-outline"
            :disabled="loading"
          />

          <v-btn
            class="reg__btn mb-4"
            block
            height="56"
            type="submit"
            :loading="loading"
            :disabled="!valid"
          >
            Войти
          </v-btn>
        </v-form>
      </v-card-text>

      <v-divider class="my-6" />

      <v-card-actions class="d-flex flex-column">
        <v-btn
          class="log__btn"
          block
          height="56"
          variant="text"
          @click="goToRegistration"
          :disabled="loading"
        >
          <!-- Ещё нет аккаунта? Регистрация -->
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts" setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

// 🔧 Базовый URL API
const API_BASE = 'http://localhost:8000'

const form = ref()
const valid = ref(false)
const loading = ref(false)
const successMessage = ref('')
const router = useRouter()

const logindata = reactive({
  username: '',
  password: '',
})

const serverErrors = reactive<{ main?: string }>({})

const rules = {
  require: (u: string) => !!u || 'Поле нужно заполнить',
  passwordmin: (u: string) =>
    u?.length >= 6 || 'Минимальная длина - 6 символов',
}

const submit = async () => {
  console.log('CLICK SUBMIT')

  // Сбрасываем ошибки и сообщения
  serverErrors.main = undefined
  successMessage.value = ''
  loading.value = true

  // Валидация формы
  const { valid: isValid } = await form.value?.validate()
  if (!isValid) {
    console.log('VALIDATION FAILED')
    loading.value = false
    return
  }

  try {
    console.log('SENDING REQUEST')

    // Формируем данные для OAuth2PasswordRequestForm
    const formData = new URLSearchParams()
    formData.append('username', logindata.username)
    formData.append('password', logindata.password)

    // ✅ Отправляем запрос на правильный эндпоинт
    const res = await axios.post(
      `${API_BASE}/user/login`,
      formData,
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      }
    )

    console.log('RESPONSE:', res.data)

    // ✅ Сохраняем токен в localStorage
    const token = res.data.access_token
    localStorage.setItem('token', token)
    localStorage.setItem('token_type', res.data.token_type)

    // ✅ Опционально: сохраняем время истечения токена
    localStorage.setItem('login_time', Date.now().toString())

    successMessage.value = 'Успешный вход! Перенаправление...'

    // 🔹 ВАЖНО: Сообщаем всем компонентам, что авторизация изменилась
    // Это обновит хедер и другие компоненты, слушающие это событие
    window.dispatchEvent(new Event('auth-updated'))

    // Небольшая задержка для показа сообщения
    setTimeout(() => {
      router.push('/')
    }, 500)

  } catch (err: any) {
    console.log('ERROR:', err)

    // Обработка ошибок
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

const goToRegistration = () => {
  router.push({ path: '/register' })
}
</script>

<style scoped lang="scss">
.register-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  padding: 24px;
  font-family: 'Montserrat', sans-serif;

  &::before {
    content: '';
    position: absolute;
    inset: 0;
    background: url('/images/mesh-gradient.svg') center/cover no-repeat;
    opacity: 0.15;
    pointer-events: none;
  }
}

.register-card {
  width: 100%;
  max-width: 520px;
  border-radius: 24px;
  backdrop-filter: blur(6px);
  background: rgba(255, 255, 255, 0.95);
}

.titleform {
  text-align: center;
  font-size: 32px;
  font-weight: 800;
  color: #0171bc;
  margin-bottom: 20px;
}

.v-input__control,
.v-input__slot {
  transition: background-color 0.25s ease;
}

.v-input--focused .v-input__slot {
  background-color: #e3f2fd !important;
}

.v-input__slot {
  background-color: #f5f8fb !important;
  border-radius: 12px !important;
  padding-left: 4px !important;
}

.reg__btn,
.log__btn {
  background: linear-gradient(135deg, #2D32FF 0%, #ff25b866 100%) !important;
  color: #fff !important;
  font-size: 18px;
  font-weight: 700;
  border-radius: 12px;
  transition:
    transform 0.2s ease,
    box-shadow 0.2s ease;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(1, 113, 188, 0.3);
  }

  &:disabled {
    opacity: 0.6;
    cursor: not-allowed;
    transform: none !important;
  }
}

.log__btn {
  background: transparent !important;
  color: #0171bc !important;
  font-size: 14px;
}
</style>