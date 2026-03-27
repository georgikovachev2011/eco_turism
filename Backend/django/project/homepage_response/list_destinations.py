from homepage_response.models import List_destinations, Items


List_destinations.objects.create(
    name='Къща за гости Гайтана',
    location='Широка лъка, Смолян',
    short_description='Традиционна родопска къща за гости с каменна и дървена архитектура, планински гледки и уютна атмосфера.',
    rating=4.9,
    reviews=127,
    num_of_guests=8,
    dollars_per_night=120
)

List_destinations.objects.create(
    name='Къщи за гости Лещен',
    location='Лещен, Благоевград',
    short_description='Панорамни традиционни къщи с автентична архитектура, спокойна обстановка и красива планинска природа.',
    rating=4.8,
    reviews=98,
    num_of_guests=6,
    dollars_per_night=150
)

List_destinations.objects.create(
    name='Къща за гости Веско и Сузи',
    location='Ковачевица, Благоевград',
    short_description='Автентична каменна къща с топъл интериор, местен характер и тиха обстановка, идеална за любителите на природата.',
    rating=4.7,
    reviews=89,
    num_of_guests=5,
    dollars_per_night=110
)

List_destinations.objects.create(
    name='Къща за гости Тишина Гела',
    location='Гела, Смолян',
    short_description='Спокойно планинско убежище, заобиколено от природа, чист въздух и широки гледки към Родопите.',
    rating=4.8,
    reviews=104,
    num_of_guests=4,
    dollars_per_night=100
)

List_destinations.objects.create(
    name='Къща Йовина',
    location='Жеравна, Сливен',
    short_description='Очарователна възрожденска къща с дървен интериор, уютен двор и незабравима историческа атмосфера.',
    rating=4.9,
    reviews=156,
    num_of_guests=6,
    dollars_per_night=140
)

List_destinations.objects.create(
    name='Еко къща Жеравна',
    location='Жеравна, Сливен',
    short_description='Еко стил на настаняване, съчетаващ традиционен дизайн, зелени външни пространства и спокойна селска обстановка.',
    rating=4.7,
    reviews=91,
    num_of_guests=4,
    dollars_per_night=115
)