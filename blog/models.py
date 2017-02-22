from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Blog(models.Model):

    """
    This model will be used for interaction between the public and the school.
    """

    title = models.CharField(
        _('Blog Title'),
        max_length=255,
        null=False,
        blank=False
    )

    featurephotoone = models.ImageField(
        _('Feature Picture One'),
        max_length=255,
        null=False,
        blank=False,
        upload_to=upload_location
    )

    featurephototwo = models.ImageField(
        _('Feature Picture Two'),
        max_length=255,
        null=True,
        blank=True,
        upload_to=upload_location
    )

    featurephotothree = models.ImageField(
        _('Feature Picture Three'),
        max_length=255,
        null=True,
        blank=True,
        upload_to=upload_location
    )

    content = models.CharField(
        _('Blog Content'),
        max_length=255,
        null=True,
        blank=True
    )

    emailorphone = models.CharField(
        _('Email or Phone'),
        max_length=30,
        null=True,
        blank=True
    )

    comment = models.CharField(
        _('Comment'),
        max_length=255,
        null=True,
        blank=True
    )

    users = models.ForeignKey(
        User,
        null=True,
        blank=True
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
    modified = models.DateTimeField(
        _('Date Modified'),
        auto_now_add=True,
        null=False,
        blank=False
    )

    def _str_(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
        # return "/blog/%s/" % (self.id)

    class Meta:
        ordering = ["-created"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Blog.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_Blog_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_Blog_receiver, sender=Blog)


class Notification(models.Model):

    """
    This model will be used to send out notification to students.
    """

    eventtitle = models.CharField(
        _('Event Title'),
        max_length=255,
        null=False,
        blank=False
    )

    eventphoto = models.ImageField(
        _('Event Photo'),
        max_length=255,
        null=True,
        blank=True,
        upload_to=upload_location
    )

    eventcontent = models.CharField(
        _('Event Content'),
        max_length=255,
        null=False,
        blank=False
    )

    eventdate = models.DateField(
        _('Event Date'),
        max_length=30,
        null=True,
        blank=True
    )

    slug = models.SlugField(
        unique=True
    )

    created = models.DateTimeField(
        _('Date Created'),
        auto_now=True,
        null=True,
        blank=True
    )
    modified = models.DateTimeField(
        _('Date Modified'),
        auto_now_add=True,
        null=False,
        blank=False
    )

    users = models.ForeignKey(
        User,
        null=True,
        blank=True
    )

    def _str_(self):
        return self.eventtitle

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
        # return "/blog/%s/" % (self.id)

    class Meta:
        ordering = ["-created"]


# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.eventtitle)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Notification.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" % (slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug


# def pre_save_Notification_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)


# pre_save.connect(pre_save_Notification_receiver, sender=Notification)
