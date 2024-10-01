from directory_processor import process_directory
from tree_printer import display_tree
import argparse
from pathlib import Path

def parse_arguments():
    parser = argparse.ArgumentParser(description='Рекурсивне копіювання та сортування файлів за розширенням.')
    parser.add_argument('source_dir', help='Шлях до вихідної директорії.')
    parser.add_argument('dest_dir', nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням "dist").')
    return parser.parse_args()

def main():
    args = parse_arguments()
    source_dir = Path(args.source_dir)
    dest_dir = Path(args.dest_dir)

    if not source_dir.exists():
        print(f'Вихідна директорія "{source_dir}" не існує.')
        return

    dest_dir.mkdir(parents=True, exist_ok=True)

    # виводимо структуру вихідної директорії перед копіюванням
    print("Структура вихідної директорії перед копіюванням:")
    display_tree(source_dir)
    print("\nПочинаємо копіювання...\n")

    # виконуємо копіювання та сортування файлів
    process_directory(source_dir, dest_dir)

    # виводимо структуру директорії призначення після копіювання
    print("\nКопіювання завершено.")
    print("Структура директорії призначення після копіювання:")
    display_tree(dest_dir)

# python3 ./task_1/main.py ./task_1/test_for_copy ./task_1/copy
if __name__ == '__main__':
        main()
