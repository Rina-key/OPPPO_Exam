<template>
  <v-main>
    <v-carousel
      height="500"
      show-arrows="hover"
      cycle
      hide-delimiter-background
    >
      <v-carousel-item
        v-for="(slide, i) in slides"
        :key="i"
      >
        <v-sheet :color="colors[i]" height="90%">
          <v-img :src="oblozhka" cover />
        </v-sheet>
      </v-carousel-item>
    </v-carousel>

    <v-container>
      <v-row class="d-flex align-center">
        <v-col cols="auto" class="d-flex align-center">
          <v-img
            :src="logo"
            class="mr-4"
            contain
            height="120"
            width="120"
          />
        </v-col>

        <v-col class="mb-4">
          <h1 class="display-2 font-weight-bold mb-3 text-center">
            ПРАВОВОЕ ОРИЕНТИРОВАНИЕ СТУДЕНТОВ
          </h1>
        </v-col>

        <v-container class="pa-0">
          <v-row justify="center">
            <v-col cols="12" md="8" lg="7">
              <v-expansion-panels class="my-4" variant="popout">
                
                <!-- Стипендии -->
                <v-expansion-panel>
                  <v-expansion-panel-title><strong>Стипендии</strong></v-expansion-panel-title>
                  <v-expansion-panel-text>
                    <v-form>
                      <v-row>
                        <v-col cols="12" v-for="(q, idx) in questionsMoney" :key="idx">
                          <div class="subtitle-1 text-grey mb-2"><em>{{ idx + 1 }}. {{ q }}</em></div>
                          <v-text-field
                            v-model="answers.stipend['q' + (idx + 1)]"
                            :placeholder="getPlaceholder(q)"
                            outlined dense
                          />
                        </v-col>
                      </v-row>
                    </v-form>
                    <v-row>
                      <v-col class="d-flex justify-end">
                        <v-btn 
                          color="primary" 
                          :loading="loading.stipend"
                          @click="submitAnswers('Стипендии', 'stipend')"
                        >Отправить</v-btn>
                      </v-col>
                    </v-row>
                  </v-expansion-panel-text>
                </v-expansion-panel>

                <!-- Образовательный процесс -->
                <v-expansion-panel>
                  <v-expansion-panel-title><strong>Образовательный процесс</strong></v-expansion-panel-title>
                  <v-expansion-panel-text>
                    <v-form>
                      <v-row>
                        <v-col cols="12" v-for="(q, idx) in questionsEducation" :key="idx">
                          <div class="subtitle-1 text-grey mb-2"><em>{{ idx + 1 }}. {{ q }}</em></div>
                          <v-text-field
                            v-model="answers.education['q' + (idx + 1)]"
                            :placeholder="getPlaceholder(q)"
                            outlined dense
                          />
                        </v-col>
                      </v-row>
                    </v-form>
                    <v-row>
                      <v-col class="d-flex justify-end">
                        <v-btn 
                          color="primary"
                          :loading="loading.education"
                          @click="submitAnswers('Образовательный процесс', 'education')"
                        >Отправить</v-btn>
                      </v-col>
                    </v-row>
                  </v-expansion-panel-text>
                </v-expansion-panel>

                <!-- Общежития -->
                <v-expansion-panel>
                  <v-expansion-panel-title><strong>Общежития</strong></v-expansion-panel-title>
                  <v-expansion-panel-text>
                    <v-form>
                      <v-row>
                        <v-col cols="12" v-for="(q, idx) in questionsMoney" :key="idx">
                          <div class="subtitle-1 text-grey mb-2"><em>{{ idx + 1 }}. {{ q }}</em></div>
                          <v-text-field
                            v-model="answers.dormitory['q' + (idx + 1)]"
                            :placeholder="getPlaceholder(q)"
                            outlined dense
                          />
                        </v-col>
                      </v-row>
                    </v-form>
                    <v-row>
                      <v-col class="d-flex justify-end">
                        <v-btn 
                          color="primary"
                          :loading="loading.dormitory"
                          @click="submitAnswers('Общежития', 'dormitory')"
                        >Отправить</v-btn>
                      </v-col>
                    </v-row>
                  </v-expansion-panel-text>
                </v-expansion-panel>

              </v-expansion-panels>
            </v-col>
          </v-row>
        </v-container>
      </v-row>
    </v-container>
  </v-main>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
import { questionsMoney, questionsEducation } from '../mocks/questions'

const API_BASE = 'http://127.0.0.1:8000/test'
const logo = '/RjtFGBm1QW-esNwS5c1Gwi3o9wKpj4R1Hol7cAIgJ6UXYaKCSvcnU7NwpZvits3IX97p8TWEoBzOxL7m5VcpBVrP.png'
const oblozhka = '/oblozhka.jpg'
const colors = ['indigo', 'warning', 'pink darken-2', 'red lighten-1', 'deep-purple accent-4']
const slides = ['First', 'Second', 'Third', 'Fourth', 'Fifth']

interface Answers {
  stipend: Record<string, string>
  education: Record<string, string>
  dormitory: Record<string, string>
}

const answers = reactive<Answers>({
  stipend: {},
  education: {},
  dormitory: {}
})

const loading = reactive({
  stipend: false,
  education: false,
  dormitory: false
})

const getPlaceholder = (question: string): string => {
  return question.includes('ФИО') || question.toLowerCase().includes('фио') 
    ? 'Введите ФИО' 
    : 'Введите ответ'
}

const getQuestionsForSection = (section: string): string[] => {
  if (section === 'Стипендии' || section === 'Общежития') return questionsMoney
  if (section === 'Образовательный процесс') return questionsEducation
  return questionsMoney
}

const getKeyForSection = (section: string): keyof Answers => {
  if (section === 'Стипендии') return 'stipend'
  if (section === 'Общежития') return 'dormitory'
  return 'education'
}

const submitAnswers = async (section: string, answerKey: keyof Answers) => {
  const qs = getQuestionsForSection(section)
  
  const answersObj: Record<string, string> = {}
  qs.forEach((question, idx) => {
    const key = 'q' + (idx + 1)
    answersObj[question] = answers[answerKey][key] ?? ''
  })

  const payload = { section, answers: answersObj }
  loading[answerKey] = true

  try {
    const res = await fetch(`${API_BASE}/submit`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
    
    if (!res.ok) {
      const errData = await res.json().catch(() => ({}))
      throw new Error(errData.detail || `HTTP ${res.status}`)
    }
    
    const data = await res.json()
    Object.keys(answers[answerKey]).forEach(k => { answers[answerKey][k] = '' })
    alert(`✅ Ответы по секции "${section}" отправлены!\nID: ${data.id}`)
    
  } catch (err: any) {
    alert(`❌ Ошибка: ${err.message}`)
    console.error('Submit error:', err)
  } finally {
    loading[answerKey] = false
  }
}
</script>

<style scoped>
.v-main { padding: 0; margin: 0; }
.v-carousel {
  margin: 0;
  width: 100vw !important;
  max-width: 100vw !important;
  position: relative;
  left: calc(50% - 50vw);
  right: calc(50% - 50vw);
}
</style>