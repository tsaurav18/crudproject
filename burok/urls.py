
from django.contrib import admin
from django.urls import path,include
import viewcrud.views
import accounts.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewcrud.views.welcome, name="welcome"),
    path('funcrud/',include('viewcrud.urls')),
    path('accounts/', include('accounts.urls')),
]
