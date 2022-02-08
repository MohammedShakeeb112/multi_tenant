from django.shortcuts import render
from .models import Member
from .utilities import get_tenant

# Create your views here.
def our_team(request):
    tenant = get_tenant(request)
    print('TENANT', tenant)
    members = Member.objects.filter(tenant=tenant)
    print('MEMBERS', members)
    return render(request, 'tenant/our_team.html', {'tenant': tenant, 'members': members})