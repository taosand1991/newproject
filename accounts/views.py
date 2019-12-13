from django.shortcuts import render
from .forms import SignUpForm, ProfileForm,UserEditForm, ProfileEditForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
# Create your views here.


def sign_up(request):
    if request.method == "POST":
        profile_form = ProfileForm(data=request.POST, files=request.FILES)
        form = SignUpForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Your account has been created')
            return redirect('post_list')

    else:
        profile_form = ProfileForm()
        form = SignUpForm()
    return render(request, 'account/sign_up.html', {'form': form, 'profile_form': profile_form})


@login_required
def profile_page(request):
    return render(request, 'account/profile_page.html', {'profiles': request.user})


@login_required
def profile_update(request):
    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=request.user)
        edit_form = ProfileEditForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        if user_form.is_valid()and edit_form.is_valid():
            user_form.save()
            edit_form.save()
            messages.info(request, "Your profile has been updated")
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserEditForm(instance=request.user)
        edit_form = ProfileEditForm(instance=request.user)
    return render(request, 'account/edit.html', {'user_form': user_form, "edit_form": edit_form})


def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password has been changed ")
            return redirect('profile')
        else:
            messages.error(request, "There is a problem changing your password")
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'account/password.html', {'form': form})



            
