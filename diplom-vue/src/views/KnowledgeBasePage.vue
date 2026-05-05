<template>
  <v-main class="knowledge-base-page">
      <ShapkaZnaniya /> 
  
    <PartFirst />

  </v-main>
  
</template>

<script setup lang="ts">
import PartFirst from '@/components/Knowledge/PartFirst.vue';
import ShapkaZnaniya from '@/components/Knowledge/ShapkaZnaniya.vue';
</script>

<style scoped lang="scss">
.knowledge-base-page {
  min-height: 100vh;
  padding-top: 0px;
  padding-left: 0px;
  padding-right: 0px;
  // background: 
  //   white
    // radial-gradient(circle at 10% 50%, #ffffff 0%, rgba(255, 255, 255, 0) 55%),
    // radial-gradient(circle at 85% 40%, rgba(245, 225, 255, 0.229) 0%, transparent 50%),
    // linear-gradient(90deg, #ffffff 0%, #fee8f9 40%, #c0cdfc 100%);
  
}
</style>