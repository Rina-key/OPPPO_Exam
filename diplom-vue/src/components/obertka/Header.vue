<template>
  <!-- Верхняя панель -->
  <v-app-bar app style="background-color: #2D32FF;">
    <v-app-bar-nav-icon
      class="white-icon"
      variant="text"
      @click.stop="toggleDrawer"
    ></v-app-bar-nav-icon>

    <v-btn 
      @click="onHome"
      color="white" 
    >ПРОЕКТ+</v-btn>
  </v-app-bar>

  <v-navigation-drawer
    class="header-drawer"
    v-model="drawer"
    app
    :rail="$vuetify.display.mdAndUp"
    :expand-on-hover="$vuetify.display.mdAndUp"
    :temporary="$vuetify.display.smAndDown"
    location="left" 
    @click:outside="$vuetify.display.smAndDown && (drawer = false)"
  >
    <div class="drawer-content">
      <v-list>
        <v-list-item
          prepend-avatar="https://randomuser.me/api/portraits/women/85.jpg"
          :subtitle="currentUser?.email || 'user@example.com'"
          :title="currentUser?.name || 'Пользователь'"
        />
      </v-list>

      <v-divider></v-divider>

      <v-list density="compact" nav>
        <v-list-item 
          prepend-icon="mdi-checkbook" 
          title="Новости" 
          link 
          :class="{ 'is-active': isRouteActive('/') }"
          @click="onHome" 
        />
        
        <v-list-item 
          v-if="isAuthenticated"
          prepend-icon="mdi-star" 
          title="Мероприятия" 
          link 
          :class="{ 'is-active': isRouteActive('/event') }"
          @click="onEvent" 
        />
        <v-list-item 
          v-if="isAuthenticated"
          prepend-icon="mdi-folder" 
          title="База знаний" 
          link 
          :class="{ 'is-active': isRouteActive('/knowledge') }"
          @click="onBase" 
        />
        <v-list-item 
          v-if="isAuthenticated"
          prepend-icon="mdi-pencil" 
          title="Мои задачи" 
          link 
          :class="{ 'is-active': isRouteActive('/mytask') }"
          @click="onMyTask" 
        />
        <v-list-item 
          v-if="isAuthenticated"
          prepend-icon="mdi-account-multiple" 
          title="Список активистов" 
          link 
          :class="{ 'is-active': isRouteActive('/activ') }"
          @click="onActiv" 
        />
        <v-list-item 
          v-if="isAuthenticated"
          prepend-icon="mdi-check-circle" 
          title="Ответы тестов" 
          link 
          :class="{ 'is-active': isRouteActive('/answer') }"
          @click="onAnswer" 
        />
      </v-list>

      <div class="bottom-actions">
        <v-list density="compact" nav>
          <v-list-item
            v-if="isAuthenticated"
            prepend-icon="mdi-cog" 
            title="Настройки" 
            link 
            :class="{ 'is-active': isRouteActive('/settings') }"
            @click="onSettingsClick" 
          />
          <v-list-item
            v-if="isAuthenticated"
            prepend-icon="mdi-logout" 
            title="Выйти" 
            link 
            @click="onLogoutClick" 
          />
          <!-- 🔹 Кнопка "Войти" скрыта для авторизованных -->
          <v-list-item 
            v-if="!isAuthenticated"
            prepend-icon="mdi-login" 
            title="Войти" 
            link 
            @click="onLoginClick" 
          />
        </v-list>
      </div>
    </div>
  </v-navigation-drawer>

  <!-- Диалог подтверждения выхода -->
  <LogoutDialog 
    v-model="showLogoutDialog" 
    @confirm="confirmLogout" 
  />
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import LogoutDialog from '@/components/obertka/LogoutDialog.vue'
import apiClient from '@/api/axios'

const router = useRouter()
const route = useRoute()
const drawer = ref(true)
const showLogoutDialog = ref(false)
const currentUser = ref<any>(null)

// 🔹 Реактивное состояние авторизации (вместо computed)
const isAuthenticated = ref(!!localStorage.getItem('token'))

// 🔹 Метод обновления состояния авторизации
const updateAuthState = () => {
  isAuthenticated.value = !!localStorage.getItem('token')
}

// 🔹 Загрузка данных пользователя
const loadCurrentUser = async () => {
  try {
    const token = localStorage.getItem('token')
    if (!token) {
      updateAuthState()
      return
    }
    
    const response = await apiClient.get('/user/me')
    currentUser.value = response.data
    updateAuthState()
  } catch (error) {
    console.log('Не удалось загрузить данные пользователя:', error)
    doLogout()
  }
}

// 🔹 Проверка активного маршрута
const isRouteActive = (path: string): boolean => {
  return route.path === path
}

const toggleDrawer = () => {
  drawer.value = !drawer.value
}

const onMyTask = () => router.push({ path: '/mytask' })
const onActiv = () => router.push({ path: '/activ' })
const onHome = () => router.push({ path: '/' })
const onEvent = () => router.push({ path: '/event' })
const onBase = () => router.push({ path: '/knowledge' })
const onAnswer = () => router.push({ path: '/answer' })

const onSettingsClick = () => {
  alert('Настройки')
}

// 🔹 Кнопка "Войти"
const onLoginClick = () => {
  router.push({ path: '/entrance' })
}

// 🔹 Открытие диалога выхода
const onLogoutClick = () => {
  showLogoutDialog.value = true
}

// 🔹 Подтверждение выхода
const confirmLogout = () => {
  showLogoutDialog.value = false
  doLogout()
}

// 🔹 Полная функция выхода с обновлением состояния
const doLogout = () => {
  const keys = ['token', 'token_type', 'login_time', 'user']
  keys.forEach(key => localStorage.removeItem(key))
  
  currentUser.value = null
  updateAuthState() // 🔹 ВАЖНО: обновляем реактивное состояние
  
  router.replace({ path: '/' })
}

// 🔹 Слушатель глобального события обновления авторизации
const handleAuthUpdated = () => {
  updateAuthState()
  if (isAuthenticated.value && !currentUser.value) {
    loadCurrentUser()
  }
}

onMounted(() => {
  loadCurrentUser()
  // Подписка на кастомное событие для синхронизации между компонентами
  window.addEventListener('auth-updated', handleAuthUpdated)
})

onBeforeUnmount(() => {
  window.removeEventListener('auth-updated', handleAuthUpdated)
})
</script>

<style scoped lang="scss">
.white-icon :deep(.v-icon) {
  color: white !important;
  opacity: 1 !important;
}

.transparent-drawer {
  background: transparent !important;
  backdrop-filter: blur(10px);
  border-right: 1px solid rgba(255, 255, 255, 0.2);
}

.transparent-drawer .v-list {
  background: transparent !important;
}

.transparent-drawer .v-list-item {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(5px);
  border-radius: 8px;
  margin: 4px 8px;
}

.transparent-drawer .v-list-item:hover {
  background: rgba(255, 255, 255, 0.2);
}

/* 👇 Активный пункт меню */
.is-active {
  :deep(.v-list-item-title) {
    font-weight: 500;
  }
  background: #8383833a;
}

.header-drawer .drawer-content {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.header-drawer .bottom-actions {
  margin-top: auto;
  width: 100%;
  padding-bottom: 1rem;
}
</style>