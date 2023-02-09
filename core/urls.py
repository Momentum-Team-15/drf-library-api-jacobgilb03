from django.urls import path, include
from . import views
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('books/', views.ListBook.as_view(), name='books_list'),
    path('books/<int:pk>/', views.BookView.as_view(), name='book_detail'),
    path('status/', views.StatusView.as_view(), name='status'),
]

# AWS: SAK: tS78EOI0a+aTbwfet4bUJGjwT7esGX0PLQNcVnFd
# ACCESS KEY ID: AKIAUR6CSIKVUO2E3SUJ
# USER: jacobgilb03