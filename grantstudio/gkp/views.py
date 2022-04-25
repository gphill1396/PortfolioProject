from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio

def index(request):

    # HOME
    home = Home.objects.latest('updated')

    # ABOUT
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # SKILLS
    categories = Category.objects.all()

    # PORTFOLIO
    portfolios = Portfolio.objects.all()

    context = {
        'home': home,
        'about': about,
        'profile': profiles,
        'categories': categories,
        'portfolios': portfolios,
    }


    
    return render(request, 'index_example.html', context)
