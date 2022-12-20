from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

EXPENSE_CATEGORY = (
    ("Food","Food"),
    ("Travel","Travel"),
    ("Shopping","Shopping"),
    ("Entertainment","Entertainment"),
    ("RENT","RENT"),
    ("HOME","HOME"),
    ("EMI","EMI"),
    ("Other","Other")
)

# ADD_EXPENSE_CHOICES = [
#      ("Expense","Expense"),
#      ("Income","Income")
#  ]

PAYMENT_MODE =(
    ("CASH","CASH"),
    ("DEBIT-CARD","DEBIT-CARD"),
    ("CREDIT-CARD","CREDIT-CARD"),
    ("ONLINE-BANKING","ONLINE-BANKING"),
    ("UPI","UPI")

)



class Expense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    date = models.DateTimeField(default=now)
    ename  = models.CharField(max_length=100)
    eamount  = models.FloatField()
    pay_mode = models.CharField(max_length=100, choices=PAYMENT_MODE)
    expense_type  = models.CharField(max_length=100, choices=EXPENSE_CATEGORY)
    # bill_receipt = models.FileField(blank=True,upload_to='documents/')












# 'c'  : 'collectstatic', # django c
# 'r'  : 'runserver',
# 'sd' : 'syncdb',
# 'sp' : 'startproject',
# 'sa' : 'startapp',
# 't'  : 'test',





# class Addmoney_info(models.Model):
#     user = models.ForeignKey(User,default = 1, on_delete=models.CASCADE)
#     add_money = models.CharField(max_length = 10 , choices = ADD_EXPENSE_CHOICES )
#     quantity = models.BigIntegerField()
#     Date = models.DateField()
#     Category = models.CharField( max_length = 20, choices = SELECT_CATEGORY_CHOICES , default ='Food')
#     class Meta:
#         db_table:'addmoney'
        
# class UserProfile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     profession = models.CharField(max_length = 10, choices=PROFESSION_CHOICES)
#     Savings = models.IntegerField( null=True, blank=True)
#     income = models.BigIntegerField(null=True, blank=True)
#     image = models.ImageField(upload_to='profile_image',blank=True)


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    income  = models.FloatField()
    expenses  = models.FloatField(default=0)
    balance = models.FloatField(blank=True, null=True)


# class TaskQuerySet(models.QuerySet):
#     def task_name_list(self):
#         return self.filter(task_name__startswith='p')


# class TaskManager(models.Manager):
#     def completed_task(self):
#         return super().get_queryset().filter(is_finished=True)
    
#     # def task_name_list(self):
#     #     return self.filter(task_name__startswith='s')

#     def get_queryset(self):
#         return TaskQuerySet(self.model, using=self._db)

# class DailyTask(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     task_name = models.CharField(max_length=255)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     due = models.DateTimeField()
#     is_finished = models.BooleanField(default=False)

#     objects = models.Manager()
#     task_objects = TaskManager()


