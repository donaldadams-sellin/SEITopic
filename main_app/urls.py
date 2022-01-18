from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('tshirts/', views.tshirts_index, name='tshirts_index'),
    path('tshirts/<int:tshirt_id>/', views.tshirts_detail, name='tshirts_detail'),
    path('myimages',views.myimages,name='myimages'),
]