from django.urls import path
from appx import views

urlpatterns={
    path('',views.home,name='my_home'),
    path('about/',views.aboutus,name='about_us'),
    path('contact/',views.contactus,name='contact_us')
}