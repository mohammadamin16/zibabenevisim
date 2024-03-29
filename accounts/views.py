from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import FileResponse
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, FormView, DetailView, UpdateView
from django.contrib.auth import get_user_model

from accounts.forms import SignUpForm


class Login(LoginView):
    template_name = 'accounts/login.html'

    def get_redirect_url(self):
        return reverse('home-page')

    def get_success_url(self):
        return reverse('home-page')

    def form_valid(self, form):
        return super().form_valid(form)


class Logout(LogoutView):
    def get_next_page(self):
        return reverse('home-page')


class SignUp(FormView):
    form_class = SignUpForm
    fields = ['phone', 'username', 'password', 'display_name']
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        form.save_user()
        return super(SignUp, self).form_valid(form)

    def get_success_url(self):
        return reverse('accounts:login')

#
# class Profile(DetailView):
#     model = get_user_model()
#     context_object_name = 'object'
#     template_name = 'accounts/profile.html'
#
#     def get_object(self, queryset=None):
#         return get_user_model().objects.get(username=self.kwargs['username'])
#
#
# def get_avatar(self, username):
#     user = get_user_model().objects.get(username=username)
#     img = user.avatar.url
#     return FileResponse(open(img, 'rb'))
#
#
# class EditProfile(UpdateView):
#     model = get_user_model()
#     fields = ['display_name', 'avatar', 'bio']
#     template_name = 'accounts/edit_profile.html'
#
#     def get_object(self, queryset=None):
#         return get_user_model().objects.get(username=self.kwargs['username'])
#
#
# class Panel(DetailView):
#     model = get_user_model()
#     template_name = 'accounts/panel.html'
#
#     def get_object(self, queryset=None):
#         user = get_user_model().objects.get(username=self.kwargs['username'])
#         return user
#
#     def get_context_data(self, **kwargs):
#         context = super(Panel, self).get_context_data(**kwargs)
#         words = self.request.user.words.all()
#         quizzes = self.request.user.quizzes.all()
#         context['words'] = words
#         context['quizzes'] = quizzes
#         return context
