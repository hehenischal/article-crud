from django.contrib import admin
from .models import Article,Author

# admin panel changes 
admin.site.register(Article)
admin.site.register(Author)

