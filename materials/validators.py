from rest_framework.serializers import ValidationError


def validate_url_materials(value):
    if 'youtube.com' not in value:
        raise ValidationError('Ссылка ведет на сторонний ресурс')
