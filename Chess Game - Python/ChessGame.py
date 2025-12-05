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
        first_turn = True
        flag = True
        teams = self.game_board.retrieve_teams()
        while (flag):
            for team in teams:
                print('-------------------------------')
                print(f"{team.team_colour} Team's Turn")
                print('------N-------------------------')
                decision = self.display_menu()
                if decision == 'S':
                    flag = False
                    break
                piece = team.select_piece()
                piece_moves = piece.moves(first_turn)
                enemy_pieces = [piece for piece in piece_moves if self.game_board.board[piece[0]][piece[1]] != '']
                if team.team_colour == 'White':
                    enemy_pieces = self.game_board.black_positions()
                else:
                    enemy_pieces = self.game_board.white_positions()
                x,y = piece.piece_current_location
                x1,y1 = None,None
                x2,y2 = None,None
                if piece.piece_role == 'Pawn':
                    if piece.piece_colour == 'White':
                        if x < 7:
                            if y < 7:
                                x1,y1 = (x+1),(y+1)
                            if y > 0:
                                x2,y2 = (x+1),(y-1)
                            if (x1 != None and self.game_board.board[x1][y1] != '') or (x2 != None and self.game_board.board[x2][y2] != ''):
                                print("Attacking")
                                enemies = [enemy for enemy in [self.game_board.board[x1][y1],self.game_board.board[x2][y2]] if enemy != '']
                                for enemy in enemies:
                                    print(f'- {enemy}:{enemy.piece_current_location}')
                                piece.attack_piece(first_turn,enemies)
                            else:
                                piece.move_piece(first_turn)
                    else:
                        if x > 0:
                            if y < 7:
                                x1,y1 = (x-1),(y+1)
                            if y > 0:
                                x2,y2 = (x-1),(y-1)
                            if (x1 != None and self.game_board.board[x1][y1] != '') or (x2 != None and self.game_board.board[x2][y2] != ''):
                                print("Attacking")
                                enemies = [enemy for enemy in [self.game_board.board[x1][y1],self.game_board.board[x2][y2]] if enemy != '']
                                for enemy in enemies:
                                    print(f'- {enemy}:{enemy.piece_current_location}')
                                piece.attack_piece(first_turn,enemies)
                            else:
                                piece.move_piece(first_turn)
                elif piece.piece_role == 'Rook':
                    rook_moves = {}
                    board = self.game_board.board
                    message = ""

                    for i in range(x+1,8):
                        
                        
                        if board[i][y] == '':
                            message = "empty"
                        else:
                            if board[i][y].piece_colour == piece.piece_colour:
                                message = f"Ally {board[i][y].piece_role}"
                            else:
                                message = f"Enemy {board[i][y].piece_role}"
                        rook_moves[i,y] = message

                    for i in range(x-1,-1,-1):
                        if board[i][y] == '':
                            message = "empty"
                        else:
                            if board[i][y].piece_colour == piece.piece_colour:
                                message = f"Ally {board[i][y].piece_role}"
                            else:
                                message = f"Enemy {board[i][y].piece_role}"
                        rook_moves[i,y] = message

                    for i in range(y+1,8):
                        if board[x][i] == '':
                            message = "empty"
                        else:
                            if board[x][i].piece_colour == piece.piece_colour:
                                message = f"Ally {board[x][i].piece_role}"
                            else:
                                message = f"Enemy {board[x][i].piece_role}"
                        rook_moves[x,i] = message

                    for i in range(y-1,-1,-1):
                        if board[x][i] == '':
                            message = "empty"
                        else:
                            if board[x][i].piece_colour == piece.piece_colour:
                                message = f"Ally {board[x][i].piece_role}"
                            else:
                                message = f"Enemy {board[x][i].piece_role}"
                        rook_moves[x,i] = message
                elif piece.piece_role == 'Bishop':
                    bishop_moves = {}
                    board = self.game_board.board
                    message = ""

                    for i in range(1,8):

                        new_x = x+i
                        new_y = y+i

                        if new_x <= 7 and new_y <= 7:
                            if board[new_x][new_y] == '':
                                message = "empty"
                            else:
                                if board[new_x][new_y].piece_colour == piece.piece_colour:
                                    message = f"Ally {board[new_x][new_y].piece_role}"
                                else:
                                    message = f"Enemy {board[new_x][new_y].piece_role}"
                            bishop_moves[new_x,new_y] = message

                        new_y = y-i

                        if new_x <= 7 and new_y >= 0:
                            if board[new_x][new_y] == '':
                                message = "empty"
                            else:
                                if board[new_x][new_y].piece_colour == piece.piece_colour:
                                    message = f"Ally {board[new_x][new_y].piece_role}"
                                else:
                                    message = f"Enemy {board[new_x][new_y].piece_role}"
                            bishop_moves[new_x,new_y] = message

                        new_x = x-i
                        new_y = y+i

                        if new_x >= 0 and new_y <= 7:
                            if board[new_x][new_y] == '':
                                message = "empty"
                            else:
                                if board[new_x][new_y].piece_colour == piece.piece_colour:
                                    message = f"Ally {board[new_x][new_y].piece_role}"
                                else:
                                    message = f"Enemy {board[new_x][new_y].piece_role}"
                            bishop_moves[new_x,new_y] = message

                        new_y = y-i

                        if new_x >= 0 and new_y >= 0:
                            if board[new_x][new_y] == '':
                                message = "empty"
                            else:
                                if board[new_x][new_y].piece_colour == piece.piece_colour:
                                    message = f"Ally {board[new_x][new_y].piece_role}"
                                else:
                                    message = f"Enemy {board[new_x][new_y].piece_role}"
                            bishop_moves[new_x,new_y] = message

                    print(bishop_moves)
                elif piece.piece_role == 'Knight':
                    enemies = []


                else:
                    piece.move_piece(first_turn)
                self.game_board.update_board()
                if first_turn:
                    first_turn = False
            
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
                if not board_flag:
                    decision = input("Select 'D', 'M' or 'S': ").upper()
                else:
                    decision = input("Select 'M' or 'S': ").upper()
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
                self.board[x][y] = v[0]
            else:
                for piece in v:
                    x,y = piece.piece_current_location
                    self.board[x][y] = piece
        for k, v in self.team_two.team_pieces.items():
            if len(v) == 1:
                x,y = v[0].piece_current_location
                self.board[x][y] = v[0]
            else:
                for piece in v:
                    x,y = piece.piece_current_location
                    self.board[x][y] = piece

    def update_board(self):
        self.board = [['' for _ in range(8)] for _ in range(8)]
        self.populate_board()

    def white_positions(self):
        white_pieces = []
        for row in self.board:
            for piece in row:
                if piece.piece_colour == 'White':
                    white_pieces.append(piece)
                else:
                    continue
    
    def black_positions(self):
        black_pieces = []
        for row in self.board:
            for piece in row:
                if piece.piece_colour == 'Black':
                    black_pieces.append(piece)
                else:
                    continue
    
    def print_board(self):
        print('--------------------------------------')
        for row in self.board:
            row_str = [str(r) for r in row]
            print(row_str)
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
            print(f"- {role}")
        select_role = str(input("Which piece would you would like to move: "))
        piece_list = self.team_pieces[select_role]
        print(f"{select_role}s")
        for piece in piece_list:
            print(piece.more_piece_info())
        select_piece = int(input(f"Which {select_role} piece would you like to move: "))
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
            [0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],
            [-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],
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
            [1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],
            [0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],
            [-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0]
            ]
        if self.team_colour == 'White':
            piece_movements['Pawn'] = [[2,0],[1,0],[1,1],[1,-1]]
        else:
            piece_movements['Pawn'] = [[-1,0],[-1,1],[-1,-1]]

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

    pawn_attack_moves = [[1,1],[1,-1],[-1,1],[-1,-1]]

    def __init__(self, colour, role, movements, no):
        self.piece_colour = colour
        if colour == 'White':
            self.enemy_colour = "Black"
        else:
            self.enemy_colour = 'White'
        self.piece_role = role
        self.piece_movement = movements
        self.piece_no = no
        self.piece_current_location = self.piece_starting_location()
        self.status = 'Active'
        self.attack = False
    
    def __str__(self):
        return f"{self.piece_colour} {self.piece_role}"
    
    def more_piece_info(self):
        return (f'{self.piece_no} - {self.piece_role} {self.piece_no} - Current Location: {self.piece_current_location}')
        
    def attack_piece(self, first_turn, enemies = None):
        self.attack = True
        moves = self.move_piece(first_turn, enemies)
        self.attack = False
        return moves
    
    def piece_defeated(self):
        self.status = 'Defeated'

    def move_piece(self,first_turn,enemies = None):
        possible_moves = []
        print(f"Current Location: {self.piece_current_location}\nPotential Movements:")
        move_index = 1
        for move in self.piece_movement:
            if move == [2,0] and self.piece_role == 'Pawn' and not first_turn:
                continue
            if move in self.pawn_attack_moves and self.attack == False:
                continue
            new_location = [self.piece_current_location[0] + move[0],self.piece_current_location[1] + move[1]]

            if enemies != None:
                enemy_locations = [enemy.piece_current_location for enemy in enemies]
                if new_location not in enemy_locations and move in self.pawn_attack_moves:
                    continue

            if new_location[0] < 0 or new_location[0] > 7 or new_location[1] < 0 or new_location[1] > 7:
                continue
            possible_moves.append(new_location)
            print(f"-{new_location} ({move_index})")
            move_index += 1
        new_location = int(input("Which would you like to move to: "))
        print(f"New Location = {possible_moves[new_location-1]}")
        self.piece_current_location = possible_moves[new_location-1]

    def attack_moves(self,first_turn,enemies):
        self.attack = True
        moves = self.move_piece(first_turn, enemies)
        self.attack = False
        return moves

    def potential_moves(self,first_turn,enemies):
        moves = []
        for move in self.moves(first_turn):
            enemy_locations = [enemy for enemy in enemies]
            if move not in enemy_locations and move in self.pawn_attack_moves and self.piece_role == 'Pawn':
                continue
            moves.append(move)
        return moves
    
    def moves(self,first_turn,enemies=None):
        moves = []
        for move in self.piece_movement:
            if move in self.pawn_attack_moves and not self.attack:
                continue
            if move == [2,0] and self.piece_role == 'Pawn' and not first_turn:
                continue
            new_location = [self.piece_current_location[0] + move[0], self.piece_current_location[1] + move[1]]

            if enemies != None:
                enemy_locations = [enemy for enemy in enemies]
                if new_location not in enemy_locations and move in self.pawn_attack_moves and self.piece_role == 'Pawn':
                    continue

            if new_location[0] < 0 or new_location[0] > 7 or new_location[1] < 0 or new_location[1] > 7:
                continue
            moves.append(new_location)
        return moves

    def piece_starting_location(self):
        locations = self.starting_locations[self.piece_colour][self.piece_role]
        if self.piece_role == 'King' or self.piece_role == 'Queen':
            return locations
        else:
            return locations[self.piece_no-1]
            
my_game = chess_game()