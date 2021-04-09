from django.contrib.auth import login, authenticate,logout
from .forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


class SignupClassView(View):
    def get(self,request):
        form = UserCreationForm()
        return render(request, 'star/signup.html', {'form': form})

    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')


class LoginClassView(View):
    def get(self,request):
        return render(request, 'star/login.html')

    def post(self,request):
        un = request.POST['username']
        ps = request.POST['password']
        user = authenticate(username=un, password=ps)
        if (user is not None):
            login(request, user)
        else:
            return render(request, 'star/login.html', {'error': 'Invalid user'})
        return render(request, 'star/login.html')


class LogoutClassView(View):
    def get(self,request):
        logout(request)
        return render(request, 'star/homepage.html')


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'star/signup.html', {'form': form})


# def login_view(request):
#     if(request.method == 'POST'):
#         un = request.POST['username']
#         ps = request.POST['password']
#         user = authenticate(username=un, password=ps)
#         if(user is not None):
#             login(request, user)
#         else:
#             return render(request, 'star/login.html', {'error':'Invalid user'})
#     return render(request, 'star/login.html')


# def logout_view(request):
#     logout(request)
#     return render(request, 'star/homepage.html')


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'star/passwordreset.html'
    subject_template_name = 'star/password_reset_subject.txt'
    email_template_name = 'star/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'star/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'star/password_reset_confirm.html'
    success_url = reverse_lazy('homepage')
    form_valid_message = "Your password was changed!"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'star/password_reset_complete.html'


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'star/password_change_form.html'
    success_url = reverse_lazy('login')


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'star/password_change_done.html'

