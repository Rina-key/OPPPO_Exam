<template>
  <v-footer class="text-center d-flex flex-column ga-2 py-4" color="#2D32FF">
    
	<div class="d-flex ga-3">
		<v-row> 
			<div class="text-body-small font-weight-regular opacity-90 align-center d-flex">
				Связаться с нами:
			</div>
			<v-btn
				icon="mdi-vk"
				density="comfortable"
				variant="text"
				href="https://vk.com/pos_ikit"
			></v-btn>
	  </v-row>
    </div>

    <v-divider class="my-2" thickness="2" width="50"></v-divider>

    <div class="text-body-small font-weight-regular opacity-60">
      Выпускная квалификационная работа по теме: <em>"Разработка веб-приложения для комплексного управления проектами и мероприятиями"</em>
    </div>

    <v-divider></v-divider>

    <div>{{ new Date().getFullYear() }} — <strong>RinaKey</strong></div>
  </v-footer>
</template>

<script setup lang="ts">
  
</script>
