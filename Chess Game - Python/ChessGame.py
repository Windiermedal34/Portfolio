class chess_team():

    def __init__(self, colour):
        self.team_colour = colour
        self.team_pieces = {}
        self.populate_chess_pieces()

    def populate_chess_pieces(self):
        self.team_pieces['King'] = [chess_piece(self.team_colour, 'King')]
        self.team_pieces['Queen'] = [chess_piece(self.team_colour, 'Queen')]
        self.team_pieces['Bishop'] = []
        self.team_pieces['Knight'] = []
        self.team_pieces['Rook'] = []
        for i in range(2):
            self.team_pieces['Bishop'].append(chess_piece(self.team_colour, 'Bishop'))
            self.team_pieces['Knight'].append(chess_piece(self.team_colour, 'Knight'))
            self.team_pieces['Rook'].append(chess_piece(self.team_colour, 'Rook'))
        
        self.team_pieces['Pawn'] = []
        for i in range(8):
            self.team_pieces['Pawn'].append(chess_piece(self.team_colour, 'Pawn'))
        
        self.print_pieces()

    def print_pieces(self):
        print('-------------------------------')
        print(f'{self.team_colour} Team')
        print('-------------------------------')
        for piece in self.team_pieces.values():
            if len(piece) <= 1:
                print(f'{len(piece)} {piece[0].piece_colour} {piece[0].piece_role} piece')
            else:
                print(f'{len(piece)} {piece[0].piece_role} pieces')
            for p in piece:
                print(f'- {p}')

class chess_piece():

    def __init__(self, colour, role):
        self.piece_colour = colour
        self.piece_role = role
        self.status = 'Active'

    def __str__(self):
        return (f'{self.piece_colour} {self.piece_role} Piece - {self.status}')
    
    def piece_defeated(self):
        self.status = 'Defeated'


chess_team('White')
chess_team('Black')