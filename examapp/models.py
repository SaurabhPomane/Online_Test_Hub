from django.db import models

# Create your models here.
class Quetion (models.Model):
    qno=models.IntegerField(primary_key=True)
    gtext=models.CharField(max_length=50)
    answer=models.CharField(max_length=50)
    op1=models.CharField(max_length=50)
    op2=models.CharField(max_length=50)
    op3=models.CharField(max_length=50)
    op4=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"qno : {self.qno},qtext:{self.gtext},answer:{self.answer},op:{self.op1},op:{self.op2},op:{self.op3},op:{self.op4},subject:{self.subject}"
    class Meta:
        db_table="quetions"


class Result(models.Model):
            username=models.CharField(max_length=50,primary_key=True)
            subject=models.CharField(max_length=20)
            score=models.IntegerField()

            class Meta:
                  db_table="Result"
