from .models import Tenant

def get_host(request):
    return request.get_host().split(':')[0].lower()

def get_tenant(request):
    hostname = get_host(request)
    print('HOSTNAME',hostname)
    subdomain = hostname.split('.')[0]
    print('SUBDOMAIN',subdomain)
    return Tenant.objects.filter(subdomain=subdomain).first()