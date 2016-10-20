from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    value = models.IntegerField()

    # def __str__(self):
    #     return self.name + ' [' + str(self.value) + ']'