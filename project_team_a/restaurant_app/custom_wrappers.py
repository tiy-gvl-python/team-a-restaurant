from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from functools import wraps
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.exceptions import PermissionDenied
from django.shortcuts import resolve_url
from django.utils.decorators import available_attrs
from django.utils.six.moves.urllib.parse import urlparse
from .models import Item, Category, Menu, Profile
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

# import login_required user_passes_test
# these functions are made to be passed into user_passes_test


staff_wrapper_func = lambda x: x.objects.filter(staff=True)
owner_wrapper_func =lambda x: owner_check(x)
customer_wrapper_func = lambda x: x.objects.filter(customer=True)


def owner_check(x):
    func = lambda x: owner_check(x) #bool(Profile.objects.filter(user=x, owner=True))
    try:
        return Profile.objects.filter(user_id=x.id, owner=True)
    except ObjectDoesNotExist:
        return redirect('restaurant_app:denied')
    except AttributeError:
        return redirect('restaurant_app:denied')
    return False


def user_test(test_func, login_url=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    """

    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            path = request.build_absolute_uri()
            resolved_login_url = resolve_url(login_url or settings.LOGIN_URL)
            # If the login url is the same scheme and net location then just
            # use the path as the "next" url.
            login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
            current_scheme, current_netloc = urlparse(path)[:2]
            if ((not login_scheme or login_scheme == current_scheme) and
                    (not login_netloc or login_netloc == current_netloc)):
                path = request.get_full_path()
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(
                path, resolved_login_url, redirect_field_name)
        return _wrapped_view
    return decorator