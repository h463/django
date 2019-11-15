# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from testapp1.models import Company
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
#from django.core.urlresolvers import reverse_lazy
# Create your views here.
class CompanyListView(ListView):
    model = Company
    template_name = "company_list.html"

class CompanyDetailView(DetailView):
    model = Company
    template_name = "company_detail.html"

class CompanyCreateView(CreateView):
    model = Company
    template_name = "company_create.html" # default: company_form.html
    fields = ('name', 'location', 'ceo')

class CompanyUpdateView(UpdateView):
    model = Company
    template_name = "company_create.html"
    fields = ('name', 'ceo')

class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'company_confirm_delete.html'
#    success_url = reverse_lazy("list")