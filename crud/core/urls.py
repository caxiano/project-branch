from django.urls import path
from .views import core_index, core_detail, core_delete

urlpatterns = [
    path('', core_index),
    path('<int:id>/', core_detail),
    path('<int:id>/delete/', core_delete),
]