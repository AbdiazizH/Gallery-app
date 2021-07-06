from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image,Location,Category


# Create your views here.
def home(request):
    images = Image.objects.all()
    locations =Location.get_locations() 
    return render(request,'all-photos/home.html',{"images":images,"locations":locations})

def locate_image(request,location):
    images = Image.filter_by_location(location)
    return render(request,'all-photos/location.html',{"located_images":images})

def search_results(request):
    if 'search' in request.GET and request.GET["search"]:
        category = request.GET.get("search")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        
        return render(request, 'all-photos/search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'all-photos/search.html', {"message": message})

def catergory(request):

    return render(request, 'all-photos/catergory.html', )


def nature(request):
    
    images = Image.objects.all()
    
    return render(request, 'all-photos/nature.html',{"images":images})

def travel(request):
    images = Image.objects.all()
    locations =Location.get_locations() 
    return render(request, 'all-photos/travel.html',{"images":images})

def animals(request):
    images = Image.objects.all()
    locations =Location.get_locations() 
    return render(request, 'all-photos/animals.html',{"images":images})

def food(request):
    images = Image.objects.all()
    locations =Location.get_locations() 
    return render(request, 'all-photos/food.html',{"images":images})

def work(request):
    images = Image.objects.all()
    locations =Location.get_locations() 
    return render(request, 'all-photos/work.html',{"images":images})