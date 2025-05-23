from django.views.generic import ListView
from task_manager.labels.models import Label
from .forms import LabelForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from task_manager.mixins import CustomLoginMixin, DeleteProtectionMixin
from task_manager.views import (
    CustomCreateView,
    CustomDeleteView,
    CustomUpdateView,
)

# Create your views here.


class LabelsListView(CustomLoginMixin, ListView):
    model = Label
    template_name = "labels/labels.html"
    context_object_name = "labels"


class LabelCreateView(CustomLoginMixin, CustomCreateView):
    model = Label
    form_class = LabelForm
    success_message = _("Label is successfully created")
    success_url = reverse_lazy("labels")
    extra_context = {
        "header": _("Create label"),
        "button_text": _("Create"),
    }


class LabelUpdateView(CustomLoginMixin, CustomUpdateView):
    model = Label
    form_class = LabelForm
    success_message = _("Label is successfully updated")
    success_url = reverse_lazy("labels")
    extra_context = {
        "header": _("Update label"),
        "button_text": _("Update"),
    }


class LabelDeleteView(
    CustomLoginMixin, 
    DeleteProtectionMixin, 
    CustomDeleteView
    ):
    model = Label
    success_message = _("Label is successfully delete")
    success_url = reverse_lazy("labels")
    protected_message = _("Cannot delete a label because it is in use")
    protected_url = reverse_lazy("labels")
    extra_context = {
        "header": _("Delete label"),
        "button_text": _("Yes, delete"),
    }