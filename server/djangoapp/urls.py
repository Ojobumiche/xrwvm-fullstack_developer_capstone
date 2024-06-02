from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from djangoapp.views import login_user, logout_request, registration
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # path for registration

    # path for login
    path('login', login_user, name='login'),
    path('logout', logout_request, name='logout'),
    path('register', registration, name='register'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
