from django.urls import path
from .views import NewsListView, NewsDetailView, HomePageView, ContactPageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/', NewsListView.as_view(), name="all_news_list"),
    path('news<int:id>/', NewsDetailView.as_view(), name='news_detail_page'),
    path('contact/', ContactPageView.as_view(), name='contact_page'),
    path('about/', AboutPageView, name='about_page'),
]
























