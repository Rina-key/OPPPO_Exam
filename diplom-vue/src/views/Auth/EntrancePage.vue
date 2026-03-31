<template>
  <div class="d-flex flex-column fill-height">
    <v-main class="fill-height d-flex align-center justify-center">
      <EntranceForm />
    </v-main>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import EntranceForm from '@/components/Entrance/EntranceForm.vue'

export default defineComponent({
  name: 'EntrancePage',
  components: {
    EntranceForm,
  },
})
</script>

<style scoped></style>
