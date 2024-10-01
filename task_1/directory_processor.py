from pathlib import Path
import shutil

def process_directory(source_dir: Path, dest_dir: Path):
    # рекурсивно обробляємо директорію
    try:
        for item in source_dir.iterdir():
            if item.is_dir():
                process_directory(item, dest_dir)
            elif item.is_file():
                process_file(item, dest_dir)
    except Exception as e:
        print(f'Помилка при обробці директорії "{source_dir}": {e}')

def process_file(file_path: Path, dest_dir: Path):
    # копіюємо файл до відповідної піддиректорії за розширенням
    try:
        extension = file_path.suffix[1:]
        if not extension:
            extension = 'no_extension'

        # створюємо піддиректорію за розширенням
        dest_subdir = dest_dir / extension # еквівалент dest_dir.joinpath(extension)
        dest_subdir.mkdir(parents=True, exist_ok=True)

        # шлях до файлу в директорії призначення
        dest_file_path = dest_subdir / file_path.name

        shutil.copy2(file_path, dest_file_path)
        print(f'Скопійовано "{file_path}" до "{dest_file_path}"')
    except Exception as e:
        print(f'Помилка при копіюванні файлу "{file_path}": {e}')
