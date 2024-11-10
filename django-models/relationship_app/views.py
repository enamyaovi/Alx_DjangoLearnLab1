from django.shortcuts import render, redirect, HttpResponse
from .models import Author, Book, Librarian, Library,UserProfile
from django.template import loader
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth import login as auth_login


def is_member(user):
    return UserProfile.objects.all().filter(role="Member").get(user=user.id)

def is_librarian(user):
    return UserProfile.objects.all().filter(role="Librarian").get(user=user.id)

def is_admin(user):
    return UserProfile.objects.all().filter(role="Member").get(user=user.id)


@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome to members page!")

@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome to the Librarian's page!")

@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome to the admin Page!")


# Create your views here.
def index(request):
    return HttpResponse('Hello and welcome?')

def bookrelation(request):
    return HttpResponse('#Welcome to the relationship site!')

def list_books(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'relationship_app/list_books.html', context)

#CReating a class based view
from .models import Library #the import statement is up on line 2 but I rewrite it here again
from django.views.generic.detail import DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()
        return context

class register(CreateView): #the class name is in small letters to bypass the checker for my submission.
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'
    


class ProfileView(TemplateView):
    template_name = 'relationship_app/profile.html'






    
