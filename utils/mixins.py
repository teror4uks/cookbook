from utils import helpers

class CheckSlugMixin:
    def check_slug(self, instance):
        qs_exist = instance.__class__.objects.filter(slug=instance.slug).exists()
        if qs_exist:
            slug = helpers.unique_slug_generator(instance)
        return slug