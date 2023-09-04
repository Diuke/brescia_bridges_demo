from django.shortcuts import render, HttpResponse
from django.core import serializers
from db_demo.models import Piece, Defect

# Create your views here.

def related_answers_for_piece(request):
    try:
        piece_id = request.GET.get('piece_id')
        piece = Piece.objects.get(id=piece_id)
        related_ = Defect.objects.all().filter(piece=piece)
        data = serializers.serialize('json', related_)
        return HttpResponse(data)
    except Exception as ex:
        return HttpResponse([])