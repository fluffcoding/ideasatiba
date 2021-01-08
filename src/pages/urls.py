from django.urls import path
from .views import front_page, post_page, search_results

urlpatterns = [
    path('front/', front_page, name='front'),
    path('post/', post_page, name='post'),
    path('search/', search_results, name='search')
]