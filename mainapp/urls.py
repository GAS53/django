from argparse import Namespace
from django.urls import path
from mainapp import views
from django.views.generic import RedirectView
from mainapp.apps import MainappConfig

app_name = MainappConfig.name


urlpatterns = [
    path("", views.Index.as_view(), name="main_page"),
    path("news/", views.News.as_view(), name="news"),
    path("news/<int:page>/", views.NewsWithPaginatorView.as_view(), name="news_paginator"),

    path("courses/", views.Courses.as_view(), name="courses"),
    path("contacts/", views.Contacts.as_view(), name="contacts"),
    path("doc_site/", views.Doc.as_view(), name="doc_site"),
    path("login/", views.Login.as_view(), name="login"),
]