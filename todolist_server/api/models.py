from django.db import models
from users.models import ApplicationUser

'''
The Category that a certain task fits into
'''


class Category(models.Model):
    title = models.CharField(max_length=200)
    color = models.IntegerField()


'''
Model for a task
MODIFIER_FUNCTIONS: Possible functions by which the task priority can increase or decrease
'''


class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(ApplicationUser, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    MODIFIER_FUNCTIONS = [
        ('e', 'exponential'),
        ('l', 'linear'),
    ]
    # function by which the task importance increases or decreases
    modifier_function = models.CharField(choices=MODIFIER_FUNCTIONS, max_length=2)

    # parameters in the eisenhower matrix
    importance = models.IntegerField()
    urgency = models.IntegerField()
    # the base importance that this task cannot drop below.
    base_importance = models.IntegerField()

    # parameters for different functions
    m = models.FloatField()  # y(x) = m * x + base_importance. This is the m factor.
    exponent = models.FloatField()  # y(x) = e^(exponent * x) + base_importance. This is the decay factor
