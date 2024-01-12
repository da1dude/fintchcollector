from django.shortcuts import render

finches = [
    {'name': 'Bob', 'description': 'blue and red', 'age': 3},
    {'name': 'Frank', 'description': 'black and blue', 'age': 2},
    {'name': 'Carl', 'description': 'gold and silver', 'age': 4},
]


# Create your views here.
def home(request):
# Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
# Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'about.html')
