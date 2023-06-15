from django.db import models

# Create your models here.







class Product_Category(models.Model):
    PC_ID=models.IntegerField(primary_key=True)
    PC_Name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.PC_Name



class Product(models.Model):
    PC_Name=models.ForeignKey(Product_Category,on_delete=models.CASCADE)
    Pid=models.IntegerField()
    Pname=models.CharField(max_length=100)
    Pprice=models.IntegerField()
    Pdescription=models.TextField()
    Pdate=models.DateField()


    def __str__(self) -> str:
        return self.Pname

















