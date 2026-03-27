from .models import Destination_Pages, Items

Destination_Pages.objects.create(
    name='Къща за гости Гайтана',
    location='Широка лъка, Смолян',
    long_description='Къща за гости „Гайтана“ се намира в традиционното родопско село Широка лъка и предлага автентична атмосфера с модерни удобства. Построена в типичен местен стил с камък и дърво, къщата разполага с уютни стаи, просторна механа и красива гледка към планината. Подходяща е както за семейства, така и за групи, които търсят спокойствие и близост до природата., планински гледки и уютна атмосфера.',
    rating=4.9,
    reviews=127,
    num_of_guests=8,
    dollars_per_night=120,
    activities=("Guided hikes in the Rhodope Mountains",
"Visiting local museums and churches",
"Traditional Bulgarian cuisine workshops",
"Bird watching and nature photography"),
    amenities= ("Free Wi-Fi",
"Parking",
"Breakfast included",
"Fireplace",
"Garden",)

)

Destination_Pages.objects.create(
    name='Къщи за гости Лещен',
    location='Лещен, Благоевград',
    long_description='Leshten Guest Homes е комплекс от традиционни къщи за гости, разположени в живописното село Лещен. Къщите съчетават автентична архитектура с модерен комфорт и предлагат панорамни гледки към Родопите. Гостите могат да се насладят на тишина, уютни интериори и просторни дворове, подходящи за релакс.',
    rating=4.8,
    reviews=98,
    num_of_guests=6,
    dollars_per_night=150,
   activities = (
    "Fishing in the local river",
    "Farm tours and animal feeding",
    "Cooking classes with local ingredients",
    "Kayaking on the river",
    "Hiking in the surrounding mountains",
),

amenities = (
    "River access",
    "Organic meals included",
    "Bicycle rental",
    "Fresh produce from the farm",
    "BBQ area",
    "Pet friendly",
)
)

Destination_Pages.objects.create(
    name='Къща за гости Веско и Сузи',
    location='Ковачевица, Благоевград',
    long_description='Vesko & Suzi Guest House предлага автентично преживяване в традиционна каменна къща с модерни удобства. Интериорът е запазен в типичен възрожденски стил, а гостите могат да се насладят на домашна кухня и тиха атмосфера.',
    rating=4.7,
    reviews=89,
    num_of_guests=5,
    dollars_per_night=110,
  activities = (
    "Hiking in the Pirin Mountains",
    "Skiing in winter season",
    "Nature photography tours",
    "Wildlife observation",
    "Traditional village walks",
),

amenities = (
    "Wood burning stove",
    "Fully equipped kitchen",
    "Hot tub",
    "Mountain bike rental",
    "Board games and books",
    "Sauna",
)
)

Destination_Pages.objects.create(
    name='Къща за гости Тишина Гела',
    location='Гела, Смолян',
    long_description='Gela Guest House Silence е малка и уютна къща, разположена сред природата. Тя предлага спокойствие, чист въздух и красива гледка към планинските върхове. Подходяща е за хора, които търсят тишина и релакс далеч от натовареното ежедневие.',
    rating=4.8,
    reviews=104,
    num_of_guests=4,
    dollars_per_night=100,
    activities = (
    "Wine tastings",
    "Vineyard tours",
    "Photography sessions",
    "Picnics in the vineyard",
    "Sunset viewing",
),

amenities = (
    "Cozy cottage accommodation",
    "Outdoor seating area",
    "Fire pit",
    "Wine cellar access",
    "Private vineyard access",
)
)
Destination_Pages.objects.create(
    name='Къща Йовина',
    location='Жеравна, Сливен',
    long_description='Gela Guest House Silence е малка и уютна къща, разположена сред природата. Тя предлага спокойствие, чист въздух и красива гледка към планинските върхове. Подходяща е за хора, които търсят тишина и релакс далеч от натовареното ежедневие.',
    rating=4.9,
    reviews=156,
    num_of_guests=6,
    dollars_per_night=140,
    activities = (
    "Guided village tours in Zheravna",
    "Bird watching in the surrounding nature",
    "Visiting historical sites and museums",
    "Traditional craft workshops",
),

amenities = (
    "Solar-powered electricity",
    "Rainwater harvesting",
    "Compostable toilets",
    "Eco-friendly toiletries",
)
)

Destination_Pages.objects.create(
    name='Еко къща Жеравна',
    location='Жеравна, Сливен',
    long_description='Eco House Zheravna предлага модерно настаняване в екологичен стил, съчетаващ традиционна архитектура и устойчиви материали. Къщата разполага с просторни стаи и зелени площи, идеални за почивка сред природата.',
    rating=4.7,
    reviews=91,
    num_of_guests=4,
    dollars_per_night=115,
    activities = (
    "Farm tours and animal feeding",
    "Organic cooking classes",
    "Kayaking on nearby lakes",
    "Nature photography workshops",
),

amenities = (
    "Eco-friendly accommodations",
    "Solar-powered facilities",
    "Organic meals included",
    "Free Wi-Fi in common areas",
)
)