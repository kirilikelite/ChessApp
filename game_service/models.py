from django.db import models

# Create your models here.


class Piece(models.Model):
    PIECE_TYPES = (
        ('P', 'Pawn'),
        ('R', 'Rook'),
        ('N', 'Knight'),
        ('B', 'Bishop'),
        ('Q', 'Queen'),
        ('K', 'King'),
    )
    COLORS = (
        ('B', 'Black'),
        ('W', 'White'),
    )

    piece_type = models.CharField(max_length=1, choices=PIECE_TYPES)
    color = models.CharField(max_length=1, choices=COLORS)

    def __str__(self):
        return f"{self.get_color_display()} {self.get_piece_type_display()}"

class Square(models.Model):
    x_coord = models.IntegerField()  # 1 to 8
    y_coord = models.IntegerField()  # 1 to 8
    piece = models.ForeignKey(Piece, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ['x_coord', 'y_coord']

    def __str__(self):
        return f"({self.x_coord}, {self.y_coord})"

class ChessBoard(models.Model):
    squares = models.ManyToManyField(Square)
    turn = models.CharField(max_length=1, choices=Piece.COLORS, default='W')  # 'W' or 'B'
    # Other fields like game status, game history, etc. can be added.

    def __str__(self):
        return f"Chess Board ID: {self.id}"


    def init_pawns(self):
        white_pawn_row = 2
        black_pawn_row = 7
        for square in self.squares.filter(y_coord__in=[white_pawn_row, black_pawn_row]):
            if square.y_coord == white_pawn_row:
                rock = Piece(piece_type="P", color="w")
            else:
                rock = Piece(piece_type="P", color="b")
            rock.save()
            square.piece = rock
            square.save()

    def init_rocks(self):
        white_rock_row = 1
        black_rock_row = 8
        for square in self.squares.filter(y_coord__in=[white_rock_row, black_rock_row], x_coord__in=[1, 8]):
            if square.y_coord == white_rock_row:
                knight = Piece(piece_type="R", color="w")
            else:
                knight = Piece(piece_type="R", color="b")
            knight.save()
            square.piece = knight
            square.save()

    def init_knights(self):
        white_knight_row = 1
        black_knight_row = 8
        for square in self.squares.filter(y_coord__in=[white_knight_row, black_knight_row], x_coord__in=[2, 7]):
            if square.y_coord == white_knight_row:
                knight = Piece(piece_type="N", color="w")
            else:
                knight = Piece(piece_type="N", color="b")
            knight.save()
            square.piece = knight
            square.save()

    def init_bishops(self):
        white_bishop_row = 1
        black_bishop_row = 8
        for square in self.squares.filter(y_coord__in=[white_bishop_row, black_bishop_row], x_coord__in=[3, 6]):
            if square.y_coord == white_bishop_row:
                bishop = Piece(piece_type="B", color="w")
            else:
                bishop = Piece(piece_type="B", color="b")
            bishop.save()
            square.piece = bishop
            square.save()

    def init_queens(self):
        white_queen = Piece(piece_type="Q", color="w")
        black_queen = Piece(piece_type="Q", color="b")
        white_queen.save()
        black_queen.save()
        white_queen_square = self.squares.get(x_coord=4, y_coord=1)
        black_queen_square = self.squares.get(x_coord=4, y_coord=8)
        white_queen_square.piece = white_queen
        black_queen_square.piece = black_queen
        white_queen_square.save()
        black_queen_square.save()

    def init_kings(self):
        white_king = Piece(piece_type="K", color="w")
        black_king = Piece(piece_type="K", color="b")
        white_king.save()
        black_king.save()
        white_king_square = self.squares.get(x_coord=5, y_coord=1)
        black_king_square = self.squares.get(x_coord=5, y_coord=8)
        white_king_square.piece = white_king
        black_king_square.piece = black_king
        white_king_square.save()
        black_king_square.save()

    def init_squares(self):
        for x in [1,2,3,4,5,6,7,8]:
            for y in [1,2,3,4,5,6,7,8]:
                print(f"x:{x}, y:{y}")
                square = Square(x_coord=x, y_coord=y, piece=None)
                square.save()
                self.squares.add(square)

    def init_board(self):
        self.init_squares()
        self.init_pawns()
        self.init_rocks()
        self.init_bishops()
        self.init_knights()
        self.init_queens()
        self.init_kings()
