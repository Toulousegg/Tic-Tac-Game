import random

def JuegoTic_Tac():
    #jugador1 = input('Jugador 1, dime tu nombre: ')
    #jugador2 = input('Jugador 2, dime tu nombre: ')
    
    print('Disfruten,')
    class TicTacToe:

        def __init__(self):
            self.board = []

        def create_board(self):
            for i in range(3):
                row = []
                for j in range(3):
                    row.append('-')
                self.board.append(row)

        def get_random_first_player(self):
            return random.randint(0, 1)

        def fix_spot(self, row, col, player):
            self.board[row][col] = player

        def is_player_win(self, player):
            win = None

            n = len(self.board)

            # checking rows
            for i in range(n):
                win = True
                for j in range(n):
                    if self.board[i][j] != player:
                        win = False
                        break
                if win:
                    return win

            # checking columns
            for i in range(n):
                win = True
                for j in range(n):
                    if self.board[j][i] != player:
                        win = False
                        break
                if win:
                    return win

            # checking diagonals
            win = True
            for i in range(n):
                if self.board[i][i] != player:
                    win = False
                    break
            if win:
                return win

            win = True
            for i in range(n):
                if self.board[i][n - 1 - i] != player:
                    win = False
                    break
            if win:
                return win
            return False

            for row in self.board:
                for item in row:
                    if item == '-':
                        return False
            return True

        def is_board_filled(self):
            for row in self.board:
                for item in row:
                    if item == '-':
                        return False
            return True

        def swap_player_turn(self, player):
            return 'X' if player == 'O' else 'O'

        def show_board(self):
            for row in self.board:
                for item in row:
                    print(item, end=" ")
                print()

        def start(self):
            self.create_board()

            player = 'X' if self.get_random_first_player() == 1 else 'O'
            while True:
                print('Turno de ' + player)

                self.show_board()

                # taking user input
                row, col = list(
                    map(int, input("Ingrese los números de fila y columna para fijar el lugar: ").split()))
                print()

                # fixing the spot
                self.fix_spot(row - 1, col - 1, player)

                # checking whether current player is won or not
                if self.is_player_win(player):
                    print(player + ' gana el juego')
                    break

                # checking whether the game is draw or not
                if self.is_board_filled():
                    print("Empate")
                    break

                # swapping the turn
                player = self.swap_player_turn(player)

            # showing the final view of board
            print()
            self.show_board()


    # starting the game
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()

print('Hola, ¿como te llamas?')

nombre =  input('Dime tu nombre: ')

print('Mucho gusto ' + nombre + ', ¿como va tu día?')

respuesta = input('(Responde con "Bien" o "Mal"): ')

if respuesta == 'bien':
    print('Me alegro muchisimo, ¿quieres jugar un juego?')
    invitación = input('(Responde con un "Si" o un "No"): ')

    if invitación == 'si':
        print('Ok, vamos a jugar Tic-Tac, ¿sabes en que consiste?')
        RespuestaJuego = input('Responde con un "Si" o con un "No": ')

        if RespuestaJuego == 'si':
                #ACÁ SE VA A EJECUTAR EL JUEGO PERO AÚN NO LO TENGO
            print('Vamos a jugar, llama a un amigo y empecemos (Para poner un simbolo escribe primero el número de la columna y después el de la fila)')
            JuegoTic_Tac()
            print('¿Quieres jugar otra vez?')
            IniciarOtraVez = input('Responde con un "Si" o con un "No": ')

            while IniciarOtraVez == 'si':
                JuegoTic_Tac()
                print('¿Quieres jugar otra vez?')

        elif RespuestaJuego == 'no':
            print('Cada jugador solo debe colocar su símbolo una vez por turno y no debe ser sobre una casilla ya jugada. En caso de que el jugador haga trampa el ganador será el otro. Gana el jugador que primero consiga una línea recta o diagonal del mismo simbolo')
            input('Presiona enter cuando hayas terminado de leer las instrucciones')
            print('Dicho esto, vamos a empezar')
            JuegoTic_Tac()
            print('¿Quieres jugar otra vez?')
            IniciarOtraVez = input('Responde con un "Si" o con un "No": ')

            while IniciarOtraVez == 'si':
                JuegoTic_Tac()
                print('¿Quieres jugar otra vez?')
                

    elif invitación == 'no':
        print('Bueno, no cumplí mi misión, adiós') #Acá se tiene que cerrar auto

elif respuesta == 'mal':
    print(':(, ¿quieres contarme que pasa?')
    desahogarte = input('Responde con un "Si" o un "No": ')

    if desahogarte == 'si':
        problema = input('Cuentame que pasa, no te guardes nada (esta conversación será eliminada): ')

        if 'soy un' 'todo es mi culpa' 'yo' 'casa' 'malos' 'estupidos' 'burlan' 'bullying' 'bully' 'bullys' in problema:
            print('Tranquilo, todo lo que debe pasar pasara en su momento, mientras tanto espera pacientemente que todas las cosas tienen su solución y recuerda que te quiero mucho y estoy muy orgulloso de ti, eres un/a maravillosa persona, pasa un buen día')
            
            input('Presiona enter cuando hayas terminado de leer')
            print('¿Quieres jugar o prefieres salir?')

            prefiero = input('Escribe que prefieres: ')

            if prefiero == 'jugar':
                JuegoTic_Tac()

            elif prefiero == 'salir': #Acá se debería salir auto
                print('Adiós, ' + nombre) 

        elif problema:
            print('Gracias por confiar en mi, sinceramente no se que escribiste, pero, ¿sabes quien si lo sabe y acaba de drenar todo ese rencor, odio, tristeza, rabia y/o frustación?, tu, la escritura es una de las formas más efectivas de desahogarse y espero haber sido de ayuda, eres una persona maravillosa y se que todo lo que hagas te saldra muy bien, te deseo lo mejor')
            
            input('Presiona enter cuando hayas terminado de leer')
            print('¿Quieres jugar o prefieres salir?')

            prefiero = input('Escribe que prefieres: ')

            if prefiero == 'jugar':
                JuegoTic_Tac()

            elif prefiero == 'salir': #Acá se debería salir auto
                print('Adiós, ' + nombre)
    elif desahogarte == 'no':
        print('Ok, si quieres mantenerlo en secreto no hay problema, siempre contaras conmigo. ¿Quieres jugar o prefieres salir?')
            
        prefiero = input('Escribe que prefieres: ')

        if prefiero == 'jugar':
            JuegoTic_Tac

        elif prefiero == 'salir': #Acá se debería salir auto
            print('Adiós, ' + nombre)