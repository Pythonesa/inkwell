from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from .models import User


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "users/signup.html"

    def form_valid(self, form):
        valid = super().form_valid(form)
        username = form.cleaned_data.get("username")
        messages.success(self.request, f"¡Usuario {username} creado con éxito!")
        return valid


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserUpdateForm
    template_name = "users/profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user
