# from django.contrib.auth.decorators import login_required, user_passes_test
# import login_required user_passes_test
# these functions are made to be passed into user_passes_test
staff_wrapper_func = lambda x: x.objects.filter(staff=True)
owner_wrapper_func = lambda x: x.objects.filter(owner=True)
customer_wrapper_func = lambda x: x.objects.filter(customer=True)