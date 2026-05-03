<template>
  <v-sheet
    :class="'bg-white ' + (isMobile ? 'mobile-panel' : 'web-panel')"
    :elevation="1"
    rounded="lg"
  >
    <v-row no-gutters class="panel-header">
      <v-col cols="1" md="1">
        <v-icon icon="mdi-menu" class="label-btn"></v-icon>
      </v-col>
      <v-col cols="8" md="8" class="pl-1">
        <h2 class="text-body-h6 font-weight-bold panel-title text-center" style="line-height: 40px">
          {{ tab.name }}
        </h2>
      </v-col>
      <v-col cols="3" md="3" class="text-right">
        <v-btn icon flat @click.prevent="$emit('openTabCreate')" class="label-btn">
          <v-icon
            :icon="tab.create ? 'mdi-close' : 'mdi-plus'"
            class="toggle-icon"
            :class="{ open: tab.create }"
          ></v-icon>
        </v-btn>
      </v-col>
    </v-row>
    <v-divider></v-divider>
    
    <CreateNoteComponent
      :tab="tab"
      @createNote="$emit('createNote', tab.id)"
      @updateNote="$emit('updateNote', tab.id, $event)"
      @updateTitle="$emit('updateTitle', $event)"
      @updateContent="$emit('updateContent', $event)"
      @updateImportance="$emit('updateImportance', $event)"
      @updateDeadline="$emit('updateDeadline', $event)"
      @updateResponsible="$emit('updateResponsible', $event)"
    />
    
    <draggable group="people" :list="tab.notes" itemKey="id" class="drag-area">
      <template #item="{ element }">
        <NoteComponent
          :element="element"
          :tab="tab"
          @openContent="element.openContent = !element.openContent"
          @openDeleteDialog="element.deleteDialog = !element.deleteDialog"
          @deleteNote="$emit('deleteNote', tab.id, element.id)"
          @requestEdit="$emit('requestEdit', tab.id, element)"
        />
      </template>
    </draggable>
  </v-sheet>
</template>

<script setup lang="ts">
import draggable from 'vuedraggable'
import { useDisplay } from 'vuetify'
import NoteComponent from '@/components/KanbanTable/NoteComponent.vue'
import CreateNoteComponent from './CreateNoteComponent.vue'

const isMobile = useDisplay().mobile.value

const props = defineProps({
  tab: {
    type: Object,
    required: true
  }
})

const emits = defineEmits([
  'openTabCreate',
  'createNote',
  'updateNote',
  'requestEdit',
  'deleteNote',
  'updateTitle',
  'updateContent',
  'updateImportance',
  'updateDeadline',
  'updateResponsible'
])
</script>

<style scoped>
.web-panel {
  min-height: 70vh;
  height: 100%;
}

.mobile-panel {
  min-height: 30vh;
  height: 100%;
}

.label-btn {
  background-color: transparent;
  height: 40px !important;
  width: 40px !important;
  color: white !important;
}

.drag-area {
  min-height: 10vh;
}

.toggle-icon {
  transition: transform 0.5s ease, opacity 0.2s ease;
  opacity: 1;
}

.toggle-icon.open {
  transform: rotate(180deg) scale(1.1);
}

.inner-shadow {
  box-shadow: inset 0 5px 5px rgba(0, 0, 0, 0.1);
}

.panel-header {
  background: linear-gradient(135deg, #2D32FF 0%, #29b6f6 100%) !important;
  color: white !important;
  padding: 8px 12px;
  border-top-left-radius: 12px;
  border-top-right-radius: 12px;
  align-items: center;
}

.panel-header .toggle-icon,
.panel-header .v-icon {
  color: white !important;
}

.panel-title {
  color: white !important;
  font-weight: 800 !important;
  text-transform: uppercase;
  font-size: 0.95rem;
  letter-spacing: 0.5px;
  border: none !important;
  margin: 0;
}
</style>