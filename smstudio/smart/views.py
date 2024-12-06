from django.shortcuts import render, get_object_or_404

from smart.models import *


def index(request):
    context = {
        'title': 'СМАРТ ФОТО',
        'services': Services.objects.filter(cat_id=1),
        'souvenirs': Services.objects.filter(cat_id=2),
        'services_title':'фотоуслуги',
        'souvenirs_title':'фотосувениры',
        'posts': Post.objects.filter(is_published=True),
    }
    return render(request, 'smart/index.html', context=context)


def services(request):
    context = {
        'title': 'ФОТОУСЛУГИ',
        'services': Services.objects.filter(cat_id=1),
    }
    return render(request, 'smart/services.html', context=context)


def souvenirs(request):
    context = {
        'title': 'ФОТОСУВЕНИРЫ',
        'services': Services.objects.filter(cat_id=2),
    }
    return render(request, 'smart/souvenirs.html', context=context)


def show_service(request, service_slug):
    service = get_object_or_404(Services, slug=service_slug)
    context = {
        'show_service': service,
        'title': service.title,
        'services': Services.objects.filter(cat_id=1),
        'souvenirs': Services.objects.filter(cat_id=2),
        'gallery': Gallery.objects.all(),
        'prices': Prices.objects.all(),
        'extracontent': Extra.objects.all(),
    }
    return render(request, 'smart/service_item.html', context=context)

def contacts(request):
    short_phone1 = Nav.objects.get(title='телефон').annotations1.replace(" ", "")
    short_phone2 = Nav.objects.get(title='телефон').annotations2.replace(" ", "")
    context = {
        'contacts_logo': Nav.objects.get(title='логотип'),
        'contacts_map': Nav.objects.get(title='карта или изображение большие'),
        'contacts_mini_map': Nav.objects.get(title='карта или изображение маленькие'),
        'contacts_phone': Nav.objects.get(title='телефон'),
        'contacts_adress': Nav.objects.get(title='адрес'),
        'contacts_mail': Nav.objects.get(title='email'),
        'main_link': Nav.objects.get(title='логотип'),
        'services_link': Nav.objects.get(title='ссылка на фотоуслуги'),
        'souvenirs_link': Nav.objects.get(title='ссылка на фотосувениры'),
        'short_phone1': short_phone1,
        'short_phone2': short_phone2,
        'title': 'КОНТАКТЫ',

    }
    return render(request, 'smart/contacts.html', context=context)
