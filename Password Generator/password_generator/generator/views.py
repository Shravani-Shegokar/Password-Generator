
from django.shortcuts import render
import random
import string

def home(request):
    return render(request, 'generator/home.html')

def generate_password(request):
    length = int(request.GET.get('length', 12))  # Default length is 12
    include_uppercase = request.GET.get('uppercase')
    include_numbers = request.GET.get('numbers')
    include_special = request.GET.get('special')

    # Lowercase letters by default
    characters = list(string.ascii_lowercase)

    if include_uppercase:
        characters.extend(list(string.ascii_uppercase))

    if include_numbers:
        characters.extend(list(string.digits))

    if include_special:
        characters.extend(list(string.punctuation))

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))

    return render(request, 'generator/password.html', {'password': password})
