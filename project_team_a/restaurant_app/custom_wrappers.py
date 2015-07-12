from .models import Profile
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

# import login_required user_passes_test
# these functions are made to be passed into user_passes_test


staff_wrapper_func = lambda x: staff_check(x)
owner_wrapper_func = lambda x: owner_check(x)
customer_wrapper_func = lambda x: customer_check(x)


def owner_check(x):
    try:
        return Profile.objects.filter(user_id=x.id, owner=True)
    except ObjectDoesNotExist:
        return redirect('restaurant_app:denied')
    except AttributeError:
        return redirect('restaurant_app:denied')


def customer_check(x):
    try:
        return Profile.objects.filter(user_id=x.id, Customer=True)
    except ObjectDoesNotExist:
        return redirect('restaurant_app:denied')
    except AttributeError:
        return redirect('restaurant_app:denied')


def staff_check(x):
    try:
        return Profile.objects.filter(user_id=x.id, staff=True)
    except ObjectDoesNotExist:
        return redirect('restaurant_app:denied')
    except AttributeError:
        return redirect('restaurant_app:denied')



'''
from django.contrib.auth.decorators import login_required

@method_decorator(login_required(redirect_field_name='restaurant_app:login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    '''
'''

The above method_decorator setup can be copied and used to require login in
class based views.

        '''