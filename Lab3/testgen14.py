def generate_maxinput14():
    N = 100  # Общее число деревень
    d = 1  # Номер начальной деревни
    v = N  # Номер конечной деревни
    R = 10000  # Количество автобусных рейсов

    with open('maxinput14.txt', 'w') as f:
        f.write(f"{N} {d} {v}\n")
        f.write(f"{R}\n")

        for i in range(1, R + 1):
            departure_village = (i % N) + 1  # Номер деревни отправления (цикличное распределение)
            departure_time = i % 10001  # Время отправления (обеспечиваем, что оно в пределах 0-10000)
            arrival_village = ((i + 1) % N) + 1  # Номер деревни назначения
            arrival_time = (departure_time + 1) % 10001  # Время прибытия (всегда позже времени отправления)

            f.write(f"{departure_village} {departure_time} {arrival_village} {arrival_time}\n")


generate_maxinput14()
