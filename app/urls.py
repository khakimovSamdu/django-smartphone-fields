from .views import get_all, get_id, get_add, get_id_update, get_id_delete
from django.urls import path
urlpatterns = [
    path('all/', get_all),
    path('id/<int:id>/', get_id),
    path('add/', get_add),
    path('update/<int:id>/', get_id_update),
    path('delete/<int:id>/', get_id_delete)
]