from django.shortcuts import render
from django.http import JsonResponse
from .models import Group, City


def index(request):
    if request.is_ajax():
        group_name = request.POST.get('group')
        group = Group.objects.get(name=group_name)
        cities_queryset = City.objects.filter(group__name=group)
        city_list = []
        for city in cities_queryset:
            city_list.append({'city': city.name,
                              'value': city.value})
        return JsonResponse({'result': 'OK', 'data': city_list})

    groups = Group.objects.all()
    context = {'groups': groups}
    return render(request, 'chart/chart.html', context)
