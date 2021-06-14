from django.db import models


class User_details(models.Model):
    name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    date_Of_Birth = models.DateField()

    def __str__(self):
        return f"{self.id} <-> ({self.name}) with phone {self.phone} and born in {self.date_Of_Birth} "


class Quizz(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    user_id = models.ForeignKey(User_details, on_delete=models.CASCADE, related_name="id_user_quizz")

    def __str__(self):
        return f"{self.id} <-> {self.user_id}"


class User_Quizz(models.Model):
    name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    quizzes = models.ManyToManyField(Quizz,
                                     blank=True,
                                     related_name="QuizzesUser"
                                     )

    def __str__(self):
        return f"{self.name} {self.last_name} and {self.quizzes}"
