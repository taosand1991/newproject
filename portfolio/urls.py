from django.urls import path
from portfolio import views

urlpatterns = [

    path('portfolio-create/', views.portfolio_create, name='create'),
    # path('portfolio/', views.index, name='index')

]