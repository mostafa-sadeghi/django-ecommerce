from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode


def account_register(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            # Setup Email
            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            message = render_to_string('account/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
    else:
        registerForm = RegistrationForm()
        return render(request, 'store/account/registration/register.html', {'form': registerForm})
