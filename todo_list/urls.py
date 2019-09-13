from django.urls import path
from .views import home, delete, cross_off, uncross, edit
urlpatterns = [

    path('', home, name='home'),
    path('delete/<item_id>', delete, name='delete'),
    path('cross_off/<item_id>', cross_off, name='cross_off'),
    path('uncross/<item_id>', uncross, name='uncross'),
    path('edit/<item_id>', edit, name='edit')
]