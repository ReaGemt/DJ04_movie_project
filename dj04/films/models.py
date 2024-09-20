from django.db import models

class Film(models.Model):
    title = models.CharField("Название фильма", max_length=100)
    description = models.TextField("Описание фильма")
    review = models.TextField("Отзыв")
    image = models.ImageField("Обложка фильма", upload_to='film_images/', blank=True, null=True)

    def __str__(self):
        return self.title
