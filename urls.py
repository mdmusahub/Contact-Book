from django.urls import path
from . import views

urlpatterns = [
    path('contactinfo/',views.contactinfo),
    path('addcontact/',views.addcontact),
    path('updatecontact/',views.updatecontact),
    path('deletecontact/',views.deletecontact),
    path('viewallcontact/',views.viewallcontact)
]