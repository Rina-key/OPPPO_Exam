import axios from 'axios'

const API_BASE = 'http://localhost:8000'

// Создаем экземпляр axios с базовыми настройками
export const authApi = axios.create({
	baseURL: API_BASE,
	headers: {
		'Content-Type': 'application/x-www-form-urlencoded',
	},
})

// 🔥 Автоматически добавляем токен ко всем запросам
authApi.interceptors.request.use((config) => {
	const token = localStorage.getItem('token')
	if (token) {
		config.headers.Authorization = `Bearer ${token}`
	}
	return config
})

// Методы API
export const auth = {
	login: async (username: string, password: string) => {
		const formData = new URLSearchParams()
		formData.append('username', username)
		formData.append('password', password)

		const response = await authApi.post('/user/login', formData)
		return response.data
	},

	getCurrentUser: async () => {
		const response = await authApi.get('/user/me')
		return response.data
	},

	logout: () => {
		localStorage.removeItem('token')
	},
}