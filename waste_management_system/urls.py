# mywebsite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]
# myapp/urls.py
from django.urls import path
from waste.views import chatbot_view

urlpatterns = [
    path('', chatbot_view, name='chatbot_view'),
]
