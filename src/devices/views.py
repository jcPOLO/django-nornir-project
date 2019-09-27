from django.shortcuts import render
from .models import Device, ModelType
from django.db.models import Q


def is_valid_q(q):
    return q != '' and q is not None


def search(request):
    qs = Device.objects.all()
    model_types = ModelType.objects.all()
    hostname_contains_query = request.GET.get('hostname_contains')
    id_exact_query = request.GET.get('id_exact')
    hostname_or_platform_query = request.GET.get('hostname_or_platform')
    ip_address_min = request.GET.get('ip_address_min')
    ip_address_max = request.GET.get('ip_address_max')
    model_type = request.GET.get('model_type')

    if is_valid_q(hostname_contains_query):
        qs = qs.filter(hostname__icontains=hostname_contains_query)
    elif is_valid_q(id_exact_query):
        qs = qs.filter(id__exact=id_exact_query)
    elif is_valid_q(hostname_or_platform_query):
        qs = qs.filter(Q(hostname__icontains=hostname_or_platform_query)
                       | Q(platform__name__icontains=hostname_or_platform_query)
                       ).distinct()
    if is_valid_q(ip_address_min):
        qs = qs.filter(ip_address__gte=ip_address_min)

    if is_valid_q(ip_address_max):
        qs = qs.filter(ip_address__lte=ip_address_max)

    if is_valid_q(model_type):
        qs = qs.filter(model_types__name=model_type)

    context = {
        'queryset': qs,
        'model_types': model_types
    }
    return render(request, 'search.html', context)
