import random
import string

def create_random_file(filename, lines_count=101, line_length=120):
    """Створює файл з випадковими літерами."""
    with open(filename, "w", encoding="utf-8") as f:
        for _ in range(lines_count):
            # генеруємо рядок зі 120 випадкових букв
            line = ''.join(random.choice(string.ascii_lowercase) for _ in range(line_length))
            f.write(line + "\n")


def count_pairs(filename, pairs_list_per_line):
    """Генератор, який рахує пари букв всередині рядків."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_index, line in enumerate(f):

                # беремо свої 3 пари для цього рядка
                pairs = pairs_list_per_line[line_index]
                pair_counts = {p: 0 for p in pairs}

                # ділимо тільки по словах (хоч у нас немає пробілів — але залишаю для відповідності умові)
                words = line.strip().split()

                for word in words:
                    word = word.lower()
                    for i in range(len(word) - 1):
                        pair = word[i:i+2]
                        if pair in pair_counts:
                            pair_counts[pair] += 1

                yield pair_counts

    except Exception as e:
        print(f"Помилка: {e}")
        return


def main():
    FILE = "random_text.txt"

    # 1. Створення файлу на 101 рядок
    create_random_file(FILE)

    # 2. Генеруємо списки з 3 букв-пар для кожного рядка (всі різні)
    all_pairs = []
    letters = string.ascii_lowercase

    for _ in range(101):
        three_pairs = set()
        while len(three_pairs) < 3:
            pair = random.choice(letters) + random.choice(letters)
            three_pairs.add(pair)
        all_pairs.append(list(three_pairs))

    # 3. Підрахунок
    result = count_pairs(FILE, all_pairs)

    for i, res in enumerate(result, start=1):
        print(f"Рядок №{i}, пари {all_pairs[i-1]}: {res}")


if name == "__main__":
    main()