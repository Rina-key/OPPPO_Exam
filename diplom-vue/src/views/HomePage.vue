<template>
  <v-main>
     <v-img 
      :src="oblozhka" 
      cover
      height="heights"
    />
    
      <RunLine />
      <FirstPart />

    <v-divider :thickness="3" class="border-opacity-50" color="primary"></v-divider>

      <SecondPart />
   
    <v-divider :thickness="3" class="border-opacity-50" color="primary"></v-divider>

      <ThirdPart />

    <v-divider :thickness="3" class="border-opacity-50" color="primary"></v-divider>

      <FourPart />

    <v-divider :thickness="3" class="border-opacity-50" color="primary"></v-divider>

      <FivePart />

    <v-divider :thickness="3" class="border-opacity-50" color="primary"></v-divider>

    <PravoTest />
  </v-main>
</template>

<script setup lang="ts">
import { reactive } from 'vue'

import { useDisplay } from 'vuetify'
import  FirstPart from '@/components/Home/FirstPart.vue'
import  RunLine from '@/components/Home/RunLine.vue'
import  SecondPart from '@/components/Home/SecondPart.vue'
import  ThirdPart from '@/components/Home/ThirdPart.vue'
import  FourPart from '@/components/Home/FourPart.vue'
import  FivePart from '@/components/Home/FivePart.vue'
import PravoTest from '@/components/PravoTest/PravoTest.vue'

const heights = {
  xs: 400,
  sm: 500,
  md: 650,
  lg: 810,
  xl: 900
}



const isMobile = useDisplay().mobile.value
const API_BASE = 'http://127.0.0.1:8000/test'
const logo = '/RjtFGBm1QW-esNwS5c1Gwi3o9wKpj4R1Hol7cAIgJ6UXYaKCSvcnU7NwpZvits3IX97p8TWEoBzOxL7m5VcpBVrP.png'
const oblozhka = '/oblozhka.jpg'







</script>

<style scoped>
.v-main { padding: 0; margin: 0; }
/* .v-carousel {
  margin: 0;
  width: 100vw !important;
  max-width: 100vw !important;
  position: relative;
  left: calc(50% - 50vw);
  right: calc(50% - 50vw);
} */
.custom-carousel-height { height: 400px !important; }
@media (min-width: 1280px) {
  .custom-carousel-height { height: 800px !important; }
}



</style>