from homepage_response.models import List_destinations, Items
List_destinations.objects.create(
        name= 'Mountain View Eco Lodge',
        location= 'Northern Mountains',
        short_description= 'Sustainsible eco-lodge with panoramic mountain views and modern amenities',
        rating= 4.9,
        reviews= 127,
        num_of_guests=4,
        dollars_per_night= 120
    )
List_destinations.objects.create(
        name= 'Riverside Farm Stay',
        location= 'Valley Region',
        short_description= 'Enjoy authentic farm life by the river with organic farming experiences.',
        rating= 4.7,
        reviews= 89,
        num_of_guests= 6,
        dollars_per_night= 85
    )
List_destinations.objects.create(name= 'Alpine Cabin Retreat',
        location= 'Alpine District',
        short_description= 'Cozy wooden cabin in the Alps, ideal for a peaceful mountain getaway.',
        rating= 4.8,
        reviews= 156,
        num_of_guests= 5,
        dollars_per_night= 150
        )
List_destinations.objects.create(
        name= 'Forest Treehouse Haven',
        location= 'Woodland Area',
        short_description= 'Unique treehouse stay nestled high in the forest canopy.',
        rating= 4.9,
        reviews= 201,
        num_of_guests=2,
        dollars_per_night= 135
    )
List_destinations.objects.create(name= 'Sunset Vineyard Cottage',
        location = 'Wine Country',
        short_description= 'Charming cottage set among vineyards with wine tasting experiences.',
        rating= 4.6,
        reviews= 73,
        num_of_guests= 4,
        dollars_per_night= 95
    )
List_destinations.objects.create(
        name= 'Lakeside Organic Farm',
        location= 'Lake District',
        short_description= 'Organic farm stay with scenic lake views and water-based activities.',
        rating= 4.8,
        reviews= 142,
        num_of_guests= 8,
        dollars_per_night= 100
    )




