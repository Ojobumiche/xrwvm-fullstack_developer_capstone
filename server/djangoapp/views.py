# Uncomment the required imports before adding the code
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
import logging


# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

# Create a `login_user` view to handle sign-in requests


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('userName')
            password = data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response_data = {"userName": username,
                                 "status": "Authenticated"}
                return JsonResponse(response_data)
            else:
                response_data = {"userName": username,
                                 "status": "Invalid credentials"}
                return JsonResponse(response_data, status=401)
        except json.JSONDecodeError:
            response_data = {"status": "Invalid JSON"}
            return JsonResponse(response_data, status=400)
    else:
        response_data = {"status": "Only POST requests are allowed"}
        return JsonResponse(response_data, status=405)

# Create a `logout_request` view to handle sign-out requests


@login_required
def logout_request(request):
    logout(request)
    response_data = {"status": "Logged out"}
    return JsonResponse(response_data)

# Create a `login_view` view for handling login via HTML form


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


@csrf_exempt
def registration(request):
    context = {}

    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    username_exist = False
    email_exist = False
    try:
        # Check if user already exists
        User.objects.get(username=username)
        username_exist = True
    except:
        # If not, simply log this is a new user
        logger.debug("{} is new user".format(username))

    # If it is a new user
    if not username_exist:
        # Create user in auth_user table
        user = User.objects.create_user(
            username=username, first_name=first_name, last_name=last_name, password=password, email=email)
        # Login the user and redirect to list page
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
        return JsonResponse(data)
    else:
        data = {"userName": username, "error": "Already Registered"}
        return JsonResponse(data)

# You can include other views for registration, dealer reviews, etc. below
# For example, registration, get_dealerships, get_dealer_reviews, get_dealer_details, add_review
