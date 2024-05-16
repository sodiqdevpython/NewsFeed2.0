from .models import News

def get_latest_news(request):
    latest_news = News.objects.all().order_by('-id')[:4]
    context = {
        'latest_news': latest_news
    }

    return context