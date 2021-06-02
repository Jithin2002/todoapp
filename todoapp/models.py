from django.db import models

# Create your models here.

class Todos(models.Model):
    task_name=models.CharField(max_length=150)
    status=models.CharField(max_length=15,default="not completed")
    user=models.CharField(max_length=140)
    date=models.DateField(auto_now=True)

    def __str__(self):
        return self.task_name



    #python manage.py makemigrations
    #python manage.py migrate

    #ORM queries for creating an object
    #reference_name=className(fieldname=value,fieldname=value,fieldname=value)
    #reference.save()



    #python manage.py shell

    #orm query for fetching all records
    #reference+name=className.objects.all()
    #print(todos)

    #todos created by a user-filter
    #refname=modelname.objects.filter(field=value)