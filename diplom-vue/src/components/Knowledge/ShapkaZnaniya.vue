<template>
  <div class="hero-section">
    <v-container class="pa-0" fluid>
      <v-row align="center" class="hero-row " >

        <!-- IMAGE -->
        <v-col
          cols="12"
          md="6"
          class="hero__image-col order-1 order-md-2 pa-0"
        >
          <div class="hero__image-wrapper">
            <img
              src="/FonZnaniya.png"
              alt="База знаний"
              class="hero__image"
              @error="showFallback = true"
            />
          </div>
        </v-col>

        <!-- TEXT -->
        <v-col
          cols="12"
          md="6"
          class="hero__content order-2 order-md-1 pa-16 pa-md-24"
        >
          <h1 class="hero__title ">
            База знаний ПОС ИКИТ
          </h1>

          <p class="hero__text">
            Все, что нужно для организации мероприятий, работы в команде и решения вопросов.
            Инструкции, ресурсы, контакты и правовая база — в одном месте.
          </p>

          
        </v-col>

      </v-row>
    </v-container>
  </div>

  <v-divider :thickness="3" class="border-opacity-50" color="primary"></v-divider>
  
  <!-- QUICK ACTIONS -->
  <v-container
    class="quick-actions-wrapper"
    style="margin-top: -20px; position: relative; z-index: 10;"
  >
    <v-row>
      <v-col
        v-for="(action, i) in quickActions"
        :key="i"
        cols="12"
        sm="4"
      >
        <v-card
          class="quick-action-card"
          variant="flat"
          elevation="2"
          rounded="lg"
          @click="handleAction(action)"
        >
          <div class="d-flex align-center pa-4">
            <v-avatar
              rounded="lg"
              size="44"
              :color="action.iconBg"
              class="mr-4"
            >
              <v-icon :color="action.iconColor" size="22">
                {{ action.icon }}
              </v-icon>
            </v-avatar>

            <span class="text-subtitle-2 font-weight-bold flex-grow-1">
              {{ action.label }}
            </span>

            <v-icon color="grey-darken-2" size="18">
              mdi-arrow-right
            </v-icon>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const showFallback = ref(false)
const searchQuery = ref('')

const quickActions = [
  { icon: 'mdi-plus', iconBg: '#fce4f0', iconColor: '#e0579a', label: 'Организовать мероприятие' },
  { icon: 'mdi-email-outline', iconBg: '#e8e6ff', iconColor: '#6c63ff', label: 'Связаться с председателем' },
  { icon: 'mdi-file-document-outline', iconBg: '#dde8ff', iconColor: '#4a7dff', label: 'Скачать документы' },
]

const handleAction = (action: typeof quickActions[0]) => {
  console.log('Action clicked:', action.label)
}
</script>

<style lang="scss" scoped>
.hero-section {
  background:
    radial-gradient(circle at 10% 50%, #ffffff 0%, rgba(255, 255, 255, 0) 55%),
    radial-gradient(circle at 85% 40%, rgba(245, 225, 255, 0.229) 0%, transparent 50%),
    linear-gradient(90deg, #ffffff 0%, #fee8f9 40%, #c0cdfc 100%);

  padding: 0px 0;
  position: relative;
  overflow: hidden;
}

/* декоративные элементы */
.hero-section::before {
  content: '';
  position: absolute;
  top: -60px;
  left: -60px;
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(255, 220, 235, 0.25) 0%, transparent 70%);
  border-radius: 50%;
}

.hero-section::after {
  content: '';
  position: absolute;
  bottom: -40px;
  right: 15%;
  width: 320px;
  height: 320px;
  background: radial-gradient(circle, rgba(200, 190, 255, 0.15) 0%, transparent 70%);
  border-radius: 50%;
}

.hero-row {
  position: relative;
  z-index: 1;
}

.hero__image-col {
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero__image-wrapper {
  width: 100%;
  display: flex;
  justify-content: center;
}

.hero__image {
  width: 100%;
  height: auto;
  max-height: 360px; 
  object-fit: contain;
}

.hero__content {
  
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.hero__title {
  font-size: 36px;
  // font-weight: 800;
  // margin-bottom: 16px;
  margin-bottom: 20px;
  padding-left: 95px;
    background: linear-gradient(135deg, #2D32FF 0%, #66B5F6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-family: 'Montserrat', sans-serif;

}

.hero__text {
  font-size: 18px;
  line-height: 1.6;
  max-width: 600px;
  margin-bottom: 0px;
  font-family: 'Montserrat', sans-serif;
  padding-left: 95px;
}

.hero__search {
  max-width: 460px;
}

.search-field :deep(.v-field) {
  background: white;
  border-radius: 9999px;
}

/* QUICK ACTIONS */
.quick-actions-wrapper {
  padding-top: 0;
  padding-bottom: 16px;
}

.quick-action-card {
  cursor: pointer;
  transition: all 0.2s ease;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12) !important;
  }
}

/* АДАПТИВ */
@media (max-width: 960px) {
  .hero__content {
    padding-left: 0;
    text-align: center;
    align-items: center;
  }

  .hero__title {
    font-size: 26px;
  }

  .hero__image {
    max-height: 260px;
  }
}

@media (max-width: 480px) {
  .hero__title {
    font-size: 22px;
  }

  .hero__text {
    font-size: 14px;
  }
}
</style>