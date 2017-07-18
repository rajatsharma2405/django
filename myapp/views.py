# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime
# Create your views here.


def signup_view(request):
    today = datetime.now()
    return render(request, 'index.html', {'today': today})
