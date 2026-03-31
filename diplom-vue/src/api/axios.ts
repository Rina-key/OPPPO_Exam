import axios from 'axios'

const API_BASE = 'http://localhost:8000'

export const apiClient = axios.create({
	baseURL: API_BASE,
})

// Автоматически добавляем токен
apiClient.interceptors.request.use((config) => {
	const token = localStorage.getItem('token')
	const tokenType = localStorage.getItem('token_type') || 'bearer'

	if (token) {
		config.headers.Authorization = `${tokenType} ${token}`
	}

	return config
})

// Обработка ошибок авторизации
apiClient.interceptors.response.use(
	(response) => response,
	(error) => {
		if (error.response?.status === 401) {
			// Токен истек — очищаем и редиректим на логин
			localStorage.removeItem('token')
			localStorage.removeItem('token_type')
			window.location.href = '/login'
		}
		return Promise.reject(error)
	}
)

export default apiClient