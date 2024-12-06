from smart.models import *
from django import template

register = template.Library()


@register.inclusion_tag('smart/navigation.html')
def show_navigaition():
        navlogo = Nav.objects.get(title='логотип')
        servicesIcon = Nav.objects.get(title='ссылка на фотоуслуги')
        souvenirsIcon = Nav.objects.get(title='ссылка на фотосувениры')
        adressIcon = Nav.objects.get(title='адрес')
        phoneIcon = Nav.objects.get(title='телефон')
        return {'navlogo': navlogo,
                'servicesIcon': servicesIcon,
                'souvenirsIcon': souvenirsIcon,
                'adressIcon': adressIcon,
                'phoneIcon': phoneIcon,
                }


@register.inclusion_tag('smart/mini_navigation.html')
def show_mini_navigation():
        navlogo = Nav.objects.get(title='логотип')
        servicesIcon = Nav.objects.get(title='ссылка на фотоуслуги')
        suvenirsIcon = Nav.objects.get(title='ссылка на фотосувениры')
        adressIcon = Nav.objects.get(title='адрес')
        phoneIcon = Nav.objects.get(title='телефон')
        return {'navlogo': navlogo,
                'servicesIcon': servicesIcon,
                'souvenirsIcon': suvenirsIcon,
                'adressIcon': adressIcon,
                'phoneIcon': phoneIcon,
                }

