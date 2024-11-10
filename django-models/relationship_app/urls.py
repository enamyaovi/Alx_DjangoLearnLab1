from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

from .views import list_books, LibraryDetailView

urlpatterns = [
    path("relations/", views.bookrelation, name='bookrelation'),
    path('', views.index, name='index'),
    path('listbooks/',views.list_books, name='listbooks'),
    path('librarydetail/<int:pk>/', views.LibraryDetailView.as_view(), name='librarydetailview'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('members/<>', views.MemberView, name='members'),
    path('librarian/', views.LibrarianView, name='librarian'),
    path('adminview/', views.AdminView, name="adminview") 
]
