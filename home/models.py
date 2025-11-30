from django.db import models
from django.utils.text import slugify

class Author(models.Model):
    name = models.CharField(max_length=30)
    dob = models.DateTimeField()

    def __str__(self):
        return f'{self.name}'

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True,blank=True,null=True)
    author = models.ForeignKey(Author,
                                on_delete=models.CASCADE,
                                null=True,
                                related_name='written_articles')
    editor = models.ForeignKey(Author,
                                on_delete=models.CASCADE,
                                null=True,
                                related_name="edited_articles")
    author_email = models.EmailField()
    is_published = models.BooleanField(default=True)


    def save(self,*args,**kwargs):
        if self.id: 
            super().save(*args,**kwargs)

        else:
            if not self.slug:
                self.slug = slugify(self.title)
            super().save(*args,**kwargs)

    def __str__(self) -> str:
        return f'{self.id}. {self.title}'
        

        