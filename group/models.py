from django.db import models

# Create your models here.

# if the models for your application live in the module myapp.models 
# (the package structure that is created for an application by the manage.py startapp script), 
# INSTALLED_APPS should read, in part:

# INSTALLED_APPS = [
#     #...
#     'myapp',
#     #...
# ]
# When you add new apps to INSTALLED_APPS, be sure to run manage.py migrate,
#  optionally making migrations for them first with manage.py makemigrations.

from django.db import models

#this is the model that will be the table of all possible Events or Activities that are suggested; 
# for simplicity we us only the fields (columns) name and cost for now
#note: a field called 'ID' is automatically created as the key in the background
#It is read only; we show how to access it below.

class Events(models.Model):
    name = models.CharField(max_length=30)  # $EVENTNAME,
   # location = models.CharField(max_length=30)  # $EVENTLOCATION,  # put (lat, long) for mapping?
    cost  = models.IntegerField()  # : $EVENTCOST,  #just make 1, 2, or 3 for now (cheap, medium, expensive)
   # description =models.CharField(max_length= 50)  #  $‘EVENTDESCRIPTION’
   # Img = =models.CharField(max_length=200)  # $EVENTIMAGE # link to image (eg jpg)


#test it out 

#SQL translations: :-) 
#class = SQL table
#instance of class = entry in the table

event1 = Events(name = "Biking", cost = 1)
event1.save()

event2 = Events(name = "Bowling", cost = 2)
event2.save()

event3 = Events(name = "Trip to Vegas", cost = 3)
event3.save()
