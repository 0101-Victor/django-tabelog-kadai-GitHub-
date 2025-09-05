# base/views/item.py
from django.shortcuts import render, get_object_or_404
from base.models.item import Store

def store_list(request):
    stores = Store.objects.all()
    return render(request, "pages/stores.html", {"stores": stores})

def store_detail(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    return render(request, "pages/store_detail.html", {"store": store})
