from django.db import models

# Create your models here.

class TModel(models.Model):
		tno=models.IntegerField()
		task=models.TextField()
		task_dt=models.DateTimeField(auto_now_add=True)


		def __str__(self):
			return self.tno;