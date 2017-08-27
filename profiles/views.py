from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

from django.views import generic

from waffo import settings

from profiles.form import *
#ProfileForm, UserForm, SignUpForm, SignInForm

# Create your views here.
#
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()  # load the profil instance created by the signal
#             user.profile.bio        = form.cleaned_data.get('bio')
#             user.profile.location   = form.cleaned_data.get('location')
#             user.profile.date_naiss = form.cleaned_data.get('date_naiss')
#             user.save()
#             # username        = form.cleaned_data.get('username')
#             raw_password    = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form    = SignUpForm()
#         return render(request, 'profiles/signup.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username        = form.cleaned_data.get('username')
            raw_password    = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/blog/actualite/')
        else:
            return render(request, 'profiles/signup.html', {'form': form})
    else:
        form    = SignUpForm()
        return render(request, 'profiles/signup.html', {'form': form})

@login_required
def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        print username, password
        return HttpResponseRedirect(settings.LOGIN_URL)
        # return redirect('/blog/actualite/')#render(request, 'registration/login.html')
    form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})






#
#
#
#
# from django.utils.http import is_safe_url
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import never_cache
# from django.views.decorators.csrf import csrf_protect
# from django.views.decorators.debug import sensitive_post_parameters
# from django.views.generic import FormView, RedirectView
#
#
# class LoginView(FormView):
#     """
#     Provides the ability to login as a user with a username and password
#     """
#     success_url = '/blog/actualite/'
#     form_class = AuthenticationForm
#     redirect_field_name = REDIRECT_FIELD_NAME
#
#     template_name = 'registration/login.html'
#
#     @method_decorator(sensitive_post_parameters('password'))
#     @method_decorator(csrf_protect)
#     @method_decorator(never_cache)
#     def dispatch(self, request, *args, **kwargs):
#         # Sets a test cookie to make sure the user has cookies enabled
#         request.session.set_test_cookie()
#
#         return super(LoginView, self).dispatch(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         auth_login(self.request, form.get_user())
#
#         # If the test cookie worked, go ahead and
#         # delete it since its no longer needed
#         if self.request.session.test_cookie_worked():
#             self.request.session.delete_test_cookie()
#
#         return super(LoginView, self).form_valid(form)
#
#     def get_success_url(self):
#         redirect_to = self.request.REQUEST.get(self.redirect_field_name)
#         if not is_safe_url(url=redirect_to, host=self.request.get_host()):
#             redirect_to = self.success_url
#         return redirect_to
#
#
# class LogoutView(RedirectView):
#     """
#     Provides users the ability to logout
#     """
#     url = '/blog/actualite/'
#
#     def get(self, request, *args, **kwargs):
#         auth_logout(request)
#         return super(LogoutView, self).get(request, *args, **kwargs)
#
#





















@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form       = UserForm(request.POST, instance=request.user)
        profile_form    = ProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!', extra_tags='alert')
            return redirect('/waffo/home/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form       = UserForm(instance=request.user)
        profile_form    = ProfileForm(instance=request.user.profile)
    context_dict = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'profiles/profile.html', context_dict)

@login_required
def viewprofile(request):
    if request.method == 'POST':
        user_form       = UserForm(request.POST, instance=request.user)
        profile_form    = ProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!', extra_tags='alert')
            return redirect('/waffo/home/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form       = UserForm(instance=request.user)
        profile_form    = ProfileForm(instance=request.user.profile)
    context_dict = {'user_form': user_form, 'profile_form': profile_form}
    # context_dict = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'profiles/viewprofile.html', context_dict)


@login_required
def profile(request):
    # Fonction de test a supprimer plutard.

    user_form   = ViewProfileForm(instance=request.user)
    profile_form= ProfileForm(instance=request.user)

    context_dict = {'user_form': user_form}
    return render(request, 'profiles/viewprofile.html', context_dict)










@login_required
def viewuserprofile(request, pk):
    prof = Profile.objects.get(pk=pk)

    # blogs = Blog

    context_dict    = {'profile': prof}

    return render(request, 'profiles/viewprofile-base.html', context_dict)
    # return render(request, 'profiles/viewuserprofile.html', context_dict)



class UserProfile(generic.edit.CreateView):
    # model =
    pass









# def userlogin(request):
#     next = request.GET.get('next', '/home/')
#     # form = UserForm(request.POST)
#     if request.method == 'POST':
#
#         form = SignInForm(request.POST, instance=request.user)
#         if form.is_valid():
#             print "Valid Form"
#             username = form.cleaned_data['username']
#             password = request.POST['password']
#
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#                 print "User is not None"
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponseRedirect(next)
#                 else:
#                     return HttpResponse("Inactive User.")
#             else:
#                 print "User is None"
#                 return HttpResponseRedirect(settings.LOGIN_URL)
#         else:
#             print "Form is not valid."
#             print form
#             # form = SignInForm()
#             return render(request, "registration/login.html", {'form':form, 'redirect_to': next})
#
#     else:
#         form = SignInForm()
#
#         return render(request, "registration/login.html", {'form': form, 'redirect_to': next})
#         # return render(request, "registration/login.html", {'redirect_to': next})
#

@login_required
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)


def userhome(request):
    pass

def userregister(request):
    return signup(request)

def userregister_success(request):
    pass












