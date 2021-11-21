from django.urls import path
from crm_app import views
app_name = 'crm_app'


urlpatterns = [
    path('', views.login, name="login"),
    path('index/', views.index, name="index"),
    path('clients/', views.clients, name="clients"),
    path('companies/', views.companies, name="companies"),
    path('add-companie/', views.add_company, name="add_company"),
    path('add-clients/', views.add_clients, name="add_clients"),
    path('delete-client/<int:client_id>', views.delete_client, name="delete_client"),
    path('update-clients/<int:client_id>', views.edit_client, name="edit_client"),
    
    
]