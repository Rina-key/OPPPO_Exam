<template>
  <v-container fluid class="register-page d-flex align-center justify-center">
    <v-card class="register-card elevation-5 pa-10">
      <v-card-title class="titleform">Регистрация</v-card-title>

      <v-card-text>
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-text-field
          
            label="Email"
            variant="outlined"
            type="email"
            :rules="[rules.require]"
            required
            class="mb-6"
            prepend-inner-icon="mdi-email-outline"
          />
          <v-text-field
            label="Пароль"
            type="password"
            
            variant="outlined"
            :rules="[rules.require, rules.passwordmin]"
            required
            class="mb-6"
            prepend-inner-icon="mdi-lock-outline"
          />
          <v-text-field
            label="Подтвердите пароль"
            type="password"
            
            variant="outlined"
           
            required
            prepend-inner-icon="mdi-lock-check-outline"
          />
        </v-form>
      </v-card-text>
      <v-divider class="my-6" />
      <v-card-actions class="d-flex flex-column">
        <v-btn class="reg__btn mb-4" block height="56" >Зарегистрироваться</v-btn>
        <v-btn class="log__btn" block height="56" variant="text" @click="login">
          Есть аккаунт? Войти
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts" setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
// import { isEmail } from 'validator'
// import { regdata } from '@/composables/auth.request'
// import type { FormData } from '@/types/auth.type'

const form = ref()
const valid = ref(false)
const router = useRouter()

// const formdata = reactive<FormData>({
//   email: '',
//   password: '',
//   password2: '',
// })

const rules = {
  require: (u: string) => !!u || 'Поле нужно заполнить',
  //email: (u: string) => isEmail(u) || 'Введен неправильный mail',
  passwordmin: (u: string) => u?.length >= 6 || 'Минимальная длина - 6 символов',
  //passsame: (u: string) => u === formdata.password || 'Пароли не совпадают',
}

// const submit = async () => {
//   if (!form.value?.validate()) return
//   try {
//     await regdata(formdata)
//     router.push({ path: '/entrance' })
//   } catch (err) {
//     console.error(err)
//   }
// }

const login = () => {
  router.push({ path: '/entrance' })
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

.subtitle {
  text-align: center;
  font-size: 16px;
  margin-bottom: 24px;
  color: #5e6e7c;
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
  background: linear-gradient(135deg, #0171bc 0%, #29b6f6 100%) !important;
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
}

.log__btn {
  background: transparent !important;
  color: #0171bc !important;
  font-size: 14px;
}
</style>
