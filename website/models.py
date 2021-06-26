
from django.db import models


class User_details(models.Model):
    name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.CharField(max_length=50, default="xxx@soccernet.pt")
    date_Of_Birth = models.CharField(max_length=50, default="18/05/2001")
    phone = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id} <-> ({self.name}) - mail {self.email} with phone {self.phone} and born in {self.date_Of_Birth}"


class Quizz(models.Model):
    user_id = models.ForeignKey(User_details, on_delete=models.CASCADE, related_name="id_user_quizz")
    question1 = models.CharField(max_length=20, default="answ1")
    question2 = models.CharField(max_length=20, default="answ2")
    question3 = models.CharField(max_length=20, default="answ3")
    question4 = models.CharField(max_length=20, default="answ4")
    question5 = models.CharField(max_length=20, default="answ5")
    question6 = models.CharField(max_length=20, default="answ6")
    question7 = models.CharField(max_length=20, default="answ7")
    question8 = models.CharField(max_length=20, default="answ8")
    question9 = models.CharField(max_length=20, default="answ9")
    question10 = models.CharField(max_length=20, default="answ10")

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


class User_Opinion(models.Model):
    id_user = models.IntegerField(default=0)
    opinion_text = models.CharField(max_length=300)
    opinion2 = models.IntegerField(default=0)
    opinion3 = models.IntegerField(default=0)

    def __str__(self):
        return f"Opiniao do user {self.id_user} : {self.opinion_text} : {self.opinion2} : {self.opinion3}"