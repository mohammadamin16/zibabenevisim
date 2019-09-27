from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<pk>', views.BookView.as_view(), name='book-view'),
    path('order/', views.OrderView.as_view(), name='order'),
]
