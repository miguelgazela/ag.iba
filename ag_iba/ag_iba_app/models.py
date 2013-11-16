from django.db import models

class User(models.Model):

    USER_PERMISSIONS = (
        ('ST', 'Standard'),
        ('AD', 'Admin'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    permission = models.CharField(max_length=2, choices=USER_PERMISSIONS)
    date_joined = models.DateTimeField()
    activated = models.BooleanField(default=False)

    def __unicode__(self):
        return "{first} {last}".format(
            first=self.first_name,
            last=self.last_name
        )

    def is_active(self):
        return self.activated


