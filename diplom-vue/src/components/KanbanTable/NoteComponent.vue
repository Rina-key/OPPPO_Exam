<template>
  <div>
    <v-sheet
      @click.prevent="$emit('openContent')"
      :color="element.color"
      class="ma-1 pa-2 drag-object"
      :rounded="element.openContent && element.content ? 't-lg' : 'lg'"
      :elevation="2"
    >
      <v-row>
        <v-col>
          <h3 class="text-body-1 font-weight-bold">
            {{ element.title }}
          </h3>
        </v-col>
        <v-col cols="3" class="text-right">
          <v-col style="display:flex; justify-content:flex-end; gap:6px">
            <v-btn
              @click.prevent="$emit('requestEdit', element)"
              class="note-btn"
              flat
              icon
            >
              <v-icon icon="mdi-pencil" color="white" size="x-small"></v-icon>
            </v-btn>
            <v-dialog width="auto" v-model="element.deleteDialog">
              <template v-slot:activator="{ props }">
                <v-btn
                  class="note-btn"
                  flat
                  icon
                  v-bind="props"
                >
                  <v-icon icon="mdi-close" color="white" size="x-small"></v-icon>
                </v-btn>
              </template>
              <v-card class="text-center">
                <v-card-text>
                  <p class="text-body-1">Вы действительно хотите удалить задачу?</p>
                </v-card-text>
                <v-card-actions>
                  <v-btn @click.prevent="$emit('deleteNote', tab.id, element.id)">
                    Удалить
                  </v-btn>
                  <v-btn @click.prevent="$emit('openDeleteDialog')">
                    Отмена
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-col>
        </v-col>
      </v-row>
    </v-sheet>

    <!-- Разворачиваемая часть -->
    <v-expand-transition class="mt-n1">
      <div v-if="element.openContent && element.content">
        <v-sheet
          class="px-2 pt-2 mx-1 inner-shadow"
          rounded="b-lg"
          :color="element.color"
          style="min-height: 64px"
        >
          <p class="text-body-2 text-justify mb-2">{{ element.content }}</p>
          
          <!-- Дедлайн и Ответственный -->
          <v-divider class="my-2" color="white" :thickness="1"></v-divider>
          
          <div v-if="element.deadline" class="d-flex align-center text-body-2 mt-2">
            <v-icon icon="mdi-calendar-clock" size="small" class="mr-2" color="white"></v-icon>
            <strong>Дедлайн:</strong>
            <span class="ml-1">{{ formatDate(element.deadline) }}</span>
          </div>
          
          <div v-if="element.responsible" class="d-flex align-center text-body-2 mt-1">
            <v-icon icon="mdi-account-outline" size="small" class="mr-2" color="white"></v-icon>
            <strong>Ответственный:</strong>
            <span class="ml-1">{{ element.responsible }}</span>
          </div>
          
        </v-sheet>
      </div>
    </v-expand-transition>
  </div>
</template>

<script setup lang="ts">
const formatDate = (dateString: string) => {
  if (!dateString) return ''
  const date = new Date(dateString)
  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  })
}

const props = defineProps({
  element: {
    type: Object,
    required: true
  },
  tab: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['deleteNote', 'openContent', 'openDeleteDialog', 'requestEdit'])
</script>

<style scoped>
.note-btn {
  background-color: transparent;
  height: 24px !important;
  width: 24px !important;
}

.drag-object {
  cursor: pointer;
}
</style>