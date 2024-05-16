from .forms import ContactForm, UpdateNews, CreateNewsForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.utils.text import slugify
from .models import News, Types
from hitcount.views import HitCountDetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from hitcount.utils import get_hitcount_model


def home(request):
    data = News.objects.filter(status=News.StatusChoices.Publish)[:4]
    trending_news = News.objects.filter(status=News.StatusChoices.Publish)[:2]
    most_popular = News.objects.all()[:5]
    context = {
        'data_news': data,
        'trending_news': trending_news,
        'most_popular': most_popular
    }
    return render(request, 'index.html', context)


# def detail(request, slug):
#     data = get_object_or_404(News, slug=slug)
#     comments = data.comments.all()
#
#     if request.method == 'POST' and request.user.is_authenticated:
#         form = CommentForm(request.POST or None)
#         if form.is_valid():
#             new_comment = form.save(commit=False)
#             new_comment.user = request.user
#             new_comment.news = data
#             new_comment.save()
#     else:
#         form = CommentForm()
#     context = {
#         'data': data,
#         'form': form,
#         'comments': comments
#     }
#     return render(request, 'latest_news.html', context)


class detail(HitCountDetailView,LoginRequiredMixin):
    model = News
    count_hit = True

    def post(self, request, slug):
        data = get_object_or_404(News, slug=slug)
        comments = data.comments.all()
        if request.user.is_authenticated:
            form = CommentForm(request.POST or None)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.user = request.user
                new_comment.news = data
                new_comment.save()
                form = CommentForm()
            context = {
                'data': data,
                'form': form,
                'comments': comments
            }
        else:
            return redirect('login')
        return render(request, 'latest_news.html', context)

    def get(self, request, slug):
        data = get_object_or_404(News, slug=slug)
        comments = data.comments.all()
        form = CommentForm()
        context = {
            'data': data,
            'form': form,
            'comments': comments
        }
        return render(request, 'latest_news.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def get_news_category(request):
    return render(request, 'categori.html', {'data': News.objects.all()[:6], 'types': Types.objects.all()})


def get_absolute_category(request, which_type):
    data = News.objects.filter(type__name=which_type)
    return render(request, 'absolute_category.html', {'types': Types.objects.all(), 'data': data})


def delete_news(request, slug):
    data = get_object_or_404(News, slug=slug)
    data.delete()
    return redirect('home')


def update_news(request, which_news):
    data = get_object_or_404(News, slug=which_news)
    form = UpdateNews(request.POST or None, request.FILES or None, instance=data)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('detail_news', which_news)
    else:
        form = UpdateNews(instance=data)

    return render(request, 'update_news.html', {'form': form, 'data': data})


def create_news(request):
    form = CreateNewsForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        new_item = form.save(commit=False)
        new_item.slug = slugify(new_item.title)
        new_item.save()
        return redirect('home')
    else:
        form = CreateNewsForm()

    context = {
        'form': form
    }

    return render(request, 'create_news.html', context)


def searching_view(request):
    input_data = request.GET.get('searched_for')
    results = News.objects.filter(
        Q(title__icontains=input_data) | Q(body__icontains=input_data)
    )
    return render(request, 'searched.html', {'data': results})

# class searching_view(View):
#     def get(self, request):
#         input_data = request.GET.get('searched_for')
#         data = News.objects.filter(
#             Q(title__icontains=input_data) | Q(body__icontains=input_data)
#         )
#         return render(request, 'searched.html', {'data': data})

# class searching_view(ListView):
#     model = News
#     template_name = 'searched.html'
#     context_object_name = 'data'
#
#     def get_queryset(self):
#         query = self.request.GET.get('searched_for')
#         return News.objects.filter(
#             Q(title__icontains=query) | Q(body__icontains=query)
#         )
# class ContactView(TemplateView):
#     def get(self, request):
#         form = ContactForm()
#         context = {
#             'form': form
#         }
#         return render(request, 'contact.html', context)

#     def post(self, request):
#         form = ContactForm(request.POST)
#         if request.method=='POST' and form.is_valid():
#             form.save()
#             return redirect('home')
#         context = {
#             'form': form
#         }
#         return render(request, 'contact.html', context)

# class HomeView(ListView):
#     model = News
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['data_news'] = self.model.objects.filter(status=News.StatusChoices.Publish)[:3]
#         context['trending_news'] = News.objects.filter(status=News.StatusChoices.Publish)[:2]
#         context['most_popular'] = News.objects.all()[:5]
#         return context
