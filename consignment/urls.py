from django.urls import path

from consignment.views import consignments_list, consignment_details, edit_consignment, delete_consignment, \
    create_consignment

urlpatterns = [
    path('', consignments_list, name='list consignments'),
    path('detail/<int:pk>/', consignment_details, name='consignment details'),
    path('edit/<int:pk>/', edit_consignment, name='edit consignment'),
    path('delete/<int:pk>/', delete_consignment, name='delete consignment'),
    path('create/', create_consignment, name='create consignment'),
]
