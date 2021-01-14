from django.db import models

from . import choices
from .utils import choice_to_str


class ItemName(models.Model):
    """
    This model exist for easy addition of language at any stage
    """
    name = models.CharField(max_length=256)
    leng = models.PositiveSmallIntegerField(choices=choices.LENG_CHOICE)
    item_menu_id = models.ForeignKey('main.ItemMenu', on_delete=models.CASCADE)

    @property
    def get_leng_name(self):
        return choice_to_str(self.leng, choices.LENG_CHOICE)


class ItemMenu(models.Model):
    """
    Homogeneous relations using for unlimited scaling in depth
    """
    parent = models.ForeignKey(
        'main.ItemMenu',
        on_delete=models.CASCADE,
        null=True,
        default=None,
    )
    link_data = models.CharField(max_length=256, null=True, default=None)
