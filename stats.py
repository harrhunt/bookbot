def count_words(text: str) -> int:
    return len(text.split())


def count_chars(text: str) -> dict[str, int]:
    result = {}
    for c in text:
        char = c.lower()
        if char not in result:
            result[char] = 0
        result[char] += 1
    return result


def sort_char_count(chars: dict[str, int]) -> list[dict[str, str | int]]:
    result: list[dict[str, str | int]] = [
        {"char": k, "num": v} for k, v in chars.items()
    ]
    result.sort(reverse=True, key=lambda x: x.get("num", 0))
    return result
