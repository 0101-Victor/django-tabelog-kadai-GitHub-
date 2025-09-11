from django.shortcuts import render

from django.views.generic import TemplateView

class TopView(TemplateView):
    template_name = "pages/index.html"

def company(request):
    return render(request, "pages/company.html")

def terms(request):
    return render(request, "pages/terms.html")
