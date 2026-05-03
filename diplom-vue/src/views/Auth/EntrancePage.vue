<template>
  <div class="entrance-wrapper d-flex align-center justify-center">
    <!-- v-main оставлен для совместимости с макетом, но его отступы обнулены -->
    <v-main class="entrance-main d-flex align-center justify-center">
      <EntranceForm />
    </v-main>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import EntranceForm from '@/components/Entrance/EntranceForm.vue'

export default defineComponent({
  name: 'EntrancePage',
  components: {
    EntranceForm,
  },
})
</script>

<style scoped>
.entrance-wrapper {
  background-image: url('/FonEntrence.jpeg');
  background-size: cover;       /* Растягивает фон на весь экран без зазоров */
  background-position: center;  /* Центрирует изображение */
  background-repeat: no-repeat;
  width: 100vw;                 /* Ширина = ширине окна */
  min-height: 100vh;            /* Минимальная высота = высоте окна */
  margin: 0 !important;
  padding: 0 !important;
  box-sizing: border-box;
}

.entrance-main {
  padding: 0 !important;
}
</style>