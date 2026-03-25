"""
URL configuration for projectx project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('appx.urls')),
    path('services/',include('appx.urls')),
        path('services/about/gallery/',include('appx.urls')),
        path('services/contact/about/',include('appx.urls')),
        path('services/gallery/contact/',include('appx.urls')),
    path('gallery/',include('appx.urls')),
        path('gallery/services/about/',include('appx.urls')),
        path('gallery/about/contact/',include('appx.urls')),
        path('gallery/contact/services/',include('appx.urls')),
    path('contact/',include('appx.urls')),
        path('contact/about/gallery/',include('appx.urls')),
        path('contact/gallery/services/',include('appx.urls')),
        path('contact/services/about/',include('appx.urls')),
    path('about/',include('appx.urls')),
        path('about/gallery/services/',include('appx.urls')),
        path('about/contact/gallery/',include('appx.urls')),
        path('about/services/contact/',include('appx.urls')),
        
    
]
