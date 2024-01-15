from django.shortcuts import render

from .models import Finch

# finches = [
#     {'name': 'Bob', 'description': 'blue and red', 'age': 3},
#     {'name': 'Frank', 'description': 'black and blue', 'age': 2},
#     {'name': 'Carl', 'description': 'gold and silver', 'age': 4},
# ]


# Create your views here.
def home(request):
# Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
# Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'about.html')

def finches_index(request):
    #collect our objects from the db
    finches = Finch.objects.all()

    # for cat in cats:
    #     print(cat)
    # We pass data to a template very much like we did in Express!
    return render(request, 'finches/index.html', {
        'finches': finches
    })
