from django.urls import path
from .views import NewsListView, NewsDetailView, HomePageView, ContactPageView, AboutPageView, \
    SoftwareNewsView, WebNewsView, AiNewsView, GameNewsView, TechNewsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/', NewsListView.as_view(), name="all_news_list"),
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='news_detail_page'),
    path('contact/', ContactPageView.as_view(), name='contact_page'),
    path('about/', AboutPageView, name='about_page'),
    path('software-news', SoftwareNewsView.as_view(), name='software_news_page'),
    path('web-news', WebNewsView.as_view(), name='web_news_page'),
    path('ai-news', AiNewsView.as_view(), name='ai_news_page'),
    path('game-news', SoftwareNewsView.as_view(), name='game_news_page'),
    path('tech-news', TechNewsView.as_view(), name='tech_news_page'),

]
























