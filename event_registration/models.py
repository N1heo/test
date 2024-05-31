from django.db import models


class Conference(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ConfUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, error_messages={'unique':"This email has already been registered."})
    conferences = models.ManyToManyField(Conference)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['reg_date']

