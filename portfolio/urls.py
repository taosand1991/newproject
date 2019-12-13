from django.urls import path
from portfolio import views

app_name = 'portfolio'

urlpatterns = [

    path('portfolio-create/', views.portfolio_create, name='create-port'),
    path('portfolio-list/', views.portfolio_list, name='port-list'),
    path('portfolio-update/<int:pk>', views.update_list, name='port-update'),
    path('/<int:pk>/portfolio-detail/', views.portfolio_detail, name='port-detail'),

]