<template>
  <v-main class="fill-height d-flex align-center justify-center">
    <RegistrationForm />
  </v-main>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import RegistrationForm from '@/components/Entrance/RegisterForm.vue'

export default defineComponent({
  name: 'RegisterPage',
  components: { RegistrationForm },
})
</script>

<style scoped></style>
