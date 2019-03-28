#!/usr/bin/env python3

from pathlib import Path
import random


meditation_book = [
    "FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", "SIXTH",
    "SEVENTH", "EIGHTH", "NINTH", "TENTH", "ELEVENTH", "TWELFTH"
    ]
meditations_per_book = [17, 15, 17, 43, 33, 54, 44, 58, 43, 38, 31, 27]


class RomanNumerals:
    """Takes an index from 1 to 57 and returns corresponding Roman Numeral
    
    >>> roman_numerals = RomanNumerals()
    >>> roman_numerals[1]
    'I'
    >>> roman_numerals[33]
    'XXXIII'
    """

    def __init__(self):
        self._roman_numerals: list = [
            "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI",
            "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
            "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII",
            "XXIX", "XXX", "XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI",
            "XXXVII", "XXXVIII", "XXXIX", "XL", "XLI", "XLII", "XLIII", "XLIV",
            "XLV", "XLVI", "XLVII", "XLVIII", "XLIX", "L", "LI", "LII", "LIII",
            "LIV", "LV", "LVI", "LVII", "LVIII"]

    def __getitem__(self, index: int):
        return self._roman_numerals[index - 1]


if __name__ == '__main__':

    this_dir: Path = Path(__file__).resolve().parent
    file_path: Path = this_dir / "meditations" / "Meditations.txt"

    random_book_number: int = random.randint(1, 12)
    random_meditation_number: int = random.randint(1, meditations_per_book[random_book_number - 1])

    book_found: bool = False
    meditation_found: bool = False
    meditation: str = ""
    roman_numerals = RomanNumerals()

    with open(file_path) as meditations_text:

        for line in meditations_text:
            if "THE " + meditation_book[random_book_number - 1] + " BOOK" in line:
                book_found = True

            if book_found and roman_numerals[random_meditation_number] + "." in line:
                meditation_found = True

            if meditation_found:
                if line == '\n':
                    break
                meditation = meditation + line

    print(
        f"Book {random_book_number}\n"
        f"Meditation {random_meditation_number}\n\n"
        f"{meditation}"
    )