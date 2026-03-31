import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import EventPage from '@/views/EventPage.vue'
import MyTaskListPage from '@/views/MyTaskListPage.vue'
import ActivListPage from '@/views/ActivListPage.vue'
import KnowledgeBasePage from '@/views/KnowledgeBasePage.vue'
import AnswerPage from '@/views/AnswerPage.vue'

import AuthRoutes from './auth'

const routes: RouteRecordRaw[] = [
	...AuthRoutes,
	{
		path: '/',
		name: 'Home',
		component: HomePage,
	},
	{
		path: '/event',
		name: 'Event',
		component: EventPage,
	},
	{
		path: '/mytask',
		name: 'MyTask',
		component: MyTaskListPage,
	},
	{
		path: '/activ',
		name: 'Activ',
		component: ActivListPage,
	},
	
	{
		path: '/knowledge',
		name: 'KnowledgeBase',
		component: KnowledgeBasePage,
	},
	{
		path: '/answer',
		name: 'AnswerPage',
		component: AnswerPage,
	},
]

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes
})

export default router

