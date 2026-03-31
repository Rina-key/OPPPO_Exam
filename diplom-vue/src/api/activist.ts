// ✅ Импортируем уже настроенный apiClient с интерсепторами
import apiClient from '@/api/axios'
import type { Activist, ActivistCreate } from '@/types/activist'

export const activistApi = {
	// 🔹 Получение всех активистов (требуется авторизация)
	getAll: async (): Promise<Activist[]> => {
		const { data } = await apiClient.get<Activist[]>('/user/all_user')
		return data
	},

	// 🔹 Получение одного по ID
	getById: async (id: number): Promise<Activist> => {
		const { data } = await apiClient.get<Activist>(`/user/${id}`)
		return data
	},

	// 🔹 Создание нового активиста (только для admin!)
	create: async (data: ActivistCreate): Promise<Activist> => {
		const { data: response } = await apiClient.post<Activist>('/user/', data)
		return response
	},

	// 🔹 Обновление
	update: async (id: number, data: Partial<Activist>): Promise<Activist> => {
		const { data: response } = await apiClient.put<Activist>(`/user/${id}`, data)
		return response
	},

	// 🔹 Удаление
	delete: async (id: number): Promise<void> => {
		await apiClient.delete(`/user/${id}`)
	}
}