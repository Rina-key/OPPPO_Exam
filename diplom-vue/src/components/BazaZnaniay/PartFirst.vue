<template>
	<v-row class="part-first" align="center">
		<v-col cols="12" md="6" class="part-first__content">
			<h1 class="part-first__title">База знаний профкома</h1>
			<p class="part-first__text">
			Все, что нужно для организации мероприятий, работы в команде и решения вопросов. Инструкции, ресурсы, контакты и правовая база — в одном месте.
			</p>
		</v-col>
		<v-col cols="12" md="6" class="part-first__image-wrapper">
			<div class="image-blur-mask"></div>
			<img src="/ShapkaZnaniyaFon.jpg" alt="База знаний" class="part-first__image">
		</v-col>
	</v-row>
</template>

<script setup lang="ts">

</script>

<style scoped>
.part-first {
display: flex;
align-items: center;
min-height: 400px;
padding: 40px 0;
}

.part-first__content {
display: flex;
flex-direction: column;
justify-content: center;
padding-right: 40px;
}

.part-first__title {
font-size: 48px;
font-weight: 700;
color: #1a1a1a;
margin-bottom: 20px;
line-height: 1.2;
}

.part-first__text {
font-size: 18px;
line-height: 1.6;
color: #666;
max-width: 540px;
}

.part-first__image-wrapper {
position: relative;
display: flex;
justify-content: flex-end;
align-items: center;
}

.part-first__image {
width: 100%;
max-width: 600px;
height: auto;
object-fit: contain;
position: relative;
z-index: 1;
}

.image-blur-mask {
position: absolute;
left: 0;
top: 0;
bottom: 0;
width: 50%;
background: linear-gradient(to right,
rgba(255, 255, 255, 1) 0%,
rgba(255, 255, 255, 0.8) 20%,
rgba(255, 255, 255, 0.4) 40%,
rgba(255, 255, 255, 0.1) 60%,
rgba(255, 255, 255, 0) 100%
);
border-radius: 50% 0 0 50% / 60% 0 0 60%;
z-index: 2;
pointer-events: none;
}

/* Адаптивность */
@media (max-width: 960px) {
.part-first__title {
font-size: 36px;
}

.part-first__text {
font-size: 16px;
}

.part-first__content {
padding-right: 0;
margin-bottom: 30px;
text-align: center;
}

.part-first__text {
max-width: 100%;
}

.image-blur-mask {
display: none;
}
}
</style>


