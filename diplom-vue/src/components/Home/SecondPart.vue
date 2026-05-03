<template>
	<v-row align="stretch" no-gutters>
		
			<v-container class=" pa-4 pa-sm-8 pa-md-50 pa-lg-60" :class="isMobile ? 'mobile-panel' : 'web-panel'">
				<h3 class="text-h4 text-sm-h4 text-md-h4 text-lg-h4 font-weight-bold mb-4 mb-sm-6 mb-md-8 text-grey-darken-4 text-center">
					Выбери свой вектор развития
				</h3>
				<p class="text-body-2 text-sm-body-1 text-md-h7 mb-6 mb-sm-8 text-grey-darken-2 font-weight-regular text-center px-2" style="line-height: 1.6;">
					В нашей команде каждый студент может найти направление по душе: от правовой поддержки до организации мероприятий и развития талантов. Присоединяйся к нам, чтобы раскрыть свой потенциал и сделать студенчество незабываемым!
				</p> 
				
				
				<v-row class="license-cards" justify="center">
					
					<v-col cols="12" sm="6" md="6" lg="3" xl="3" class="px-2 px-sm-3 mb-4 mb-md-6">
						
						<v-card class="license-card" height="100%">
							<div class="popular-badge text-center py-2 py-sm-3">
								<p class="text-caption text-sm-body-2 text-white font-weight-medium mb-0 px-2">
									Защищаем студентов 24/7
								</p>
							</div>
							<v-card-text class="text-center pt-2 pt-sm-4 d-flex flex-column">
								
								<div class="icon-wrapper mb-2 mb-sm-4">
									<v-icon size="32" size-sm="40" color="grey-darken-1">mdi-shield</v-icon>
								</div>
								<div class="text-h5 text-sm-h6 font-weight-bold mb-4 mb-sm-6 px-1">Правовой отдел</div>
								
								<v-divider class="mb-3 mb-sm-4"></v-divider>
								
								<v-list density="compact" bg-color="transparent" class="mb-4 mb-sm-6 flex-grow-1">
									<v-list-item v-for="(item, index) in pravo" :key="index" class="px-0 text-left">
										<template v-slot:prepend>
											<v-icon size="20" size-sm="24" color="primary" class="mr-2">mdi-check</v-icon>
										</template>
										<v-list-item-title class="text-caption text-sm-body-2 text-grey-darken-3">{{ item }}</v-list-item-title>
									</v-list-item>
								</v-list>
							</v-card-text>
						</v-card>
					</v-col>

					<v-col cols="12" sm="6" md="6" lg="3" xl="3" class="px-2 px-sm-3 mb-4 mb-md-6">
						<v-card class="license-card" height="100%">
							<div class="popular-badge text-center py-2 py-sm-3">
								<p class="text-caption text-sm-body-3 text-white font-weight-medium mb-0 px-2">
									Создаем незабываемые впечатления
								</p>
							</div>
							<v-card-text class="text-center pt-2 pt-sm-4 d-flex flex-column">
								<div class="icon-wrapper mb-2 mb-sm-4">
									<v-icon size="32" size-sm="40" color="grey-darken-1">mdi-fire</v-icon>
								</div>
								<div class="text-h5 text-sm-h6 font-weight-bold mb-4 mb-sm-6 px-1">Культурно-массовый отдел</div>
								
								<v-divider class="mb-3 mb-sm-4"></v-divider>
								
								<v-list density="compact" bg-color="transparent" class="mb-4 mb-sm-6 flex-grow-1">
									<v-list-item v-for="(item, index) in party" :key="index" class="px-0 text-left">
										<template v-slot:prepend>
											<v-icon size="20" size-sm="24" color="primary" class="mr-2">mdi-check</v-icon>
										</template>
										<v-list-item-title class="text-caption text-sm-body-2 text-grey-darken-3">{{ item }}</v-list-item-title>
									</v-list-item>
								</v-list>
							</v-card-text>

						</v-card>
					</v-col>

					<v-col cols="12" sm="6" md="6" lg="3" xl="3" class="px-2 px-sm-3 mb-4 mb-md-6">
						
						<v-card class="license-card" height="100%">
							<div class="popular-badge text-center py-2 py-sm-3">
								<p class="text-caption text-sm-body-2 text-white font-weight-medium mb-0 px-2">
									Информируем обо всём
								</p>
							</div>
							<v-card-text class="text-center pt-2 pt-sm-4 d-flex flex-column">
								
								<div class="icon-wrapper mb-2 mb-sm-4">
									<v-icon size="32" size-sm="40" color="grey-darken-1">mdi-bullhorn</v-icon>
								</div>
								<div class="text-h5 text-sm-h6 font-weight-bold mb-4 mb-sm-6 px-1">Информационный отдел</div>
								
								<v-divider class="mb-3 mb-sm-4"></v-divider>
								
								<v-list density="compact" bg-color="transparent" class="mb-4 mb-sm-6 flex-grow-1">
									<v-list-item v-for="(item, index) in info" :key="index" class="px-0 text-left">
										<template v-slot:prepend>
											<v-icon size="20" size-sm="24" color="primary" class="mr-2">mdi-check</v-icon>
										</template>
										<v-list-item-title class="text-caption text-sm-body-2 text-grey-darken-3">{{ item }}</v-list-item-title>
									</v-list-item>
								</v-list>
							</v-card-text>

						</v-card>
					</v-col>

					<v-col cols="12" sm="6" md="6" lg="3" xl="3" class="px-2 px-sm-3 mb-4 mb-md-6">
						
						<v-card class="license-card" height="100%">
							<div class="popular-badge text-center py-2 py-sm-3">
								<p class="text-caption text-sm-body-2 text-white font-weight-medium mb-0 px-2">
									Создаём контент
								</p>
							</div>
							<v-card-text class="text-center pt-2 pt-sm-4 d-flex flex-column">
								
								<div class="icon-wrapper mb-2 mb-sm-4">
									<v-icon size="32" size-sm="40" color="grey-darken-1">mdi-camera-enhance</v-icon>
								</div>
								<div class="text-h5 text-sm-h5 font-weight-bold mb-4 mb-sm-6 px-1">Медиа отдел</div>
								
								<v-divider class="mb-3 mb-sm-4"></v-divider>
								
								<v-list density="compact" bg-color="transparent" class="mb-4 mb-sm-6 flex-grow-1">
									<v-list-item v-for="(item, index) in photo" :key="index" class="px-0 text-left">
										<template v-slot:prepend>
											<v-icon size="20" size-sm="24" color="primary" class="mr-2">mdi-check</v-icon>
										</template>
										<v-list-item-title class="text-caption text-sm-body-2 text-grey-darken-3">{{ item }}</v-list-item-title>
									</v-list-item>
								</v-list>
							</v-card-text>

						</v-card>
					</v-col>
				</v-row>
				
			</v-container>
		
	</v-row>

</template>

<script setup lang="ts">
	import { computed } from 'vue'
	import { useDisplay } from 'vuetify'

	const display = useDisplay()
	const isMobile = computed(() => display.mobile.value)

	const pravo = [
		'Члены всех коммиссий института',
		'Отстаиваем ваши интересы при взаимодействии с администрацией вуза',
		'Решаем спорные вопросы с общежитиями и стипендиальным обеспечением',
		'Представляем студентов во всех комиссиях института',
		'Помогаем восстановить справедливость в конфликтных ситуациях',
		'Обеспечиваем юридическую грамотность и правовую безопасность'
	]

	const party = [
		'Организуем яркие мероприятия и фестивали',
		'Создаем комфортную среду для творческой самореализации',
		'Объединяем студентов через волонтерство, творчество и спорт',
		'Работаем на мероприятиях различного масштаба',
		'Поддерживаем инициативы активистов и помогаем реализовывать идеи',
		'В команде отдела: организаторы и волонтеры'
	]

	const info = [
		'Оперативно информируем о важных изменениях в жизни университета',
		'Ведем активную работу в социальных сетях и мессенджерах',
		'Транслируем реальные истории и достижения наших студентов',
		'Создаем качественный контент, полезный для учебы и жизни',
		'Обеспечиваем прозрачность работы профкома через открытые каналы',
		'В команде отдела: копирайтеры и дизайнеры'
	]

	const photo = [
		'Обеспечиваем полное медиа-сопровождение всех активностей профкома',
		'Проводим мастер-классы по съемке и монтажу для новичков',
		'Наши фотографы фиксируют ключевые моменты студенческой жизни',
		'Видеографы снимают репортажи, промо-ролики и прямые трансляции',
		'Монтажеры собирают динамичный контент и работают со звуком',
		'В команде отдела: фотографы, видеографы и монтажеры',
	]
</script>

<style lang="scss" scoped>
.license-cards {
	margin-top: 1rem;
	
	@media (min-width: 960px) {
		margin-top: 2rem;
	}
}

.license-card {
	border-radius: 12px;
	background-color: #f8f7f7;
	border: 1px solid #2d30ff27;
	transition: all 0.3s ease;
	height: 100%;
	overflow: hidden;
	display: flex;
	flex-direction: column;
	
	@media (min-width: 600px) {
		border-radius: 16px;
	}
	
	&:hover {
		transform: translateY(-4px);
		box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
		border-color: rgba(45, 48, 255, 0.4);
		
		@media (min-width: 600px) {
			transform: translateY(-8px);
			box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
		}
	}
}

/* ✅ Стили для переноса текста в списках */
:deep(.v-list-item-title) {
	white-space: normal !important;
	word-wrap: break-word !important;
	word-break: break-word !important;
	line-height: 1.4 !important;
}

/* ✅ Растягиваем v-card-text на всю высоту карточки */
:deep(.v-card-text) {
	display: flex;
	flex-direction: column;
	flex: 1;
}

/* ✅ Растягиваем список, чтобы он занимал доступное место */
:deep(.v-list) {
	flex: 1;
}

.popular-card {
	border: 2px solid rgba(255, 255, 255, 0.3);
	position: relative;
	
	&:hover {
		border-color: rgba(255, 255, 255, 0.5);
	}
}

.popular-badge {
	background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
	border-radius: 0;
	margin: -1px -1px 0 -1px;
	
	@media (min-width: 600px) {
		border-radius: 12px 12px 0 0;
	}
	
	p {
		line-height: 1.4;
	}
}

.icon-wrapper {
	width: 64px;
	height: 64px;
	border-radius: 50%;
	background-color: rgba(255, 255, 255, 0.5);
	display: flex;
	align-items: center;
	justify-content: center;
	margin: 0 auto;
	border: 2px solid rgba(45, 48, 255, 0.2);
	
	@media (min-width: 600px) {
		width: 80px;
		height: 80px;
		background-color: rgba(255, 255, 255, 0.7);
	}
}

:deep(.v-list-item) {
	min-height: 32px;
	padding: 2px 0 !important;
	
	@media (min-width: 600px) {
		min-height: 36px;
		padding: 4px 0 !important;
	}
}

// :deep(.v-list-item__prepend) {
// 	// margin-inline-end: 8px;
	
// 	@media (min-width: 600px) {
// 		margin-inline-end: 12px;
// 	}
// }													

:deep(.v-btn) {
	text-transform: none;
	font-weight: 500;
	letter-spacing: 0.5px;
}

// Extra small devices (phones, less than 600px)
@media (max-width: 599px) {
	.license-card {
		max-width: 100%;
		margin: 0 auto;
	}
	
	.icon-wrapper {
		width: 56px;
		height: 56px;
	}
}

// Small devices (phones, 600px and up)
@media (min-width: 600px) and (max-width: 959px) {
	.license-card {
		max-width: 400px;
		margin: 0 auto;
	}
}

// Medium devices (tablets, 960px and up)
@media (min-width: 960px) and (max-width: 1263px) {
	.license-cards {
		margin-left: -8px;
		margin-right: -8px;
	}
}

// Large devices (desktops, 1264px and up)
@media (min-width: 1264px) {
	.license-cards {
		margin-left: -12px;
		margin-right: -12px;
	}
}

// Extra large devices (large desktops, 1904px and up)
@media (min-width: 1904px) {
	.license-cards {
		margin-left: -16px;
		margin-right: -16px;
	}
}
</style>