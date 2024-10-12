import time
import psutil


def main():
    rank_mapping = {'6': 0, '7': 1, '8': 2, '9': 3, 'T': 4, 'J': 5, 'Q': 6, 'K': 7, 'A': 8}
    suit_mapping = {'C': 0, 'D': 1, 'H': 2, 'S': 3}

    with open('input.txt', 'r') as fin:
        N_M_trump = fin.readline().strip().split()
        N = int(N_M_trump[0])
        M = int(N_M_trump[1])
        trump_suit = N_M_trump[2]
        player_cards_input = fin.readline().strip().split()
        attacking_cards_input = fin.readline().strip().split()
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
            with open('output.txt', 'w') as fout:
                fout.write("NO")
            return

    with open('output.txt', 'w') as fout:
        fout.write("YES")


if __name__ == "__main__":
    t_start = time.perf_counter()
    main()
    t_end = time.perf_counter()
    print(f"Время работы: {t_end - t_start:.8f} секунд.")
    print(f"Потребление памяти: {psutil.Process().memory_info().rss / (1024 * 1024):.2f} МБ")