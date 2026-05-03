<template>
	<v-container fluid class="pt-5">
		<!-- Заголовок -->
		<v-row align="stretch" no-gutters>
			<v-col cols="12">
				<v-container
					class="d-flex flex-column justify-center pa-0 pa-md-3"
					:class="isMobile ? 'mobile-panel' : 'web-panel'"
				>
					<h3 class="text-h4 text-md-h4 font-weight-bold mb-6 text-grey-darken-4 text-center">
						Истории активистов
					</h3>

					<p class="text-body-1 text-md-h8 mb-8 text-grey-darken-2 font-weight-regular text-center mx-auto" style="max-width: 1200px; line-height: 1.6;">
						Каждый активист когда-то был обычным студентом — всё изменилось в момент, когда он решил попробовать что-то большее и открыл для себя мир новых идей, людей и возможностей. <br> 
						Истории тех, кто однажды сделал шаг вперёд и превратил студенческую жизнь в нечто большее.
					</p>
				</v-container>
			</v-col>
		</v-row>

		<!-- Контент карусели -->
		<v-container
			class="d-flex flex-column justify-center pt-4 pb-16 pa-md-0"
			:class="isMobile ? 'mobile-panel' : 'web-panel'"
		>
			<v-row align="stretch" no-gutters justify="center">
				
				<!-- Левая колонка: Текст -->
				<v-col 
					cols="12" 
					md="7" 
					lg="6"
					class="d-flex flex-column justify-center"
				>
					<v-card 
						class="activist-card cursor-pointer"
						hover
					>
						<v-card-text class="pa-8 card-body-flex">
							<Transition name="slide-fade" mode="out-in">
								<div :key="currentActivist.id" class="d-flex flex-column h-100">
									
									<div class="activist-role text-primary font-weight-bold mb-2">
										{{ currentActivist.role }}
									</div>
									<h4 class="text-h5 font-weight-bold mb-4">
										{{ currentActivist.title }}
									</h4>
									<v-divider class="mb-4" thickness="2"></v-divider>
									
									<p class="text-body-1 text-grey-darken-2 activist-description mb-auto">
										{{ currentActivist.description }}
									</p>
									
									<div class="controls-wrapper">
										<div class="d-flex align-center mb-4">
											<!-- 👇 Добавлен @click.stop и класс cursor-pointer -->
											<v-chip 
												v-for="(_, index) in activists" 
												:key="index"
												:class="index === currentIndex ? 'active-chip' : 'inactive-chip'"
												class="mr-3 cursor-pointer"
												size="small"
												@click.stop="goToActivist(index)"
											></v-chip>
											<span class="ml-auto text-grey text-caption">
												{{ currentIndex + 1 }} / {{ activists.length }}
											</span>
										</div>

										<div class="d-flex">
											<v-btn 
												variant="text" 
												color="primary" 
												class="mr-2"
												@click.stop="prevActivist"
											>
												<v-icon start>mdi-arrow-left</v-icon>
												Назад
											</v-btn>

											<v-btn 
												variant="text" 
												color="primary" 
												@click.stop="nextActivist"
											>
												Вперед
												<v-icon end>mdi-arrow-right</v-icon>
											</v-btn>
										</div>
									</div>

								</div>
							</Transition>
						</v-card-text>
					</v-card>
				</v-col>

				<!-- Правая колонка: Фото -->
				<v-col 
					cols="12" 
					md="5" 
					lg="4"
					class="d-flex flex-column justify-center"
				>
					<v-hover v-slot="{ isHovering, props }">
						<Transition name="fade" mode="out-in">
							<v-img
								:key="currentActivist.id"
								:src="currentActivist.image"
								cover
								height="400"
								class="activist-image"
								:class="isHovering ? 'elevated' : ''"
								v-bind="props"
							></v-img>
						</Transition>
					</v-hover>
				</v-col>

			</v-row>
		</v-container>
	</v-container>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { useDisplay } from 'vuetify'
import { allActivists, type ActivistMock } from '@/mocks/activist'

const display = useDisplay()
const isMobile = computed(() => display.mobile.value)

const currentIndex = ref(0)
const activists: ActivistMock[] = allActivists

const currentActivist = computed<ActivistMock>(() => activists[currentIndex.value]!)

const nextActivist = () => {
	currentIndex.value = (currentIndex.value + 1) % activists.length
}

const prevActivist = () => {
	currentIndex.value = (currentIndex.value - 1 + activists.length) % activists.length
}

// 👇 Новая функция для перехода по клику на индикатор
const goToActivist = (index: number) => {
	currentIndex.value = index
}
</script>

<style scoped lang="scss">
.activist-card {
	display: flex;
	flex-direction: column;
	border-radius: 16px;
	transition: all 0.3s ease;
	min-height: 420px; 
	height: 100%;
}

.card-body-flex {
	display: flex;
	flex-direction: column;
	height: 100%;
	flex: 1;
}

.activist-description {
	line-height: 1.8;
	margin-bottom: auto !important; 
}

.activist-role {
	text-transform: uppercase;
	letter-spacing: 1px;
	font-size: 0.875rem;
}

/* Стили для кликабельных индикаторов */
.active-chip {
	background-color: #1976d2 !important;
	width: 32px;
	transition: all 0.3s ease;
	cursor: pointer;
}

.inactive-chip {
	background-color: #e0e0e0 !important;
	width: 8px;
	transition: all 0.3s ease;
	cursor: pointer;

	&:hover {
		background-color: #bdbdbd !important;
		width: 12px; /* Легкое увеличение при наведении */
	}
}

.activist-image {
	border-radius: 16px;
	box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
	transition: all 0.3s ease;
	overflow: hidden;
}

.elevated {
	box-shadow: 0 12px 32px rgba(0, 0, 0, 0.25);
	transform: translateY(-4px);
}

/* Анимации */
.fade-enter-active,
.fade-leave-active {
	transition: opacity 0.5s ease;
}
.fade-enter-from,
.fade-leave-to {
	opacity: 0;
}

.slide-fade-enter-active {
	transition: all 0.5s ease;
}
.slide-fade-leave-active {
	transition: all 0.3s ease;
}
.slide-fade-enter-from {
	opacity: 0;
	transform: translateY(20px);
}
.slide-fade-leave-to {
	opacity: 0;
	transform: translateY(-10px);
}

@media (max-width: 960px) {
	.activist-image {
		height: 410px !important;
	}
	.activist-card {
		min-height: auto;
	}
}

@media (max-width: 600px) {
	.activist-image {
		height: 350px !important;
	}
}
</style>