from rest_framework import serializers
from flashcards.models import Flashcard, FlashcardCollection


class FlashcardCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashcardCollection
        fields = [
            'id',
            'title',
            'description',
            'header_color',
            'background_color',
            'font_color',
            'header_font_color',
            'header_text_left',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = [
            'id',
            'collection',
            'front',
            'back',
            'header_right',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
