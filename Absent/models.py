from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from sisdatasources.models import Student


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Absent(models.Model):

    """
    This model will be used by the student to requst for absence.
    """

    student_id = models.ManyToManyField(
        'sisdatasources.Student',
        related_query_name='Student',
        blank=False,
    )

    absentreason = models.CharField(
        _('Absent Reason'),
        max_length=255,
        null=False,
        blank=False
    )

    absentfrom = models.DateField(
        _('Absent From'),
        max_length=30,
        null=False,
        blank=False
    )

    absentto = models.DateField(
        _('Absent Till'),
        max_length=30,
        null=False,
        blank=False
    )

    absentphoto = models.ImageField(
        _('Absent Picture'),
        max_length=255,
        null=True,
        blank=True,
        upload_to=upload_location
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )

    def _str_(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Absent:detail", kwargs={"slug": self.slug})
        # return "/blog/%s/" % (self.id)

    class Meta:
        ordering = ["-created"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.absentreason)
    if new_slug is not None:
        slug = new_slug
    qs = Absent.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_Absent_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_Absent_receiver, sender=Absent)
