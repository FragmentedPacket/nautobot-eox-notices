"""Django models for eox_notices plugin."""

from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from nautobot.utilities.querysets import RestrictedQuerySet
from nautobot.extras.models import ChangeLoggedModel
from nautobot.core.models import BaseModel
from nautobot.dcim.models import Device


class EoxNotice(ChangeLoggedModel, BaseModel):
    # Assign permissions to model
    objects = RestrictedQuerySet.as_manager()

    # Set model columns
    devices = models.ManyToManyField(Device)
    device_type = models.ForeignKey(to="dcim.DeviceType", on_delete=models.CASCADE, verbose_name="Device Type")
    end_of_sale = models.DateField(null=True, blank=True, verbose_name="End of Sale")
    end_of_support = models.DateField(null=True, blank=True, verbose_name="End of Support")
    end_of_sw_releases = models.DateField(null=True, blank=True, verbose_name="End of Software Releases")
    end_of_security_patches = models.DateField(null=True, blank=True, verbose_name="End of Security Patches")
    notice_url = models.URLField(blank=True, verbose_name="Notice URL")

    class Meta:
        ordering = ("end_of_support", "end_of_sale")
        constraints = [models.UniqueConstraint(fields=["device_type"], name="unique_device_type")]

    def __str__(self):
        if self.end_of_support:
            msg = f"{self.device_type} - End of support: {self.end_of_support}"
        else:
            msg = f"{self.device_type} - End of sale: {self.end_of_sale}"
        return msg

    def get_absolute_url(self):
        return reverse("plugins:eox_notices:eoxnotice", kwargs={"pk": self.pk})

    def save(self, signal=False):
        # Update the model with related devices that are of the specific device type
        if not signal:
            related_devices = Device.objects.filter(device_type=self.device_type)
            self.devices.add(*related_devices)
        super().save()

    def clean(self):
        super().clean()

        if not self.end_of_sale and not self.end_of_support:
            raise ValidationError(_("End of Sale or End of Support must be specified."))
