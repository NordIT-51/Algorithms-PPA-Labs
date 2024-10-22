import time
import psutil
from utils import readfile, writefile, analyze

def main():
    rank_mapping = {'6': 0, '7': 1, '8': 2, '9': 3, 'T': 4, 'J': 5, 'Q': 6, 'K': 7, 'A': 8}
    suit_mapping = {'C': 0, 'D': 1, 'H': 2, 'S': 3}

    inp = readfile()
    print(inp)
    N_M_trump = inp[0].strip().split()
    N = int(N_M_trump[0])
    M = int(N_M_trump[1])
    trump_suit = N_M_trump[2]
    player_cards_input = inp[1].strip().split()
    attacking_cards_input = inp[2].strip().split()
    player_cards = [[0]*9 for _ in range(4)]

    for card in player_cards_input:
        rank_char = card[:-1]
        suit_char = card[-1]
        rank = rank_mapping[rank_char]
        suit = suit_mapping[suit_char]
        player_cards[suit][rank] = 1

    trump_suit_index = suit_mapping[trump_suit]

    for attack_card in attacking_cards_input:
        attack_rank_char = attack_card[:-1]
        attack_suit_char = attack_card[-1]
        attack_rank = rank_mapping[attack_rank_char]
        attack_suit = suit_mapping[attack_suit_char]
        defended = False

        for defend_rank in range(attack_rank + 1, 9):
            if player_cards[attack_suit][defend_rank]:
                player_cards[attack_suit][defend_rank] = 0
                defended = True
                break
        if not defended:
            if attack_suit != trump_suit_index:
                for defend_rank in range(9):
                    if player_cards[trump_suit_index][defend_rank]:
                        player_cards[trump_suit_index][defend_rank] = 0
                        defended = True
                        break

        if not defended:
            writefile('NO')
            return

    writefile('YES')


if __name__ == "__main__":
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    analyze(t_start, t_end)