export interface CardMock {
	id: number
	title: string
	description: string
	image: string
	badge: string
	badgeColor: string
}

export const poolCard1: CardMock = {
	id: 1,
	title: 'Бассейн',
	description: 'Плавай бесплатно! Членам профсоюза — бесплатное посещение университетского бассейна. Забота о здоровье в каждом заплыве',
	image: 'https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?w=600&q=80',
	badge: 'БОНУСЫ',
	badgeColor: '#2650e8'
}

export const poolCard2: CardMock = {
	id: 2,
	title: 'Бесплатная печать',
	description: 'Курсовые, дипломы, постеры — печатай бесплатно! 20 страниц для членов профсоюза в месяц бесплатно. Экономь время и деньги на учёбе',
	image: 'https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=600&q=80',
	badge: 'БОНУСЫ',
	badgeColor: '#2650e8'
}

export const foodCard1: CardMock = {
	id: 3,
	title: 'Материальная помощь',
	description: 'Финансовая поддержка в сложных ситуациях. Дополнительная выплата от профсоюза поверх институтской — мы заботимся о твоем благополучии.',
	image: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=600&q=80',
	badge: 'ДЕНЬГИ',
	badgeColor: '#28e182'
}

export const foodCard2: CardMock = {
	id: 4,
	title: 'Талоны в столовую',
	description: 'Забота о твоем бюджете и здоровье.  на бесплатную кашу и эксклюзивные скидки на обеды в столовых университета.',
	image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=600&q=80',
	badge: 'БОНУСЫ',
	badgeColor: '#2650e8'
}

// === Категория 3: Партнёры СКС РФ ===
export const partnerCard1: CardMock = {
	id: 5,
	title: 'СКС Бонус',
	description: 'Самая масштабная программа лояльности в России. Тысячи скидок на еду, развлечения и шопинг по приложению в твоем смартфоне.',
	image: 'https://images.unsplash.com/photo-1562157873-818bc0726f68?w=600&q=80',
	badge: 'ПАРТНЁР',
	badgeColor: '#8e26e8'
}

export const partnerCard2: CardMock = {
	id: 6,
	title: 'Стипендия активистам',
	description: 'Твоя энергия достойна вознаграждения! Получай повышенную стипендию за вклад в жизнь университета и активную позицию.',
	image: 'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=600&q=80',
	badge: 'ДЕНЬГИ',
	badgeColor: '#28e182'
}

// === Дополнительные бонусы ===
export const bonusCard1: CardMock = {
	id: 7,
	title: 'Стипендия для платников',
	description: 'Учишься на платном, но есть достижения? Снижай финансовую нагрузку! Специальные выплаты для успешных студентов-контрактников.',
	image: 'https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=600&q=80',
	badge: 'ДЕНЬГИ',
	badgeColor: '#28e182'
}

export const bonusCard2: CardMock = {
	id: 8,
	title: 'Портфолио',
	description: 'Организуешь ивенты, участвуешь в проектах, получаешь сертификаты? Мы поможем собрать мощное портфолио, которое откроет двери для самореализации.',
	image: 'https://images.unsplash.com/photo-1523580494863-6f3031224c94?w=600&q=80',
	badge: 'ОПЫТ',
	badgeColor: '#1bb8e8'
}

export const bonusCard3: CardMock = {
	id: 9,
	title: 'Форумы',
	description: 'Бесплатные поездки по всей России. Посещай топовые площадки, заводи полезные знакомства и получай новые знания за счет профсоюза.',
	image: 'https://images.unsplash.com/photo-1523580494863-6f3031224c94?w=600&q=80',
	badge: 'ОПЫТ',
	badgeColor: '#1bb8e8'
}

export const bonusCard4: CardMock = {
	id: 10,
	title: 'Конкурсы',
	description: 'Шанс проявить талант и прославиться.Участвуй в масштабных состязаниях, побеждай и получай ценные призы и сертификаты.',
	image: 'https://images.unsplash.com/photo-1523580494863-6f3031224c94?w=600&q=80',
	badge: 'ОПЫТ',
	badgeColor: '#1bb8e8'
}

export const bonusCard5: CardMock = {
	id: 11,
	title: 'Обучение',
	description: 'Реальные кейсы в организации ивентов. Развивай лидерство, тайм-менеджмент и работу в команде — то, что пригодится в будущем.',
	image: 'https://images.unsplash.com/photo-1523580494863-6f3031224c94?w=600&q=80',
	badge: 'ОПЫТ',
	badgeColor: '#1bb8e8'
}
// ...добавьте остальные карточки по аналогии...

// ✅ Экспортируем всё в одном массиве для удобного использования
export const allBonusCards: CardMock[] = [
	poolCard1,
	poolCard2,
	foodCard1,
	foodCard2,
	partnerCard1,
	partnerCard2,
	bonusCard1,
	bonusCard2,
	bonusCard3,
	bonusCard4,
	bonusCard5,
	// ...остальные
]