from django.db import models

# Create your models here.

class CollegeProfile( models.Model ):
    Branch = models.CharField(max_length= 100 )
    registration_number = models.CharField( max_length= 50 , primary_key=True )
    PassOutYear = models.CharField( max_length= 10 )

    def __str__(self) -> str:
        return self.registration_number


class PersonDetails(models.Model):
    college_profile  = models.ForeignKey( "CollegeProfile" , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length = 10)

    def __str__(self) -> str:
        return self.name
    

class ConnectHandles(models.Model):
    college_profile  = models.ForeignKey( "CollegeProfile" , on_delete=models.CASCADE)
    handlename = models.CharField(max_length=50 , null=True, blank=True)
    link = models.URLField(max_length=300,  null=True, blank=True)
    
    def __str__(self) -> str:
        return self.handlename


class PastCompanies_AndPosition(models.Model):
    college_profile  = models.ForeignKey( "CollegeProfile" , on_delete=models.CASCADE)
    company_name = models.CharField( max_length=100 ,null=True, blank=True)
    position_hold = models.CharField( max_length= 100 ,null=True, blank=True )
    years_worked = models.CharField( max_length= 10 )

    def __str__(self) -> str:
        return self.company_name


class Current_WorkProfile(models.Model):
    college_profile  = models.ForeignKey( "CollegeProfile" , on_delete=models.CASCADE)
    company_name = models.CharField( max_length=100 )
    current_position = models.CharField( max_length= 100 )
    years_worked = models.CharField( max_length= 10 )

    class Meta:
       managed = True
       db_table = 'current_workprofile'

    def __str__(self) -> str:
        return self.company_name


# class Positionheld_InCollege(models.Model):
#     college_profile  = models.ForeignKey( CollegeProfile , on_delete=models.CASCADE ),
#     position_name = models.CharField( max_length= 100 ,blank=True, default=True )
#     from_ =  models.DateField( auto_now= True ,null=True),
#     to_ =  models.DateField( auto_now=True ,null=True),


