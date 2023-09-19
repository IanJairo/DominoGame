from ClassDomino import *

welcome_message = (
    "Bem-vindo ao Jogo de Dominó!\n\n"
    "Neste jogo, você irá competir com outros jogadores para combinar as peças de dominó e vencer.\n"
    "Cada jogador receberá um conjunto de peças e a partida começa.\n"
    "Você pode jogar com 2 a 8 jogadores.\n\n"
    "Vamos começar!\n"
)


def main():

    is_valid_player_number = False
    print(welcome_message)

    while not is_valid_player_number:
        num_players = int(
            input("Quantos jogadores participarão do jogo de dominó? "))

        if num_players < 2 or num_players > 8:
            print("Número de jogadores inválido. Digite um número entre 2 e 8.\n")
            continue
        is_valid_player_number = True

    domino_set = DominoSet()

    # Criação de todas as peças de dominó
    for i in range(7):
        for j in range(i, 7):
            domino_set.add_piece(i, j)

    # Embaralhar as peças
    domino_set.shuffle()

    players = []
    players_names = []

    while len(players) < num_players:
        player_name = input(f"Nome do jogador {len(players)+1}: ")

        if player_name in players_names:
            print("Já existe um jogador com esse nome. Digite outro nome.\n")
            continue

        players.append(Player(player_name))
        players_names.append(player_name)

    # Distribuir peças aos jogadores
    num_pieces_per_player = len(list(domino_set)) // num_players
    for player in players:
        for _ in range(num_pieces_per_player):
            player.draw_piece(domino_set)

    board = DominoBoard()

    while True:
        # Inicialmente, suponha que todos os jogadores não podem jogar
        all_players_cannot_play = True
        skipped_players = 0  # Número de jogadores que passaram a vez

        for player in players:
            if not player.skipped_turn:
                # Se pelo menos um jogador não pulou o turno, altere para False
                all_players_cannot_play = False

            print(" ")
            print(" ==== ==== ==== ")
            print(f"Tabuleiro: {board}")
            print(" ==== ==== ==== ")
            print(" ")

            print(
                f"\nMão de {player.name}: {', '.join(f'[{piece.value1}:{piece.value2}]' for piece in player.hand)}")

            if not player.skipped_turn:
                while True:
                    try:

                        print(" ")
                        print(" - - - - - - - - ")
                        print(" ")

                        piece_index = int(input(
                            f"{player.name}, escolha uma peça para jogar (0-{len(list(player.hand)) - 1}) ou pule sua vez (-1): "))

                        if piece_index == -1:
                            if player.can_play_piece(board):
                                print(
                                    "Você não pode passar a vez porque tem pelo menos uma peça que pode ser jogada.")

                                continue
                            else:
                                player.skip_turn()
                                skipped_players += 1
                            break

                        piece = list(player.hand)[piece_index]

                        if player.play_piece(piece, board):
                            break
                        else:
                            print("Jogada inválida. Escolha outra peça.")
                    except (ValueError, IndexError):
                        print(
                            "Entrada inválida. Digite o número correspondente à peça que deseja jogar ou -1 para pular sua vez.")

            if len(list(player.hand)) == 0:
                print(f"{player.name} venceu o jogo!")
                return

            # Resetar o turno do jogador
            player.reset_turn()

        if skipped_players == len(players):
            print("Todos os jogadores passaram a vez. O jogo termina em empate.")
            return


if __name__ == "__main__":
    main()
''
