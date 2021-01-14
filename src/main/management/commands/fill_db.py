from django.core.management.base import BaseCommand

from main.models import ItemName, ItemMenu


def depth_analys(item_object, depth=1):
    parent_id = item_object.parent_id
    if parent_id:
        parent = ItemMenu.objects.filter(id=parent_id).last()
        depth += 1
        return depth_analys(parent, depth)
    else:
        return depth


# def item_fill_db():
#     for i in range(20):
#         ItemMenu.objects.create()


class Command(BaseCommand):
    help = 'Generate random books'  # noqa

    def add_arguments(self, parser):
        parser.add_argument('-d', '--depth', type=int, help='nesting depth')
        parser.add_argument('-b', '--breadth', type=int, help='namber of elements i breadth')

    def handle(self, *args, **kwargs):
        ob1 = ItemMenu.objects.all().last()
        x = depth_analys(ob1)
        print(x)
