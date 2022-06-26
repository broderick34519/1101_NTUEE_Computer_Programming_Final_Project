from django.shortcuts import render

from django.views import generic
# Create your views here.
from .models import Bike, Owner, BikeInstance, Genre

from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_bikes = Bike.objects.all().count()
    num_instances = BikeInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BikeInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_owners = Owner.objects.count()
    
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_bikes': num_bikes,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_owners': num_owners,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BikeListView(generic.ListView):
    model = Bike
    paginate_by = 5
class BikeDetailView(generic.DetailView):
    model = Bike


class LoanedBikesByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing bikes on loan to current user."""
    model = BikeInstance
    template_name ='catalog/bikeinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BikeInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


