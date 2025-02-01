from django.urls import path
from . import views
# from . models import User

urlpatterns = [
    path('info', views.info, name='info-detail')
    

]