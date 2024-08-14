from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "users/signup.html"

    def form_valid(self, form):
        valid = super().form_valid(form)
        username = form.cleaned_data.get("username")
        messages.success(self.request, f"¡Usuario {username} creado con éxito!")
        return valid
