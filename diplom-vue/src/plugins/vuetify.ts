// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Vuetify
import { createVuetify } from 'vuetify'
import { ru } from 'vuetify/locale'  // ← 1. Импортируй русский язык

export default createVuetify({
  // https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides

  // 🔹 Настройка языка
  locale: {
    locale: 'ru',           // ← Активный язык интерфейса
    fallback: 'en',         // ← Запасной язык, если нет перевода
    messages: { ru },       // ← Подключаем русские переводы
  },

  // 🔹 Иконки (если используешь MDI)
  icons: {
    defaultSet: 'mdi',
  },

  // 🔹 Глобальные настройки компонентов (опционально)
  defaults: {
    VDataTableServer: {
      itemsPerPageText: 'Показывать',  // ← Переопределение, если нужно
    },
  },
})