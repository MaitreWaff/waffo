from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

from waffo import settings

from profiles.form import ProfileForm, UserForm, SignUpForm, SignInForm

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
def profile(request):
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
    return render(request, 'profiles/viewprofile.html', context_dict)


def login(request):
    next = request.GET.get('next', '/home/')
    # form = UserForm(request.POST)
    if request.method == 'POST':

        form = SignInForm(request.POST, instance=request.user)
        if form.is_valid():
            print "Valid Form"
            username = form.cleaned_data['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                print "User is not None"
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(next)
                else:
                    return HttpResponse("Inactive User.")
            else:
                print "User is None"
                return HttpResponseRedirect(settings.LOGIN_URL)
        else:
            print "Form is not valid."
            print form
            # form = SignInForm()
            return render(request, "registration/login.html", {'form':form, 'redirect_to': next})

    else:
        form = SignInForm()

        return render(request, "registration/login.html", {'form': form, 'redirect_to': next})
        # return render(request, "registration/login.html", {'redirect_to': next})


@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)















