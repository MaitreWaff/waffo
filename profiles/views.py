from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect

from profiles.form import ProfileForm, UserForm

# Create your views here.

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form       = UserForm(request.POST, instance=request.user)
        profile_form    = ProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form       = UserForm(instance=request.user)
        profile_form    = ProfileForm(instance=request.user.profile)
    context_dict = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'profiles/profile.html', context_dict)


















