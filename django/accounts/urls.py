from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/', views.detail_or_delete_or_update),
]
