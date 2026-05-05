<template>
  

    <!-- ==================== HERO ==================== -->
    

    <!-- ==================== MAIN SECTION CARDS ==================== -->
    <v-container>
      <h2 class="section-title">Основные разделы</h2>
      <v-row>
        <v-col
          v-for="(section, i) in mainSections"
          :key="i"
          cols="12"
          sm="6"
          lg="3"
        >
          <v-card
            class="main-card"
            variant="flat"
            rounded="xl"
            elevation="1"
          >
            <v-card-text class="pa-6">
              <div class="d-flex align-center mb-3">
                <span class="card-emoji mr-2">{{ section.emoji }}</span>
                <span
                  class="text-caption font-weight-bold text-uppercase"
                  :style="{ color: section.color }"
                >
                  {{ section.number }}. {{ section.title }}
                </span>
              </div>

              <p class="text-body-2 text-medium-emphasis mb-2">{{ section.description }}</p>

              <ul class="card-list">
                <li v-for="(item, j) in section.items" :key="j">{{ item }}</li>
              </ul>

              <a
                href="#"
                class="card-link"
                :style="{ color: section.color }"
              >
                Перейти в раздел
                <v-icon size="14" end>mdi-arrow-right</v-icon>
              </a>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>

    <!-- ==================== TWO-COLUMN: Popular + Contacts ==================== -->
    <v-container>
      <v-row>

        <!-- Popular -->
        <v-col cols="12" md="6">
          <v-card variant="flat" rounded="xl" elevation="1">
            <v-card-title class="d-flex align-center justify-space-between pa-5 pb-2">
              <span class="text-subtitle-1 font-weight-bold">🔥 Популярное</span>
              <a href="#" class="text-caption font-weight-medium text-grey-darken-2">Смотреть все</a>
            </v-card-title>
            <v-divider />
            <v-list lines="one" class="py-0">
              <v-list-item
                v-for="(item, i) in popularItems"
                :key="i"
                class="popular-item"
              >
                <template #prepend>
                  <span class="popular-num">{{ i + 1 }}</span>
                </template>
                <v-list-item-title class="text-body-2">{{ item.text }}</v-list-item-title>
                <template #append>
                  <v-chip size="x-small" variant="tonal" color="primary">{{ item.tag }}</v-chip>
                </template>
              </v-list-item>
            </v-list>
          </v-card>
        </v-col>

        <!-- Contacts -->
        <v-col cols="12" md="6">
          <v-card variant="flat" rounded="xl" elevation="1">
            <v-card-title class="d-flex align-center justify-space-between pa-5 pb-2">
              <span class="text-subtitle-1 font-weight-bold">Контакты по направлениям</span>
              <a href="#" class="text-caption font-weight-medium text-grey-darken-2">Все контакты →</a>
            </v-card-title>
            <v-divider />
            <v-card-text class="pa-4">
              <v-row>
                <v-col
                  v-for="(contact, i) in contacts"
                  :key="i"
                  cols="6"
                >
                  <div class="contact-card-inner">
                    <v-avatar rounded="lg" size="44" color="#e8e6ff">
                      <v-icon>{{ contact.avatar }}</v-icon>
                    </v-avatar>
                    <div>
                      <div class="text-subtitle-2 font-weight-bold">{{ contact.name }}</div>
                      <div class="text-caption text-grey-darken-1">{{ contact.role }}</div>
                    </div>
                  </div>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>

      </v-row>
    </v-container>

    <!-- ==================== TWO-COLUMN: Legal + FAQ ==================== -->
    <v-container>
      <v-row>

        <!-- Legal -->
        <v-col cols="12" md="6">
          <v-card variant="flat" rounded="xl" elevation="1">
            <v-card-title class="d-flex align-center justify-space-between pa-5 pb-2">
              <span class="text-subtitle-1 font-weight-bold">⚖ Правовая база простым языком</span>
              <a href="#" class="text-caption font-weight-medium text-grey-darken-2">Смотреть все →</a>
            </v-card-title>
            <v-divider />
            <v-list lines="one" class="py-0">
              <v-list-item
                v-for="(item, i) in legalItems"
                :key="i"
                class="legal-item"
              >
                <template #prepend>
                  <v-avatar rounded="sm" size="28" color="#e8e6ff">
                    <v-icon size="14" color="#6c63ff">{{ item.icon }}</v-icon>
                  </v-avatar>
                </template>
                <v-list-item-title class="text-body-2">{{ item.text }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-card>
        </v-col>

        <!-- FAQ -->
        <v-col cols="12" md="6">
          <v-card variant="flat" rounded="xl" elevation="1">
            <v-card-title class="d-flex align-center justify-space-between pa-5 pb-2">
              <span class="text-subtitle-1 font-weight-bold">FAQ / Частые вопросы</span>
              <a href="#" class="text-caption font-weight-medium text-grey-darken-2">Смотреть все →</a>
            </v-card-title>
            <v-divider />
            <v-list lines="one" class="py-0">
              <v-list-item
                v-for="(item, i) in faqItems"
                :key="i"
                class="faq-item"
              >
                <template #prepend>
                  <v-avatar rounded="pill" size="22" color="#e8e6ff">
                    <span class="text-caption font-weight-bold" style="color: #6c63ff;">?</span>
                  </v-avatar>
                </template>
                <v-list-item-title class="text-body-2">{{ item.question }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-card>
        </v-col>

      </v-row>
    </v-container>

    <!-- ==================== BOTTOM BANNER ==================== -->
    <v-container class="mb-8">
      <v-card
        variant="flat"
        rounded="xl"
        class="bottom-banner"
        color="#f4e4ff"
      >
        <v-row align="center" no-gutters>
          <v-col cols="12" md="6" class="pa-8">
            <h3 class="text-h5 font-weight-bold mb-2">Знания — это сила активиста</h3>
            <p class="text-body-2 text-medium-emphasis mb-4">
              Используй базу знаний, чтобы быстрее находить ответы, эффективно работать и создавать крутые проекты вместе с профкомом!
            </p>
            <v-btn
              color="primary"
              rounded="lg"
              class="font-weight-bold"
            >
              Есть вопрос? Напиши нам
            </v-btn>
          </v-col>
          <v-col cols="12" md="6" class="d-none d-md-block">
            <svg viewBox="0 0 360 180" fill="none" class="w-100">
              <circle cx="80" cy="100" r="30" fill="#dde8ff" />
              <rect x="55" y="130" width="50" height="40" rx="8" fill="#dde8ff" />
              <circle cx="160" cy="90" r="30" fill="#f4e4ff" />
              <rect x="135" y="120" width="50" height="40" rx="8" fill="#f4e4ff" />
              <circle cx="240" cy="100" r="30" fill="#fce4f0" />
              <rect x="215" y="130" width="50" height="40" rx="8" fill="#fce4f0" />
              <circle cx="310" cy="95" r="30" fill="#e0ffe4" />
              <rect x="285" y="125" width="50" height="40" rx="8" fill="#e0ffe4" />
              <rect x="120" y="140" width="100" height="30" rx="4" fill="#c8ccf0" />
              <rect x="130" y="145" width="80" height="15" rx="2" fill="#fff" />
            </svg>
          </v-col>
        </v-row>
      </v-card>
    </v-container>

  
</template>

<script setup lang="ts">
import { ref } from 'vue'

const showFallback = ref(false)
const searchQuery = ref('')

// Data
const quickActions = [
  { icon: 'mdi-plus', iconBg: '#fce4f0', iconColor: '#e0579a', label: 'Организовать мероприятие' },
  { icon: 'mdi-email-outline', iconBg: '#e8e6ff', iconColor: '#6c63ff', label: 'Связаться с главой' },
  { icon: 'mdi-file-document-outline', iconBg: '#dde8ff', iconColor: '#4a7dff', label: 'Скачать документы' },
]

const mainSections = [
  {
    number: '1',
    title: 'Организация мероприятий',
    emoji: '📅',
    color: '#e0579a',
    description: 'Пошаговые инструкции, чек-листы и шаблоны для организации мероприятий от идеи до отчёта.',
    items: ['Как организовать мероприятие с нуля', 'Таймлайн подготовки', 'Бронирование аудитории', 'Работа с бюджетом', 'Согласование с вузом', 'Шаблоны документов'],
  },
  {
    number: '2',
    title: 'Полезные ресурсы',
    emoji: '📚',
    color: '#4a7dff',
    description: 'Подборка сервисов, платформ и материалов, которые упрощают работу и помогают развиваться.',
    items: ['Дизайн и визуал', 'Организация работы', 'Коммуникация и чаты', 'Продвижение и соцсети', 'Фото и видео', 'Обучающие материалы'],
  },
  {
    number: '3',
    title: 'Контакты',
    emoji: '👤',
    color: '#34c77a',
    description: 'К кому обращаться по вопросам мероприятий, документов, медиа и другим направлениям.',
    items: ['Председатель профкома', 'Заместители', 'Главы направлений', 'Ответственные лица', 'Контакты по вопросам'],
  },
  {
    number: '4',
    title: 'Правовая база',
    emoji: '⚖️',
    color: '#e89a2e',
    description: 'Объясняем законы и положения понятным языком: ваши права, льготы и возможности.',
    items: ['Положение о профкоме', 'Права и обязанности студентов', 'Материальная поддержка', 'Нормативные документы', 'Разбор законов и актов'],
  },
]

const popularItems = [
  { text: 'Как организовать мероприятие с нуля', tag: 'мероприятия' },
  { text: 'Шаблон заявки на мероприятие', tag: 'документы' },
  { text: 'Как получить материальную поддержку', tag: 'правовая база' },
  { text: 'К кому обращаться по вопросам?', tag: 'контакты' },
  { text: 'Чек-лист подготовки мероприятия', tag: 'мероприятия' },
]

const contacts = [
  { avatar: 'mdi-account-tie', name: 'Иванов Иван', role: 'Председатель' },
  { avatar: 'mdi-laptop', name: 'Петрова Анна', role: 'Медиа-отдел' },
  { avatar: 'mdi-calendar-check', name: 'Сидоров Максим', role: 'Орг-отдел' },
  { avatar: 'mdi-music', name: 'Ким Екатерина', role: 'Культурно-массовый отдел' },
]

const legalItems = [
  { icon: 'mdi-scale-balance', text: 'Положение о профкоме студентов' },
  { icon: 'mdi-shield-account', text: 'Права и обязанности студентов' },
  { icon: 'mdi-cash-multiple', text: 'Материальная поддержка' },
  { icon: 'mdi-file-document', text: 'Нормативные документы и акты' },
  { icon: 'mdi-magnify', text: 'Разбор законов и положений' },
]

const faqItems = [
  { question: 'Как вступить в профком?' },
  { question: 'Как предложить идею мероприятия?' },
  { question: 'Как проходит согласование мероприятия?' },
  { question: 'Где взять финансирование на проект?' },
  { question: 'Что делать, если есть проблема или вопрос?' },
  { question: 'Как получить материальную поддержку?' },
]

// Methods

</script>

<style scoped lang="scss">

.knowledge-base-page {
  background: #f9f9ff;
  min-height: 100vh;
  padding-top: 0px;
  padding-left: 0px;
  padding-right: 0px;
}
/* Hero Section */
.hero-section {
  background: linear-gradient(160deg, #eef0ff 0%, #d8ddff 40%, #bfc6ff 100%);
  padding: 0px 0;
  position: relative;
  overflow: hidden;
}

.hero-section::before {
  content: '';
  position: absolute;
  top: -120px;
  right: -120px;
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(100, 120, 255, 0.15) 0%, transparent 70%);
  border-radius: 50%;
  pointer-events: none;
}

.hero-row {
  position: relative;
  z-index: 1;
  min-height: 380px;
}

.hero__image-col {
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero__image-wrapper {
  position: relative;
  width: 100%;
  max-width: 560px;
}

.image-blur-mask {
  position: absolute;
  inset: -30px;
  background: radial-gradient(ellipse at center, rgba(120, 130, 255, 0.18) 0%, transparent 70%);
  z-index: 0;
  border-radius: 50%;
  pointer-events: none;
}

.hero__image {
  position: relative;
  z-index: 1;
  width: 100%;
  height: auto;
  display: block;
  border-radius: 16px;
  min-height: 260px;
  object-fit: contain;
}

.hero__image--fallback {
  background: transparent;
}

.hero__content {
  padding-left: 20px;
}

.hero__title {
  font-size: 38px;
  font-weight: 800;
  color: #1a1a2e;
  line-height: 1.15;
  margin-bottom: 16px;
}

.hero__text {
  font-size: 16px;
  line-height: 1.65;
  color: #4a4a6a;
  max-width: 480px;
  margin-bottom: 24px;
}

.hero__search {
  max-width: 480px;
}

.search-field :deep(.v-field) {
  background: white;
}

/* Section Title */
.section-title {
  font-size: 24px;
  font-weight: 700;
  color: #1e1e2f;
  margin-bottom: 24px;
}

/* Main Cards */
.main-card {
  height: 100%;
  transition: transform 0.2s;
}

.main-card:hover {
  transform: translateY(-4px);
}

.card-emoji {
  font-size: 36px;
  line-height: 1;
}

.card-list {
  list-style: none;
  padding: 0;
  margin: 12px 0 16px;
}

.card-list li {
  padding: 4px 0;
  font-size: 13px;
  color: #5a5a7a;
  position: relative;
  padding-left: 14px;
}

.card-list li::before {
  content: '•';
  position: absolute;
  left: 0;
  color: #c0c4e0;
}

.card-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
  transition: gap 0.2s;
}

.card-link:hover {
  gap: 10px;
}

/* Quick Actions */
.quick-action-card {
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.quick-action-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(40, 50, 120, 0.12) !important;
}

/* Popular Items */
.popular-item {
  cursor: pointer;
  transition: background 0.2s;
}

.popular-item:hover {
  background: rgba(100, 120, 255, 0.05);
}

.popular-num {
  font-weight: 700;
  color: #e0579a;
  min-width: 24px;
}

/* Contact Card Inner */
.contact-card-inner {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px;
  border-radius: 12px;
  border: 1px solid #f0f1f7;
  transition: border-color 0.2s;
  cursor: pointer;
}

.contact-card-inner:hover {
  border-color: #c8ccf0;
}

/* Legal Items */
.legal-item {
  cursor: pointer;
  transition: background 0.2s;
}

.legal-item:hover {
  background: rgba(100, 120, 255, 0.05);
}

/* FAQ Items */
.faq-item {
  cursor: pointer;
  transition: background 0.2s;
}

.faq-item:hover {
  background: rgba(100, 120, 255, 0.05);
}

/* Bottom Banner */
.bottom-banner {
  background: linear-gradient(135deg, #f4e4ff 0%, #dde8ff 100%);
  overflow: hidden;
}

/* Responsive */
@media (max-width: 960px) {
  .hero__title {
    font-size: 28px;
  }
  
  .hero__content {
    padding-left: 0;
    text-align: center;
  }
  
  .hero__text {
    margin: 0 auto 24px;
  }
  
  .hero__search {
    margin: 0 auto;
  }
  
  .hero__image-col {
    order: -1 !important;
    margin-bottom: 24px;
  }
}

@media (max-width: 600px) {
  .quick-actions-wrapper {
    margin-top: 16px;
  }
  
  .section-title {
    font-size: 20px;
  }
}
</style>