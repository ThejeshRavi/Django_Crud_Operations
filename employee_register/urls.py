from django.urls import path, include
from .import views 

urlpatterns = [
    path('', views.employee_form, name = 'employee_insert'), # GET and POST Request for insert operation
    path('delete/<int:id>',views.employee_delete, name ='employee_delete'),#delete request for delete operation
    path('<int:id>/', views.employee_form,name='employee_update'), #GET and POST Request for update Operation
    path('list/',views.employee_list, name = 'employee_list')# GET request to retrieve and display all records
    
]
