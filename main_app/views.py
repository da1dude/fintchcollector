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

    # for finch in finches:
    #     print(finch)
    # We pass data to a template very much like we did in Express!
    return render(request, 'finches/index.html', {
        'finches': finches
    })

#detail view - shows 1 cat at '/cats/:id'
def finches_detail(request, finch_id):
    #find one cat wiht its id
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', { 'finch': finch })