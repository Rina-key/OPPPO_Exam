<template>
  <v-app :class="{ 'app-home': route.path === '/' }">
    <div class="global-background"></div>
    <Header />
    <v-main class="main">
      <RouterView />
    </v-main>
    <Footer />
  </v-app>
</template>

<script setup lang="ts">
import { defineComponent } from 'vue'
import { useRoute } from 'vue-router'

import Header from '@/components/obertka/Header.vue'
import Footer from './components/obertka/Footer.vue';

const route = useRoute()
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap');

/* Глобальный фон на весь сайт */
.main {
  padding: 0;
  position: relative;
  min-height: 100vh; /* Гарантируем минимальную высоту viewport */
  font-family: 'Montserrat', sans-serif;
}

.global-background {
  position: fixed; 
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('/Fon.jpeg');
  background-size: cover; /* Картинка покрывает весь экран */
  background-position: center center; /* Центрируем изображение */
  background-repeat: no-repeat;
  background-attachment: fixed; /* Фиксируем фон при прокрутке */
  z-index: 0;
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

/* Гарантируем, что контент всегда выше фона */
.v-main {
  position: relative;
  z-index: 1;
}
</style>