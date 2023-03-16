from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItemManager(models.Manager):

    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)  # contenttype id for the product model
        return TaggedItem.objects \
            .select_related('tag') \
            .filter(
            content_type=content_type,
            object_id=obj_id
        )


#  мы делаем так, если хотим чтобы это приложение можно было использовать в других проектах
#  если не хотим, можно просто product = models.ForeignKey(Product...)
class TaggedItem(models.Model):
    objects = TaggedItemManager()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    #  if primary key is not an integer this is not going to work
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
