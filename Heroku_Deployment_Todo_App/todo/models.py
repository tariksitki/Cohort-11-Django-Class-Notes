from django.db import models

# Create your models here.


class Todo(models.Model):
    status_choices = [
        ("C", "Completed"),
        ("P", "Pending"),
        ("I", "In-Progress")
    ]
    priority_choices = [
        ("1", "😂"),
        ("1", "😊"),
        ("1", "🤣"),
        ("1", "😒"),
        ("1", "😁")
    ]
    title = models.CharField(max_length=40)
    description = models.TextField()
    status = models.CharField(max_length=30, choices=status_choices)
    priority = models.CharField(max_length=30, choices=priority_choices)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Todoss"
        db_table = "Todos_Table"
        ordering = ["title"]

        ## ordering liste yada tuple olmali





    ## windows tusu ve noktaya basili tut   emoji
    ## emoji icin extension var 



