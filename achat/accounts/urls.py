from django.urls import path
from .views import register_client, dashboard_view, login_view

urlpatterns = [
    path('register/', register_client, name='register_client'),
    path('login/', login_view, name='login'),
        path('admin_dashboard/', dashboard_view, name='admin_dashboard'),
    # Ajoutez la vue pour le tableau de bord client si elle existe
    path('client_dashboard/', dashboard_view, name='client_dashboard'), 
]
