import json
import os


def read_text_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().strip()


def file_exists(file_path: str) -> bool:
    return os.path.isfile(file_path)


def save_json_file(data: dict, file_path: str) -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)