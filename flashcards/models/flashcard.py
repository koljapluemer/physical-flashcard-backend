from django.db import models


class Flashcard(models.Model):
    collection = models.ForeignKey('FlashcardCollection', on_delete=models.CASCADE, related_name='flashcards')
    front = models.TextField()
    back = models.TextField()
    header_right = models.CharField(max_length=200, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.front[:50] if self.front else f"Flashcard {self.id}"


class FlashcardCollection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    header_color = models.CharField(max_length=7, default='#100e75')
    background_color = models.CharField(max_length=7, default='#f0f0f0')
    font_color = models.CharField(max_length=7, default='#171717')
    header_font_color = models.CharField(max_length=7, default='#fff')
    header_text_left = models.CharField(max_length=200, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
