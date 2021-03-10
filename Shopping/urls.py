from django.urls import path,include
from . import views


urlpatterns = [
    path('add_items',views.add_item),
    path('',views.list_view, name = 'home'),
    path('<person>/<slug:item_name>/<id>/update', views.update_view,name = 'update'),
    path('<person>/<slug:item_name>/<id>/delete', views.delete_view, name='delete'),
]
