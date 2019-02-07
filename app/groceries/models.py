from django.db import models

class GroceryItem(models.Model):
    """
    GroceryItem Model
    Defines the attributes of a grocery list item
    """
    name = models.CharField(max_length=255)
    amount = models.IntegerField(default=1)
    msg = models.CharField(max_length=255, blank=True)

    def get_item(self):
        return 'You need ' + str(self.amount) + ' of ' + self.name + ' (' + self.msg + ').'

    def __repr__(self):
        return self.name + ' is added.'
