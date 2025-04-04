from django.shortcuts import render
from .models import News

# Create your views here.
def news_list_view(request):
    my_news = News.objects.all()
    
    return render(request, 'content/news_list.html', {"news": my_news})
