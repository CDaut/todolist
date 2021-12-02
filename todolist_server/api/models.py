from django.db import models
from user_manager.models import ApplicationUser

'''
The Category that a certain task fits into
'''


class Category(models.Model):
    title = models.CharField(max_length=200)
    color = models.IntegerField()
    created_by = models.ForeignKey(ApplicationUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


'''
Model for a task
MODIFIER_FUNCTIONS: Possible functions by which the task priority can increase or decrease
'''


class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(ApplicationUser, on_delete=models.CASCADE)
    due_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    MODIFIER_FUNCTIONS = [
        ('n', 'none'),
        ('e', 'exponential'),
        ('l', 'linear'),
    ]
    # function by which the task importance increases or decreases
    modifier_function = models.CharField(choices=MODIFIER_FUNCTIONS, max_length=2, blank=True)

    # parameters in the eisenhower matrix
    importance = models.IntegerField()
    urgency = models.IntegerField()
    # the todolist_server importance that this task cannot drop below.
    base_importance = models.IntegerField()

    # parameters for different functions
    m = models.FloatField(blank=True, default=0)  # y(x) = m * x + base_importance. This is the m factor.
    exponent = models.FloatField(blank=True,
                                 default=0)  # y(x) = e^(exponent * x) + base_importance. This is the decay factor

    def __str__(self):
        return self.title
