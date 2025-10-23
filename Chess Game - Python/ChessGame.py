class chess_game():

    king_movements = {
        'One space vertical':[0,1],
        'One space horizontal':[1,0],
        'One space diagonal':[[1,1],[1,-1],[-1,1],[-1,-1]]}
    queen_movements = ['Multi spaces vertical', 'Multi spaces horizontal', 'Multi spaces diagonal']
    bishop_movements = ['Multi spaces diagonal']
    knight_movements = ['One space horizontal and Two spaces vertical', 'Two Spaces horizontal and One space vertical']
    rook_movements = ['Multi spaces horizontal','Multi spaces vertical']
    pawn_movements = {
        'Two spaces vertical (In one direction, first move of game)':[[0,2],[0,-2]],
        'One space vertical (In one direction)':[[0,1],[0,-1]],
        'One space diagonal (when taking a piece)':[[1,1],[1,-1],[-1,1],[-1,-1]]}

    def __init__(self):
        print('Chess Game')

class chess_team():

    def __init__(self, colour):
        self.team_colour = colour
        self.team_pieces = {}
        self.piece_movements = self.retrieve_piece_movements()
        self.populate_chess_pieces()

    def populate_chess_pieces(self):
        self.team_pieces['King'] = [chess_piece(self.team_colour, 'King', self.piece_movements['King'], 1)]
        self.team_pieces['Queen'] = [chess_piece(self.team_colour, 'Queen', self.piece_movements['Queen'], 1)]
        self.team_pieces['Bishop'] = []
        self.team_pieces['Knight'] = []
        self.team_pieces['Rook'] = []
        for i in range(2):
            self.team_pieces['Bishop'].append(chess_piece(self.team_colour, 'Bishop', self.piece_movements['Bishop'], i+1))
            self.team_pieces['Knight'].append(chess_piece(self.team_colour, 'Knight', self.piece_movements['Knight'], i+1))
            self.team_pieces['Rook'].append(chess_piece(self.team_colour, 'Rook', self.piece_movements['Rook'], i+1))
        self.team_pieces['Pawn'] = []
        for i in range(8):
            self.team_pieces['Pawn'].append(chess_piece(self.team_colour, 'Pawn', self.piece_movements['Pawn'], i+1))
        
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

    def retrieve_piece_movements(self):
        piece_movements = {}
        piece_movements['King'] = [[0,1],[1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        piece_movements['Queen'] = [
            [0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],
            [1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],
            [1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],
            [1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7],
            [-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],
            [-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7]
        ]
        piece_movements['Bishop'] = [
            [1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],
            [1,-1],[2,-2],[3,-3],[4,-4],[5,-5],[6,-6],[7,-7],
            [-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],
            [-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7]
        ]
        piece_movements['Knight'] = [
            [1,2],[1,-2],[-1,2],[-1,-2],
            [2,1],[2,-1],[-2,1],[-2,-1]
            ]
        piece_movements['Rook'] = [
            [0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],
            [1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0]
            ]
        if self.team_colour == 'White':
            piece_movements['Pawn'] = [[0,-2],[0,-1],[1,-1],[-1,-1]]
        else:
            piece_movements['Pawn'] = [[0,1],[1,1],[-1,1]]

        return piece_movements

class chess_piece():

    def __init__(self, colour, role, movements, no):
        self.piece_colour = colour
        self.piece_role = role
        self.piece_movement = movements
        self.piece_no = no
        self.piece_current_location = self.piece_starting_location()
        #self.piece_movement = self.piece_movements()
        self.status = 'Active'

    def __str__(self):
        return (f'{self.piece_colour} {self.piece_role} {self.piece_no} Piece - {self.status} - Current Location {self.piece_current_location} - Can move {self.piece_movement}')
    
    def piece_defeated(self):
        self.status = 'Defeated'

    def piece_starting_location(self):
        if self.piece_role == 'King':
            if self.piece_colour == 'White':
                return [0,4]
            else:
                return [7,4]
        elif self.piece_role == 'Queen':
            if self.piece_colour == 'White':
                return [0,3]
            else:
                return [7,3]
        elif self.piece_role == 'Bishop':
            if self.piece_no == 1:
                if self.piece_colour == 'White':
                    return [0,2]
                else:
                    return [7,2]
            else:
                if self.piece_colour == 'White':
                    return [0,5]
                else:
                    return [7,5]
        elif self.piece_role == 'Knight':
            if self.piece_no == 1:
                if self.piece_colour == 'White':
                    return [0,1]
                else:
                    return [7,1]
            else:
                if self.piece_colour == 'White':
                    return [0,6]
                else:
                    return [7,6]
        elif self.piece_role == 'Rook':
            if self.piece_no == 1:
                if self.piece_colour == 'White':
                    return [0,0]
                else:
                    return [7,0]
            else:
                if self.piece_colour == 'White':
                    return [0,7]
                else:
                    return [7,7]
        else:
            if self.piece_colour == 'White':
                return [1,self.piece_no+1]
            else:
                return [6,self.piece_no+1]



    def piece_movements(self):
        piece_movements = {'King':'One square all directions',
                           'Queen': 'Multiple squares all directions',
                           'Bishop': 'Multiple squares diagonally',
                           'Knight': 'One square horizontally and two squares vertically or two squares horizontally and one square vertically',
                           'Rook': 'Multiple squares horizontally and vertically',
                           'Pawn': 'One square vertically'}
        if self.piece_role == 'Pawn':
            return self.pawn_movements()
        elif self.piece_role == 'Rook':
            return self.rook_movements()
        #return piece_movements[self.piece_role]
    
    def pawn_movements(self):
        if self.piece_colour == 'White':
            return [[0,-2],[0,-1],[1,-1],[-1,-1]]
        else:
            return [[0,1],[1,1],[-1,1]]
        
    def rook_movements(self):
        return [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0]]

chess_team('White')
chess_team('Black')