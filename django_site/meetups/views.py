from django.shortcuts import render


# Create your views here.

def index(request):
    meetups = [
        {
            'title': 'A First Meetup',
            'locations': 'New York, NY',
            'slug': 'a-first-meetup'
        },
        {
            'title': 'A Second Meetup',
            'locations': 'Paris',
            'slug': 'a-second-meetup'
        }
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': False,
        'meetups':meetups
        })