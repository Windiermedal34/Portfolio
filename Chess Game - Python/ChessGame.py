class chess_game():

    def __init__(self):
        print('Chess Game')
        self.setting_up_game()
        self.play_game()

    def setting_up_game(self):
        print('Setting Up The Game')
        self.game_board = chess_board()

    def play_game(self):
        print('Playing The Game')
        flag = True
        teams = self.game_board.retrieve_teams()
        while (flag):
            for team in teams:
                print('-------------------------------')
                print(f"{team.team_colour} Team's Turn")
                print('------N-------------------------')
                decision = self.display_menu()
                if decision == 'S':
                    break
                piece = team.select_piece()
                piece.move_piece()
            break
        print("Game Over")

    def display_menu(self):
        decision = ""
        flag = True
        board_flag = False
        while flag:
            if not board_flag:
                print("MENU:\n - Display Board (D)\n - Move Piece (M)\n - Surrender (S):")
            else:
                print("MENU:\n - Move Piece (M)\n - Surrender (S):")
            try:
                decision = input("Select 'D', 'M' or 'S': ").upper()
            except Exception:
                print("Error Occured")
                continue
            if decision == 'D':
                board_flag = True
                self.game_board.print_board()
                continue
            elif decision == 'M' or decision == 'S':
                flag = False
        return decision

class chess_board():

    board = [
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['','','','','','','',''],
        ['','','','','','','','']
        ]

    def __init__(self):
        self.team_one = chess_team('White')
        self.team_two = chess_team('Black')
        self.populate_board()

    def retrieve_teams(self):
        return self.team_one,self.team_two

    def populate_board(self):
        for k, v in self.team_one.team_pieces.items():
            if len(v) == 1:
                x,y = v[0].piece_current_location
                self.board[x][y] = f'{v[0].piece_colour} {k}'
            else:
                for piece in v:
                    x,y = piece.piece_current_location
                    self.board[x][y] = f'{piece.piece_colour} {k}'
        for k, v in self.team_two.team_pieces.items():
            if len(v) == 1:
                x,y = v[0].piece_current_location
                self.board[x][y] = f'{v[0].piece_colour} {k}'
            else:
                for piece in v:
                    x,y = piece.piece_current_location
                    self.board[x][y] = f'{piece.piece_colour} {k}'

    def print_board(self):
        print('--------------------------------------')
        for row in self.board:
            print(row)
        print('--------------------------------------')

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

    def select_piece(self):
        for role in self.team_pieces.keys():
            print(role)
        select_role = str(input("Select the role of a piece you would like to move."))
        piece_list = self.team_pieces[select_role]
        print(f"{select_role}s")
        for piece in piece_list:
            print(piece)
        select_piece = int(input(f"Select which {select_role} you would like to move."))
        return piece_list[select_piece-1]

    def show_pieces(self):
        for piece_role,piece_list in self.team_pieces.items():
            print(f"{piece_role}s")
            if len(piece_list) == 1:
                piece = piece_list[0]
                piece.print_piece_short()
            else:
                for piece in piece_list:
                    piece.print_piece_short()

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

    starting_locations = {
        "White": {
            "King": [0,4],
            "Queen": [0,3],
            "Bishop": [[0,2],[0,5]],
            "Knight": [[0,1],[0,6]],
            "Rook": [[0,0],[0,7]],
            "Pawn": [[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
        },
        "Black": {
            "King": [7,4],
            "Queen": [7,3],
            "Bishop": [[7,2],[7,5]],
            "Knight": [[7,1],[7,6]],
            "Rook": [[7,0],[7,7]],
            "Pawn": [[6,0],[6,1],[6,2],[6,3],[6,4],[6,5],[6,6],[6,7]]
        }
    }

    def __init__(self, colour, role, movements, no):
        self.piece_colour = colour
        self.piece_role = role
        self.piece_movement = movements
        self.piece_no = no
        self.piece_current_location = self.piece_starting_location()
        self.status = 'Active'

    def __str__(self):
        return (f'{self.piece_no} - {self.piece_role} {self.piece_no} - Current Location: {self.piece_current_location}')
    
    def piece_defeated(self):
        self.status = 'Defeated'

    def move_piece(self):
        print(f"Current Location: {self.piece_current_location}\nWhere would you like to move:")
        for move in self.piece_movement:
            new_location = [self.piece_current_location[0] + move[0],self.piece_current_location[1] + move[1]]
            if new_location[0] < 0 or new_location[0] > 7 or new_location[1] < 0 or new_location[1] > 7:
                continue
            print(f"-{new_location}")


    def piece_starting_location(self):
        locations = self.starting_locations[self.piece_colour][self.piece_role]
        if self.piece_role == 'King' or self.piece_role == 'Queen':
            return locations
        else:
            return locations[self.piece_no-1]
        #if self.piece_role == 'King':
            #if self.piece_colour == 'White':
                #return [0,4]
            #else:
                #return [7,4]
        #elif self.piece_role == 'Queen':
            #if self.piece_colour == 'White':
                #return [0,3]
            #else:
                #return [7,3]
        #elif self.piece_role == 'Bishop':
            #if self.piece_no == 1:
                #if self.piece_colour == 'White':
                    #return [0,2]
                #else:
                    #return [7,2]
            #else:
                #if self.piece_colour == 'White':
                    #return [0,5]
                #else:
                    #return [7,5]
        #elif self.piece_role == 'Knight':
            #if self.piece_no == 1:
                #if self.piece_colour == 'White':
                    #return [0,1]
                #else:
                    #return [7,1]
            #else:
                #if self.piece_colour == 'White':
                    #return [0,6]
                #else:
                    #return [7,6]
        #elif self.piece_role == 'Rook':
            #if self.piece_no == 1:
                #if self.piece_colour == 'White':
                    #return [0,0]
                #else:
                    #return [7,0]
            #else:
                #if self.piece_colour == 'White':
                    #return [0,7]
                #else:
                    #return [7,7]
        #else:
            #if self.piece_colour == 'White':
                #return [1,self.piece_no-1]
            #else:
                #return [6,self.piece_no-1]
            
my_game = chess_game()