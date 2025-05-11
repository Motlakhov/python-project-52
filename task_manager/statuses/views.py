from django.views.generic import ListView
from task_manager.statuses.models import Status
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from task_manager.mixins import CustomLoginMixin, DeleteProtectionMixin
from task_manager.views import (
    CustomCreateView,
    CustomDeleteView,
    CustomUpdateView,
)
from .forms import StatusForm

# Create your views here.


class BasicStatusView(CustomLoginMixin):
    model = Status
    success_url = reverse_lazy("statuses")


class StatusesListView(BasicStatusView, ListView):
    template_name = "statuses/statuses.html"
    context_object_name = "statuses"


class StatusCreateView(BasicStatusView, CustomCreateView):
    form_class = StatusForm
    success_message = _("Status successfully created")
    extra_context = {
        "header": _("Create status"),
        "button_text": _("Create"),
    }


class StatusUpdateView(BasicStatusView, CustomUpdateView):
    form_class = StatusForm
    success_message = _("Status successfully updated")
    extra_context = {
        "header": _("Update status"),
        "button_text": _("Update"),
    }


class StatusDeleteView(
    BasicStatusView, 
    DeleteProtectionMixin, 
    CustomDeleteView
    ):
    success_message = _("Status successfully delete")
    protected_message = _("Cannot delete a status because it is in use")
    protected_url = reverse_lazy("statuses")
    extra_context = {
        "header": _("Delete status"),
        "button_text": _("Yes, delete"),
    }