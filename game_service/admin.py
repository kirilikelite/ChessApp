from django.contrib import admin
from .models import Piece, Square, ChessBoard

class PieceAdmin(admin.ModelAdmin):
    list_display = ['piece_type', 'color']
    list_filter = ['color', 'piece_type']
    search_fields = ['piece_type', 'color']

class SquareAdmin(admin.ModelAdmin):
    list_display = ['x_coord', 'y_coord', 'piece']
    list_filter = ['x_coord', 'y_coord']
    search_fields = ['x_coord', 'y_coord']
    raw_id_fields = ['piece']  # This makes it easier to assign a piece to a square in the admin interface

class ChessBoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'turn']
    list_filter = ['turn']
    search_fields = ['id']
    filter_horizontal = ['squares']

admin.site.register(Piece, PieceAdmin)
admin.site.register(Square, SquareAdmin)
admin.site.register(ChessBoard, ChessBoardAdmin)