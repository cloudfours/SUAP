from django import  template
from django.contrib.auth.models import Group
from django.template.defaultfilters import register
register=template.Library()
@register.filter(name='has_group')
def  has_group(user,group_name):
    try:
      
           grupo=Group.objects.filter(name=group_name).exists()
       
    except Group.DoesNotExist:
        return False
    return  grupo in user.groups.all()
