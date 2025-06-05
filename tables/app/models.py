from django.db import models
# Create your models here.

# creating a model for the table department
class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=10)
    loc = models.CharField(max_length=10)
    def __str__(self):
        return str(self.deptno)
        
# creating a model for the table employee
class emp(models.Model):
    eno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    hiredate = models.DateField(auto_now_add=True)
    mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    sal = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    comm = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    deptno = models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        
# creating a model for the table sale

class Sal(models.Model):
    Grade=models.IntegerField()
    losal=models.DecimalField(max_digits=10,decimal_places=2)
    hisal=models.DecimalField(max_digits=10,decimal_places=2)

    def _str_(self):
        return str(self.Grade)