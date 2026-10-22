
from sre_parse import CATEGORIES
from django.db import models


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ("income", "Income"),
        ("expense", "Expense"),
    )
    CATEGORIES = (
        ('food', 'Food'),
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('transport', 'Transport'),
        ('housing', 'Housing'),
        ('health', 'Health'),
        ('shopping', 'Shopping'),
        ('freelance', 'Freelance'),
        ('salary', 'Salary'),
        ('investments', 'Investments'),
        ('other', 'Other'),
    )

    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES,
    )
    category = models.CharField(
        max_length=20,
        choices = CATEGORIES,
        default = 'other'
    )
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
