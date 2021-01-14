from django.db import models

from .utils import choice_to_str

from . import choices


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


    # def __str__(self):
    #     leng = ''
    #     for leng_choice in choices.LENG_CHOICE:
    #         if leng_choice[0] == self.leng:
    #             leng = leng_choice[1]
    #             break
    #     return f"{self.item_menu_id.id}) {self.name} ({leng})"


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





    # def __str__(self):
    #     name = ItemName.objects.filter(item_menu_id=self.id, leng=2).first()
    #     eng_name = None if not name else name.name
    #     return f"{self.id}) Item: {eng_name}"
