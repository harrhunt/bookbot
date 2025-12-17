import sys
from pathlib import Path

from stats import count_chars, count_words, sort_char_count


def get_book_text(path: str | Path) -> str:
    if isinstance(path, str):
        path = Path(path)
    with path.open() as file:
        return file.read()


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    num_chars = count_chars(text)
    sorted_chars = sort_char_count(num_chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        if entry["char"].isalpha():  # type: ignore[union-attr]
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
