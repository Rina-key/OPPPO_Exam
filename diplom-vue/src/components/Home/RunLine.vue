<template>
  <div class="info-banner" ref="container">
    <div class="gradient-mask-left"></div>
    <div class="gradient-mask-right"></div>

    <div class="marquee-track" ref="track">
      <div class="marquee-group">
        <span
          v-for="(item, index) in bannerItems"
          :key="index"
          class="marquee-item"
        >
          <!-- MDI иконка -->
          <v-icon size="18" class="item-icon">
            {{ item.icon }}
          </v-icon>

          <span class="item-text">{{ item.text }}</span>
          <span class="separator">•</span>
        </span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, nextTick } from 'vue'

interface BannerItem {
  icon: string
  text: string
}

const bannerItems = ref<BannerItem[]>([
  { icon: 'mdi-shield-outline', text: 'ЗАЩИЩАЕМ И ПРЕДСТАВЛЯЕМ ПРАВА СТУДЕНТОВ' },
  { icon: 'mdi-star-outline', text: 'ЗДЕСЬ ЗАЖИГАЮТСЯ ЗВЁЗДЫ' },
  { icon: 'mdi-heart-outline', text: 'КОМАНДА МЕЧТЫ' },
  { icon: 'mdi-rocket-launch-outline', text: 'ВЫЕЗЖАЕМ НА ФОРУМЫ' },
  { icon: 'mdi-trophy-outline', text: 'УЧАСТВУЕМ В КОНКУРСАХ' },
  { icon: 'mdi-fire', text: 'ОРГАНИЗУЕМ МЕРОПРИЯТИЯ' },
  { icon: 'mdi-account-star-outline', text: 'РАЗВИВАЕМ ТАЛАНТЫ В КАЖДОМ' },
])

const container = ref<HTMLElement | null>(null)
const track = ref<HTMLElement | null>(null)

onMounted(async () => {
  await nextTick()

  if (!track.value || !container.value) return

  const group = track.value.querySelector('.marquee-group') as HTMLElement

  // 🔥 Дублируем до нужной ширины
  while (track.value.scrollWidth < container.value.offsetWidth * 6) {
    track.value.appendChild(group.cloneNode(true))
  }

  track.value.classList.add('animate')
})
</script>

<style scoped>
.info-banner {
  background: #2D32FF;
  color: white;
  padding: 12px 0;
  overflow: hidden;
  white-space: nowrap;
  position: relative;
}

.gradient-mask-left {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 100px;
  background: linear-gradient(to right, #2d30ff 0%, transparent 100%);
  z-index: 1;
}

.gradient-mask-right {
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
  width: 100px;
  background: linear-gradient(to left, #2D32FF 0%, transparent 100%);
  z-index: 1;
}

.marquee-track {
  display: flex;
  width: max-content;
  will-change: transform;
}

.marquee-track.animate {
  animation: marquee 59s linear infinite;
}

.marquee-group {
  display: flex;
}

.marquee-item {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 0 24px;
  font-weight: 600;
  font-size: 14px;
  letter-spacing: 1px;
  text-transform: uppercase;
}

.item-icon {
  opacity: 0.9;
}

.separator {
  margin-left: 8px;
  opacity: 0.4;
}

@keyframes marquee {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-50%);
  }
}

.info-banner:hover .marquee-track {
  animation-play-state: paused;
}
</style>