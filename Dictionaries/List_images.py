from PIL import Image


class List_images:
    def __init__(self):
        self.Images = {
            'blackRook': {'Image': Image.open("Images/Rook-Black.png")},
            'blackKnight': {'Image': Image.open("Images/Horse-Black.png")},
            'blackBishop': {'Image': Image.open("Images/Bishop-Black.png")},
            'blackKing': {'Image': Image.open("Images/King-Black.png")},
            'blackQueen': {'Image': Image.open("Images/Queen-Black.png")},
            'blackPawn': {'Image': Image.open("Images/Pawn-Black.png")},
            'whiteRook': {'Image': Image.open("Images/Rook-White.png")},
            'whiteKnight': {'Image': Image.open("Images/Horse-White.png")},
            'whiteBishop': {'Image': Image.open("Images/Bishop-White.png")},
            'whiteKing': {'Image': Image.open("Images/King-White.png")},
            'whiteQueen': {'Image': Image.open("Images/Queen-White.png")},
            'whitePawn': {'Image': Image.open("Images/Pawn-White.png")}}
