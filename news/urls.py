from django.urls import path
# from .views import HomeView
from .views import home, detail, contact, get_news_category, get_absolute_category, delete_news, update_news, create_news, searching_view

urlpatterns = [
    path('', home, name='home'),
    path('news/<str:slug>/', detail.as_view(), name='detail_news'),
    path('contact/', contact, name='contact'),
    path('category/', get_news_category, name='category'),
    path('category/<str:which_type>/', get_absolute_category, name='category_detail'),
    path('news/<str:slug>/delete/', delete_news, name='delete_news'),
    path('news/<str:which_news>/update/', update_news, name='edit_news'),
    path('create/news/', create_news, name='create'),
    path('searched/', searching_view, name='search')
]