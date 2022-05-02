from multiprocessing import get_context
from django.views.generic import View, TemplateView
from datetime import datetime

class Index(TemplateView):
    template_name = 'mainapp/index.html'

class News(TemplateView):
    template_name = 'mainapp/news.html'

    def get_news(self):
        news = [
            'Их было около дюжины человек, солдат, матросов, недавних вчерашних крестьян, голодных, оборванных, у многих измятые гимнастерки, у некоторых простреленная и обгоревшая одежда. У каждого — револьвер в руке, у кого обрез, у других винтовки',
            'Солдаты всем сразу дали винтовки и стали учить стрелять.',
            'К берегам реки приткнула баржу, и около баржи плавало несколько солдат с винтовками.',
            'RuGPT3: Быстрый как ветер», — кричит с берега Михаил, а ему кричат из толпы ребята, рабочие:',
            'Небашев пошел к порту и постоял около портовых огней. На берегу видны были факелы, освещающие вход в порт и дебаркадеры. Н'
        ]
        return news

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context["news_title"] = "Громкий новостной заголовок"
        context[ "news_preview"] = "Предварительное описание, которое заинтересует каждого"
        context["datetime_obj"] = datetime.now()
        context["range"] = self.get_news()
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







