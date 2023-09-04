from django.urls import path
from db_demo.views import related_answers_for_piece

urlpatterns = [
    path('related_answers_for_piece', related_answers_for_piece, name = 'related_answers_for_piece')
]