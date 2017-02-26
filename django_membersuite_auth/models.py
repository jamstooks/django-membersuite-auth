from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from future.utils import python_2_unicode_compatible


@python_2_unicode_compatible
class MemberSuitePortalUser(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    membersuite_id = models.CharField(max_length=64, unique=True)
    membersuite_session_key = models.CharField(max_length=64, unique=True)
    is_member = models.BooleanField(default=False)

    def __str__(self):
        return ("<{classname}: membersuite ID: {membersuite_id}, "
                "user ID: {user_id}, is member: {is_member}").format(
                    classname=self.__class__.__name__,
                    membersuite_id=self.membersuite_id,
                    user_id=self.user.id,
                    is_member=self.is_member)
