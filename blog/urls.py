from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/detail/', views.post_detail, name='detail'),
    path('create/', views.create_post, name='create'),
    path('edit/<int:pk>/', views.edit_post, name='edit'),
    path('delete/<int:pk>/', views.post_delete, name='delete'),
    path('about/', views.about, name='about'),
    path('<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:pk>/share_post/', views.share_post, name='share'),
    path('<category>', views.category_details, name='category'),


]
