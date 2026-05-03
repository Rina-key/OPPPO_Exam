<template>
  <v-hover v-slot="{ isHovering, props }">
    <v-card
      class="bonus-card"
      elevation="2"
      v-bind="props"
    >
      <!-- Картинка + бейдж -->
      <div class="card-image-wrap">
        <v-img :src="image" cover height="180" />
        <v-chip
          v-if="badge"
          class="card-badge"
          :style="{ backgroundColor: badgeColor }"
          size="x-small"
          label
        >
          {{ badge }}
        </v-chip>
      </div>

      <!-- Контент -->
      <v-card-text class="card-body">
        <div class="card-header">
          <span class="card-title">{{ title }}</span>
          <span v-if="price" class="card-price">{{ price }} ₽</span>
        </div>
        <div class="card-description">
          {{ description }}
        </div>
      </v-card-text>

      <!-- Overlay при наведении -->
      <v-overlay
        :model-value="!!isHovering"
        class="align-center justify-center"
        contained
        scrim="rgba(0,0,0,0.45)"
      >
        <v-btn
          class="hover-btn"
          color="white"
          variant="flat"
          @click="handleClick"
        >
          Подробнее
        </v-btn>
      </v-overlay>
    </v-card>
  </v-hover>
</template>

<script setup lang="ts">
interface Props {
  id: number
  title: string
  description: string
  image: string
  badge?: string
  badgeColor?: string
  price?: string | number
}

const props = defineProps<Props>()
const emit = defineEmits<{
  (e: 'click', payload: { id: number }): void
}>()

const handleClick = () => {
  emit('click', { id: props.id })
}
</script>

<style scoped>
.bonus-card {
  width: 100%;
  border: 2px solid #1a1a1a;
  position: relative;
  overflow: hidden;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  border-radius: 12px;
}

.bonus-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}

.card-image-wrap {
  position: relative;
}

.card-badge {
  position: absolute;
  top: 8px;
  left: 8px;
  color: white;
  font-weight: 600;
}

.card-body {
  padding: 12px 10px 10px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 8px;
  margin-bottom: 6px;
}

.card-title {
  font-weight: 600;
  font-size: 14px;
  color: #1a1a1a;
  line-height: 1.3;
}

.card-price {
  color: #2d30ff;
  font-weight: 700;
  font-size: 14px;
  white-space: nowrap;
}

.card-description {
  font-size: 12px;
  color: #555;
  line-height: 1.4;
}

.hover-btn {
  text-transform: none;
  font-weight: 600;
  border-radius: 10px;
  padding: 0 24px;
}
</style>