export default [
	{
		path: '/register',
		name: 'Register',
		component: () => import('@/views/Auth/RegisterPage.vue'),
	},
	{
		path: '/entrance',
		name: 'Entrance',
		component: () => import('@/views/Auth/EntrancePage.vue'),
	},
]