# -*- coding: utf-8 -*-
from __future__ import unicode_literals



from django.contrib.auth.decorators import login_required


from django.core.mail import send_mail
from django.conf import settings
#from django.core.mail import EmailMultiAlternatives
from datetime import datetime 


from models import CustomUser, Product
from django.template.loader import render_to_string
# Create your views here.
def sendmensage():

    productList= Product.objects.filter().order_by('-created_date')[:3]
    #productList= Product.objects.filter().order_by('-created_date')
    msg_plain = render_to_string('email.txt', {'productList': productList})
    msg_html = render_to_string('email.html', {'productList': productList})
    
    
    recievers = ['jesusismael_3@hotmail.com']
    for user in CustomUser.objects.all():
        recievers.append(user.email)

    send_mail(
        'News',
        msg_plain,
        settings.EMAIL_HOST_USER,
        recievers, 
        html_message=msg_html,
    )
