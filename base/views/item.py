from django.shortcuts import render
from django.views.generic import ListView
from base.models import Item # トップページにアイテム一覧を表示するために設定


class IndexListView(ListView):
    model = Item # djangoがアイテムモデルの一覧からデータをもってきてくれる設定
    template_name = 'pages/index.html' # どのテンプレとを返していくのかを記載

def index(request):
    object_list = Item.object.all()
    context = {
        'object_list': object_list,
    }
    return render(request, 'pages/index.html', context)