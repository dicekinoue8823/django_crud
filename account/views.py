from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def signup(request):
    form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})
