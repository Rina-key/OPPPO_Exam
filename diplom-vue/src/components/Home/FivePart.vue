<template>
  <v-container fluid class="pa-0 bg-white">
    <v-row align="stretch" no-gutters>
      <!-- Заголовок -->
      <v-col cols="12" md="5" class="d-flex flex-column justify-center">
        <v-container
          class="d-flex flex-column justify-center pa-12 pa-md-16 bg-white"
        >
          <h3 class="text-h4 text-md-h4 font-weight-bold mb-6 text-grey-darken-4 text-center">
            Часто задаваемые вопросы
          </h3>
          <p class="text-body-1 text-grey text-center text-md-h8" >
            Найдите ответы на популярные вопросы о профкоме
          </p>
        </v-container>
      </v-col>

      <!-- Контент -->
      <v-col cols="12" md="7" class="d-flex flex-column justify-center">
        <v-container class="pa-8 pa-md-12">
          <v-expansion-panels variant="accordion" class="faq-panels">
            <v-expansion-panel
              v-for="(item, index) in faqItems"
              :key="item.id"
            >
              <v-expansion-panel-title class="faq-title">
                <div class="d-flex align-center">
                  <v-icon 
                    :icon="item.icon" 
                    class="mr-4 question-icon"
                    size="24"
                  ></v-icon>
                  <span>{{ item.title }}</span>
                </div>
              </v-expansion-panel-title>
              <v-expansion-panel-text class="faq-text">
                <v-divider class="mb-4"></v-divider>
                {{ item.description }}
              </v-expansion-panel-text>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-container>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useDisplay } from 'vuetify'

const display = useDisplay()
const isMobile = computed(() => display.mobile.value)

interface FAQItem {
  id: number
  title: string
  description: string
  icon: string
}

const faqItems: FAQItem[] = [
  {
    id: 1,
    title: 'Как вступить в профком?',
    description: 'Для вступления необходимо заполнить заявление на сайте или в кабинете профкома. Процесс занимает не более 5 минут, а все преимущества становятся доступны сразу после вступления.',
    icon: 'mdi-account-plus'
  },
  {
    id: 2,
    title: 'Какие бонусы получают активисты?',
    description: 'Активисты получают доступ к эксклюзивным мероприятиям, ПГАС, мерчу и возможность участвовать в выездных школах лидерства.',
    icon: 'mdi-gift'
  },
  {
    id: 3,
    title: 'Можно ли совмещать активизм с учебой?',
    description: 'Да, мы ценим тайм-менеджмент. Все задачи планируются заранее, а нагрузка регулируется индивидуально. Многие наши лидеры успешно совмещают активизм, учебу и работу.',
    icon: 'mdi-calendar-clock'
  }
]
</script>

<style scoped lang="scss">
.faq-panels {
  max-width: 750px;
  
  :deep(.v-expansion-panel) {
    background: white;
    border-radius: 12px !important;
    margin-bottom: 12px !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    border: none !important;
    overflow: hidden;
    transition: all 0.3s ease;
    
    &:last-child {
      margin-bottom: 0;
    }

    
  }

  :deep(.v-expansion-panel-title) {
    padding: 20px 24px !important;
    font-weight: 600;
    color: #1a1a1a;
    font-size: 1.05rem;
    background: white;
    
    &:hover {
      background: #f8f9fa;
    }

    .v-expansion-panel-title__overlay {
      opacity: 0 !important;
    }
  }

  :deep(.v-expansion-panel-text) {
    padding: 0 24px 24px 24px !important;
    color: #555;
    line-height: 1.7;
    font-size: 0.95rem;
    background: white;
  }

  :deep(.v-expansion-panel-title__icon) {
    color: #1976d2;
    transition: transform 0.3s ease;
  }
}

.question-icon {
  color: #1976d2;
  flex-shrink: 0;
}

@media (max-width: 960px) {
  .faq-panels {
    :deep(.v-expansion-panel-title) {
      padding: 16px 18px !important;
      font-size: 0.95rem;
    }
    :deep(.v-expansion-panel-text) {
      padding: 0 18px 18px 18px !important;
      font-size: 0.9rem;
    }
  }
}
</style>