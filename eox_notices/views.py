"""Views for eox_notices."""

from django.contrib.auth.mixins import PermissionRequiredMixin
from nautobot.core.views.generic import (
    BulkDeleteView,
    BulkEditView,
    ObjectDeleteView,
    ObjectEditView,
    ObjectListView,
    ObjectView,
)
from .models import EoxNotice
from .tables import EoxNoticesTable
from .forms import EoxNoticeForm, EoxNoticeBulkEditForm, EoxNoticeFilterForm
from .filters import EoxNoticeFilter


class EoxNoticesListView(PermissionRequiredMixin, ObjectListView):
    """List view."""

    queryset = EoxNotice.objects.prefetch_related("devices", "device_type")
    filterset = EoxNoticeFilter
    filterset_form = EoxNoticeFilterForm
    table = EoxNoticesTable
    permission_required = "eox_notices.view_eoxnotice"
    action_buttons = ("add",)


class EoxNoticeView(PermissionRequiredMixin, ObjectView):
    """Detail view."""

    queryset = EoxNotice.objects.prefetch_related("devices", "device_type")
    permission_required = "eox_notices.view_eoxnotice"


class EoxNoticeCreateView(PermissionRequiredMixin, ObjectEditView):
    """Create view."""

    model = EoxNotice
    queryset = EoxNotice.objects.prefetch_related("devices", "device_type")
    model_form = EoxNoticeForm
    permission_required = "eox_notices.add_eoxnotice"
    default_return_url = "plugins:eox_notices:eoxnotice_list"


class EoxNoticeDeleteView(PermissionRequiredMixin, ObjectDeleteView):
    """Delete view."""

    model = EoxNotice
    queryset = EoxNotice.objects.prefetch_related("devices", "device_type")
    permission_required = "eox_notices.delete_eoxnotice"
    default_return_url = "plugins:eox_notices:eoxnotice_list"


class EoxNoticeEditView(PermissionRequiredMixin, ObjectEditView):
    """Edit view."""

    model = EoxNotice
    queryset = EoxNotice.objects.prefetch_related("devices", "device_type")
    model_form = EoxNoticeForm
    permission_required = "eox_notices.change_eoxnotice"
    default_return_url = "plugins:eox_notices:eoxnotice"


class EoxNoticeBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    """View for deleting one or more EoxNotice records."""

    permission_required = "eox_notices.delete_eoxnotice"
    queryset = EoxNotice.objects.prefetch_related("devices", "device_type")
    table = EoxNoticesTable
    bulk_delete_url = "plugins:eox_notices.eoxnotice_bulk_delete"
    default_return_url = "plugins:eox_notices:eoxnotice_list"


class EoxNoticeBulkEditView(PermissionRequiredMixin, BulkEditView):
    """View for editing one or more EoxNotice records."""

    queryset = EoxNotice.objects.prefetch_related("devices", "device_type")
    filterset = EoxNoticeFilter
    table = EoxNoticesTable
    form = EoxNoticeBulkEditForm
    permission_required = "eox_notices.change_eoxnotice"
    bulk_edit_url = "plugins:eox_notices.eoxnotice_bulk_edit"
