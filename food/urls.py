from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),  # we mention template name in the class based view
    path('item/', views.items, name='item'),
    path('<int:pk>/', views.DetailClassView.as_view(), name='detail'),
    path('add/', views.CreateItem, name='create_item'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]
