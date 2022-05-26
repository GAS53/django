from multiprocessing import get_context
from django.views.generic import View, TemplateView
from mainapp import models as mainapp_models
from django.shortcuts import get_object_or_404

class Index(TemplateView):
    template_name = 'mainapp/index.html'

class News(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news_qs"] = mainapp_models.News.objects.all()[:5]
        return context

class News_full_view(TemplateView):
    template_name = "mainapp/news_detail.html"
    
    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context["news_object"] = get_object_or_404(mainapp_models.News, pk=pk)
        return context



class NewsWithPaginatorView(News):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context["page_num"] = page
        return context



class Contacts(TemplateView):
    template_name = 'mainapp/contacts.html'

class Courses(TemplateView):
    template_name = 'mainapp/courses_list.html'

class Doc(TemplateView):
    template_name = 'mainapp/doc_site.html'

class Login(TemplateView):
    template_name = 'mainapp/login.html'







