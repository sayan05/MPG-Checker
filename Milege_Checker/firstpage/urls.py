from django.urls import path
from . import views
app_name='firstpage'
urlpatterns = [
    path('', views.index,name="index"),
    path('predictMPG',views.predictMPG,name='predictMPG'),

]