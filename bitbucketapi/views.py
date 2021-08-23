from .forms import RegistrationForm
from django.views import generic
from django.urls import reverse_lazy
from .models import RequestsList, Note
from django.contrib.auth.mixins import LoginRequiredMixin


class RegistrationView(generic.CreateView):
    template_name = "bitbucketapi/registration.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("bitbucketapi:registration")


class RequestsView(LoginRequiredMixin, generic.ListView):
    login_url = "bitbucketapi:login"
    template_name = "bitbucketapi/index.html"
    context_object_name = "requestslist"

    def get_queryset(self):
        x_forwarded_for = self.request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            current_ip = x_forwarded_for.split(",")[-1].strip()
        else:
            current_ip = self.request.META.get("REMOTE_ADDR")

        return RequestsList.objects.filter(ip_user=current_ip).order_by("-id")


class NoteView(LoginRequiredMixin, generic.CreateView):
    login_url = "bitbucketapi:login"
    model = Note
    fields = ("note",)
    template_name = "bitbucketapi/note.html"
    success_url = reverse_lazy("bitbucketapi:note")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["note"] = self.model.objects.filter(
            user_note=self.request.user
        ).order_by("-id")
        return context

    def form_valid(self, form):
        form.instance.user_note = self.request.user
        return super().form_valid(form)
