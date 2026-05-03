<template>
	
		<v-row align="stretch" no-gutters>
			<v-col cols="12" lg="6" md="6" class="d-flex  justify-center">
				<v-container class="d-flex flex-column justify-center pa-12 pa-md-16 bg-white" :class="isMobile ? 'mobile-panel' : 'web-panel'">
				
				
				<h1 class="text-h3 text-md-h3 font-weight-bold mb-8 text-grey-darken-4">
					Создаём условия для<br>лучшего студенчества
				</h1>
				
				
				<p class="text-body-1 text-md-h6 mb-8 text-grey-darken-2 font-weight-regular" style="max-width: 500px; line-height: 1.6;">
					Отстаиваем права и помогаем с 2008 года
				</p>
				
				
				<v-row >
					<v-col cols="12" lg="6" sm="7" class="d-flex justify-center ">
						<v-btn 
						color="primary" 
						size="large" 
						rounded="lg"
						class="px-8"
						height="48"
						href='https://vk.com/pos_ikit?w=app5619682_-2289674' 
						>
						Присоединиться
						</v-btn>
					</v-col>
					<!-- <v-col cols="12" lg="6" sm="5" class="d-flex justify-center ">
						<v-btn 
						variant="outlined" 
						size="large" 
						rounded="lg"
						class="px-8"
						height="48"
						color="grey-darken-2"
						>
						Узнать больше
						</v-btn>
					</v-col> -->
				</v-row>
				
				</v-container>
			</v-col>
			
			<v-col cols="12" md="6" class="d-flex flex-column justify-center">
				<v-container :class="'h-90 ' + (isMobile ? 'mobile-panel' : 'web-panel')"
				class="d-flex flex-column pa-0"> 
				<v-carousel 
					show-arrows="hover" 
					cycle 
					hide-delimiter-background
					
				>
					<v-carousel-item
					v-for="(src, i) in images"
					:key="i"
					:src="src"
					cover
					class="rounded-x0"
					></v-carousel-item>
				</v-carousel>
				</v-container>
			</v-col>
		</v-row>
	
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useDisplay } from 'vuetify'
import { hr } from 'vuetify/locale'


const display = useDisplay()
const isMobile = computed(() => display.mobile.value)


const images = [
  '\BFwS0xXNdIGsfxsuYPJdOstdNnLxOlTYrdlXjs_BG_sSwEbKbrpeekYtzreMyCZXvhc-RkiHgE1bqueqDx4DcTMf.jpg',
  '\C0Vh35tUVbZZj8arjDM07ozcQyJoXTMi1urqR5wfBUZalRyjP9PRE43aVQ5PcRo-522Lti1IQxO21UIVcx4O_G5C.jpg',
  '\LdWifrSADGupraFNwJuL7voi14io97wUx77ILoCirT7EP9h9uU7bnPfpjG5mz963dBMX8l1se1za7PeJtDoMQle1.jpg',
  '\LYM14obH--_jNpC0r336auHxR5TRqYfSj4yHUzOrx_O7H9rxgcQCRpfm0kpHg_7y7QIijoelLYqdSNsE8bHy2MJZ.jpg',
  '\Mopshond2_03-10-2005.jpg'
]
</script>