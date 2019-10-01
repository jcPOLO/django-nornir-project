from django.shortcuts import render
from .models import Device, ModelType
from django.db.models import Q
from django.http import JsonResponse
from django.core.serializers import serialize


def is_valid_q(q):
    return q != '' and q is not None


def search(request):
    devices = Device.objects.all()
    model_types = ModelType.objects.all()
    hostname_contains_query = request.GET.get('hostname_contains')
    id_exact_query = request.GET.get('id_exact')
    hostname_or_platform_query = request.GET.get('hostname_or_platform')
    ip_address_min = request.GET.get('ip_address_min')
    ip_address_max = request.GET.get('ip_address_max')
    model_type = request.GET.get('model_type')

    if is_valid_q(hostname_contains_query):
        devices = devices.filter(hostname__icontains=hostname_contains_query)
    elif is_valid_q(id_exact_query):
        devices = devices.filter(id__exact=id_exact_query)
    elif is_valid_q(hostname_or_platform_query):
        devices = devices.filter(Q(hostname__icontains=hostname_or_platform_query) | Q(
            platform__name__icontains=hostname_or_platform_query)).distinct()
    if is_valid_q(ip_address_min):
        devices = devices.filter(ip_address__gte=ip_address_min)
    if is_valid_q(ip_address_max):
        devices = devices.filter(ip_address__lte=ip_address_max)
    if is_valid_q(model_type):
        devices = devices.filter(model_types__name=model_type)

    context = {
        'devices': devices,
        'model_types': model_types
    }
    return render(request, 'search.html', context)


def device_models_list(request, id):
    device = Device.objects.get(id=id)
    context = {
        'device': device.ip_address,
        'model': 'anchoas',
        'entity': 'anchoasentiti'
    }
    return JsonResponse(context)


def api_get_device(request, id):
    device = Device.objects.get(id=id)
    context = {
        'hostname': device.hostname,
        'serial': device.serial
    }
    return JsonResponse(context)
