from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser, Review

"""
Admin configuration for the Library app.

This module customizes the admin interface for managing books, reviews, 
and the custom user model.
"""

# Admin configuration for the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Book model.

    Features:
        - Displays title, author, and publication year in the admin list view.
        - Allows searching by title, author, and publication year.
        - Filters the list view by title, author, and publication year.
    """
    list_display = ("title", "author", "publication_year")
    search_fields = ["title", "author", "publication_year"]
    list_filter = ("title", "author", "publication_year")

# Admin configuration for the Review model
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Review model.

    Features:
        - Displays book, user, and review text in the admin list view.
    """
    list_display = ["book", "user", "review_text"]

# Register the custom user model with the default UserAdmin
admin.site.register(CustomUser, UserAdmin)
