from django.shortcuts import render
from django.views.generic import TemplateView

class TopView(TemplateView):
    template_name = "pages/index.html"

class CompanyView(TemplateView):
    template_name = "pages/company.html"

class TermsView(TemplateView):
    template_name = "pages/terms.html"