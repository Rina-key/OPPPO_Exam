export interface Activist {
	id: number
	username: string
	name: string
	group: string
	phone: string
	email: string
	birth: string
	education: string
	vk: string
	tg: string
}

export interface ActivistCreate {
	username: string
	password: string
	name?: string
	group?: string
	phone?: string
	email?: string
	birth?: string
	education?: string
	vk?: string
	tg?: string
}