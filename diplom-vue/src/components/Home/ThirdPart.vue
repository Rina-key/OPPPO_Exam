<template>
  <v-container fluid class="pa-0 bg-white">
    <v-row align="stretch" no-gutters>

      <!-- Заголовок -->
      <v-col cols="12"  md="4" class="d-flex flex-column justify-center">
        <v-container
          class="d-flex flex-column justify-center pa-12 pa-md-16 bg-white"
          :class="isMobile ? 'mobile-panel' : 'web-panel'"
        >
          <h3 class="text-h4 text-md-h4 font-weight-bold mb-6 text-grey-darken-4 text-center">
            Бонусы и возможности <br> в профкоме
          </h3>

          <p class="text-body-1 text-grey text-center text-md-h8" >
            Узнайте о преимуществах и возможностях, которые открываются перед активистами профкома
          </p>
        </v-container>
      </v-col>

      <!-- Контент -->
      <v-col cols="12"  md="8" class="d-flex flex-column justify-center">
        <v-container class="pa-0">
          <v-sheet class="menu-scroll" elevation="0">
            <div class="menu-track">

              <div
                v-for="(group, i) in chunkedItems"
                :key="i"
                class="menu-page"
              >

                <v-hover
                  v-for="item in group"
                  :key="item.id"
                  v-slot="{ isHovering, props }"
                >
                  <v-card
                    class="menu-card"
                    elevation="2"
                    v-bind="props"
                  >

                    <!-- картинка -->
                    <div class="card-image-wrap">
                      <v-img :src="item.image" cover height="180" />

                      <v-chip
                        class="card-badge"
                        :style="{ backgroundColor: item.badgeColor }"
                        size="x-small"
                        label
                      >
                        {{ item.badge }}
                      </v-chip>
                    </div>

                    <!-- текст -->
                    <v-card-text class="card-body">
                      <div class="card-header">
                        <span class="card-title">{{ item.title }}</span>
                      </div>
                      <v-divider :thickness="2" class="border-opacity-50" color="grey"></v-divider>

                      <div class="card-description">
                        {{ item.description }}
                      </div>
                    </v-card-text>

                    <v-overlay
                      :model-value="!!isHovering"
                      class="align-center justify-center"
                      contained
                      scrim="rgba(0,0,0,0.30)"
                    >
                    </v-overlay>

                  </v-card>
                </v-hover>

              </div>

            </div>
          </v-sheet>
        </v-container>
      </v-col>

    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useDisplay } from 'vuetify'
import { allBonusCards, type CardMock } from '@/mocks/cards'

const display = useDisplay()
const isMobile = computed(() => display.mobile.value)

type MenuItem = CardMock

const menuItems: MenuItem[] = allBonusCards

const chunkSize = computed(() => {
  if (display.xs.value) return 2
  if (display.sm.value) return 4
  if (display.md.value) return 4
  return 8
})

const chunkedItems = computed(() => {
  const size = chunkSize.value
  const result = []
  for (let i = 0; i < menuItems.length; i += size) {
    result.push(menuItems.slice(i, i + size))
  }
  return result
})
</script>

<style scoped lang="scss">
.menu-scroll {
  overflow-x: auto;
  overflow-y: hidden;
  padding: 16px 0;
  -webkit-overflow-scrolling: touch;
}

.menu-track {
  display: flex;
  gap: 24px;
  scroll-snap-type: x mandatory;
}

.menu-page {
  flex: 0 0 100%;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  padding: 0 16px;
  scroll-snap-align: start;
  align-items: stretch;
}

/* планшет */
@media (max-width: 960px) {
  .menu-page {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* мобилка */
@media (max-width: 600px) {
  .menu-page {
    grid-template-columns: repeat(1, 1fr);
  }
}

.menu-card {
  width: 100%;
  height: 100%;
  border: 2px solid #1a1a1a;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.menu-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}

.card-image-wrap {
  position: relative;
  flex-shrink: 0;
}

.card-title {
  font-weight: 600;
  color: #1a1a1a;
}

.card-badge {
  position: absolute;
  top: 8px;
  left: 8px;
  color: white;
}

.card-body {
  padding: 10px;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.card-header {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
  flex-shrink: 0;
}

.card-description {
  flex: 1;
  font-size: 12px;
  color: #555;
  margin-top: 8px;
  overflow-y: auto;
}

.hover-btn {
  text-transform: none;
  font-weight: 600;
  border-radius: 10px;
}
</style>