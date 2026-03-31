<template>
  <div class="pa-4 text-center">
    <v-dialog
      v-model="dialog"
      max-width="600"
    >
      <v-card
        prepend-icon="mdi-account"
        title="Редактирование информации"
      >
	        
        <v-card-text>
			
		<v-row>
          <v-col dense>
            <v-row>
				<v-col
				cols="12"
				md="12"
				sm="12"
				>
				<v-text-field
					label="ФИО*"
					required
				></v-text-field>
				</v-col>
			</v-row>

			<v-row>
				<v-col
				cols="12"
				md="4"
				sm="6"
				>
				<v-text-field
					label="Группа*"
					required
				></v-text-field>
				</v-col>

				<v-col
				cols="12"
				md="4"
				sm="6"
				>
				<v-text-field
					label="Телефон*"
					persistent-hint
					required
				></v-text-field>
				</v-col>
			</v-row>

			<v-row>
				<v-col
				cols="12"
				md="4"
				sm="6"
				>
				<v-text-field
					label="Почта"
					required
				></v-text-field>
				</v-col>

				<v-col
				cols="12"
				md="4"
				sm="6"
				>
				<v-select
					:items="['Бюджет', 'Платная']"
					label="Форма обучения"
					required
				></v-select>
				</v-col>
			</v-row>

			<v-row>
				<v-col
				cols="12"
				md="4"
				sm="6"
				>
				<v-text-field
					label="Ссылка на ВК*"
					type="password"
					required
				></v-text-field>
				</v-col>

				<v-col
				cols="12"
				md="4"
				sm="6"
				>
				<v-text-field
					label="Ссылка на ТГ"
					
				></v-text-field>
				</v-col>
			</v-row>
            
          </v-col>
		</v-row>
          <small class="text-caption text-medium-emphas">*обязательное поле</small>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="primary"
            text="Сохранить"
            variant="tonal"
            @click="dialog = false"
          ></v-btn>

		  <v-btn
            text="Закрыть"
            variant="plain"
            @click="dialog = false"
          ></v-btn>

        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script setup lang="ts">
  import { ref } from 'vue'

const emit = defineEmits<{
  confirm: [item: any]
  cancel: []
}>()

const dialog = ref(false)
const formData = ref<any>({})
const originalItem = ref<any>(null)

const open = (item: any) => {
  console.log('✏️ [EditDialog] open() вызван:', item)
  originalItem.value = item
  formData.value = { ...item }
  dialog.value = true
}

const cancel = () => {
  dialog.value = false
  emit('cancel')
}

const save = () => {
  console.log('💾 [EditDialog] save() вызван')
  const updatedItem = { 
    ...originalItem.value, 
    ...formData.value 
  }
  dialog.value = false
  emit('confirm', updatedItem)
}

defineExpose({ open })
</script>