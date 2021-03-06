from django.core.management.base import BaseCommand

from google_trans_new import google_translator

from main import choices
from main.models import ItemMenu, ItemName

from random_words import RandomWords


def depth_analys(item_object, depth=1):
    parent_id = item_object.parent_id
    if parent_id:
        parent = ItemMenu.objects.filter(id=parent_id).last()
        depth += 1
        return depth_analys(parent, depth)
    else:
        return depth


def item_fill_db(breadth, depth=2, parents=None):
    if not depth:
        return
    if parents:
        for parent in parents:
            childs = []
            for _ in range(breadth):
                child = ItemMenu.objects.create(parent=parent)
                childs.append(child)
            item_fill_db(breadth=breadth, depth=depth-1, parents=childs)
    else:  # len(parents) == 0
        childs = []
        for _ in range(breadth):
            child = ItemMenu.objects.create()
            childs.append(child)
        item_fill_db(breadth=breadth, depth=depth-1, parents=childs)


def name_fill_db():
    rw = RandomWords()
    translator = google_translator()
    queryset = ItemMenu.objects.all()
    for item in queryset:
        word = rw.random_word()
        for leng_id, leng_name in choices.LENG_CHOICE:
            if leng_name == 'en':
                ItemName.objects.create(
                    name=word,
                    leng=leng_id,
                    item_menu_id=item
                )
            else:
                trans_word = translator.translate(word, lang_src='en', lang_tgt=leng_name)
                ItemName.objects.create(
                    name=trans_word,
                    leng=leng_id,
                    item_menu_id=item
                )


class Command(BaseCommand):
    help = 'Generate random books'  # noqa

    def add_arguments(self, parser):
        parser.add_argument('-d', '--depth', type=int, help='nesting depth')
        parser.add_argument('-b', '--breadth', type=int, help='namber of elements i breadth')

    def handle(self, *args, **kwargs):
        depth = kwargs.get("depth", 2)
        depth = 2 if depth is None else depth
        breadth = kwargs.get("breadth", 5)
        breadth = 5 if breadth is None else breadth
        item_fill_db(breadth=breadth, depth=depth)
        name_fill_db()
