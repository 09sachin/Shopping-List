from django.urls import path,include
from . import views


urlpatterns = [
    path('add_items',views.add_item),
    path('',views.list_view, name = 'home'),
    path('<id>/update', views.update_view),
    path('<id>/delete', views.delete_view),
]
