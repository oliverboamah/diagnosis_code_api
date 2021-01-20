# Django imports
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/codes/', include('api_v1.urls'))
]
