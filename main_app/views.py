from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic import ListView
from django.views.generic.detail import DetailView


from .models import Finch, Toy
from .forms import FeedingForm

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

#detail view - shows 1 finch at '/finches/:id'
def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    #find one finch wiht its id
    id_list = finch.toys.all().values_list('id')
    # Now we can query for toys whose ids are not in the list using exclude
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch, 'feeding_form': feeding_form,
        # Add the toys to be displayed
        'toys': toys_finch_doesnt_have
    })

class FinchCreate(CreateView):
    model = Finch
    # fields = '__all__'
    # fields = ['name', 'breed', 'description', 'age']
    success_url = '/finches'
    fields = ['name', 'breed', 'description', 'age']

class FinchUpdate(UpdateView):
    model = Finch
    # Let's disallow the renaming of a finch by excluding the name field!
    fields = ['name', 'breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

def add_feeding(request, finch_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the finch_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

#List of Toy Views here

#ToyList
class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'

#Toy Detail
class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'

#Toy Create
class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']

    def form_valid(self, form):
        return super().form_valid(form)
    
#Toy Update
class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

#Toy Delete
class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys.html'

#add and remove toys from finches
def assoc_toy(request, finch_id, toy_id):
    #we target the finch and pass it a toy id
    Finch.objects.get(id=finch_id).toys.add(toy_id)

    return redirect('detail', finch_id=finch_id)

def unassoc_toy(request, finch_id, toy_id):
    #we target the finch and pass it a toy id
    Finch.objects.get(id=finch_id).toys.remove(toy_id)

    return redirect('detail', finch_id=finch_id)