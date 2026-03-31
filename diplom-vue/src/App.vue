<template>
  <v-app :class="{ 'app-home': route.path === '/' }">
    <div class="global-background"></div>
    <Header />
    <v-main class="main" >
      <RouterView />
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import { defineComponent } from 'vue'
import { useRoute } from 'vue-router'

import Header from '@/components/obertka/Header.vue'

const route = useRoute()
</script>
<style>
/* Глобальный фон на весь сайт */
.main {
  padding: 0;
  position: relative;
   /* Размещаем основной контент поверх фона */
}

.global-background {
  position: fixed; 
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
  to left,
  transparent 0%,
  rgba(45, 50, 255, 0.4) 20%,
  rgba(102, 181, 246, 0.4) 40%,
  rgba(255, 37, 184, 0.4) 70%,
  rgba(255, 128, 214, 0.4) 60%,
  transparent 100%);
filter: blur(100px);
  z-index: 0;/*///////////*/
  pointer-events: none;
}

/* Убираем стандартный фон Vuetify */
.v-application {
  background: transparent !important;
}

/* Убираем внутренний отступ v-main только на главной */
.app-home .v-main__wrap {
  padding-top: 0 !important;
}

.app-home .v-main {
  padding-top: 0 !important;
  margin-top: 0 !important;
}




</style>