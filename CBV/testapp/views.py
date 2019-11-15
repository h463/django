# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView
from .models import Book
# Create your views here.

# NORMAL VIEW
#class HelloView(View):
#   def get(self,request):
#        return HttpResponse("Hello world")

#TEMPLATEVIEW
#class HelloTemplateView(TemplateView):
#    template_name = "base.html"

#TEMPLATECONTEXT
class HelloTemplateView(TemplateView):
     template_name = "base.html"
     def get_context_data(self, **kwargs):
         context=super(HelloTemplateView, self).get_context_data(**kwargs)
         context['name'] = "haritha"
         context['subject'] = 'python'
         context['marks'] = 100
         return context

#BY USING FUNCTION BASED VIEWS
def info_view(request):
    books = Book.objects.all()
    return render (request, "base,html", {"books": books})

#BY USING CLASS BAED VIEWS(LISTVIEW)
class BookListView(ListView):
    template_name = "base.html" # to customise own template
    context_object_name = "book_list" # to customise own context object
    model = Book
     #default templete: "book_list.html"
     #default context object: "book_list"

class BookDetailView(DetailView):
    model = Book
    template_name = "detail.html"  # to customise own template
    context_object_name = "book"  # to customise own context object
    # default template: "book_detail.html"
    # default context object: "book" or "object"