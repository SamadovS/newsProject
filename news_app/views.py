from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import News, Category
from .forms import ContactForm

# def news_list(request):
#     # news_list = News.objects.filter(status=News.Status.Published)
#     news_list = News.published.all()
#     context = {
#         "news_list":news_list
#     }
#     return render(request, "news/news_list.html", context)
#
# def news_detail(request, id):
#     news = get_object_or_404(News, id=id, status=News.Status.Published)
#     context = {
#         "news":news
#     }
#     return render(request, 'news/news_detail.html', context)


class NewsListView(ListView):
    # news_list = News.Published.all()
    model = News
    template_name = "news/news_list.html"
    context_object_name = "news_list"


class NewsDetailView(DetailView):
    # news = get_object_or_404(News, id=id, status=News.Status.Published)
    template_name = "news/news_detail.html"
    context_object_name = "news"

# def HomePageView(request):
#     news_list = News.published.all().order_by('-publish_time')[:7]
#     categories = Category.objects.all()
#     software_last = News.published.filter(category__name='Software').order_by('-publish_time')[:1]
#     software_news = News.published.all().filter(category__name='Software').order_by('-publish_time')[1:6]
#     context = {
#         "news_list" : news_list,
#         "categories" : categories,
#         'software_last' : software_last,
#         "software_news" : software_news,
#
#     }
#     return render(request, "news/home.html", context)

class HomePageView(ListView):
    model = News
    template_name = "news/home.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:4]
        context['software_news'] = News.published.all().filter(category__name='Software').order_by('-publish_time')[:5] #asosiy
        context['aiml_news'] = News.published.all().filter(category__name='AI and Machine Learning').order_by('-publish_time')[:5]
        context['scitech_news'] = News.published.all().filter(category__name='Science and Technologies').order_by('-publish_time')[:5]
        context['intweb_news'] = News.published.all().filter(category__name='Internet and Web').order_by('-publish_time')[:5]
        context['game_news'] = News.published.all().filter(category__name='Gaming').order_by('-publish_time')[:5]
        return context
def AboutPageView(request):
    context = {

    }
    return render(request, 'news/about.html', context)


class ContactPageView(TemplateView):
    template_name = 'news/contact.html'
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form':form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Thank you connecting with us! </h2>")
        context = {
            'form': form
        }

        return render(request, 'news/contact.html', context)













