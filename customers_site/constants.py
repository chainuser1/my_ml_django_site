from survey_app.models import Category
TAX_AMOUNT = 12

CATEGORY_CHOICES = [(category.id,category.name) for category in Category.objects.all()]