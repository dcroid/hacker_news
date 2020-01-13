from django.core.management.base import BaseCommand
from news.models import Post
from news.spider import ycombinator


class Command(BaseCommand):
    help = 'Parsing new from news.ycombinator.com'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Start parsing ycombinator.com'))
        news = ycombinator()
        objs = [Post(**data) for data in news]
        Post.objects.bulk_create(objs, ignore_conflicts=True)
        self.stdout.write(self.style.SUCCESS('Get {} objects\nFinished!!!'.format(len(news))))


