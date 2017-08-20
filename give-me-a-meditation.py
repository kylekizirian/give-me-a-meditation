import os
import random

meditation_book = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", "SIXTH", "SEVENTH", "EIGHTH", "NINTH", "TENTH",
                   "ELEVENTH", "TWELFTH"]
meditations_per_book = [17, 15, 17, 43, 33, 54, 44, 58, 43, 38, 31, 27]
roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XII", "XIV", "XV", "XVI",
                  "XVII", "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII",
                  "XXIX", "XXX", "XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI", "XXXVII", "XXXVIII", "XXXIX",
                  "XL", "XLI", "XLII", "XLIII", "XLIV", "XLV", "XLVI", "XLVII", "XLVIII", "XLIX", "L", "LI", "LII",
                  "LIII", "LIV", "LV", "LVI", "LVII", "LVIII"]

file_path = os.path.join(os.curdir, "meditations", "Meditations.txt")
meditations_text = open(file_path)

random_book_number = random.randint(1, 12)
random_meditation_number = random.randint(1, meditations_per_book[random_book_number - 1])
print("Book " + str(random_book_number))
print("Meditation " + str(random_meditation_number) + "\n")

book_found = False
meditation_found = False
meditation = ""

for line in meditations_text:

    if "THE " + meditation_book[random_book_number - 1] + " BOOK" in line:
        book_found = True

    if book_found and roman_numerals[random_meditation_number-1] + "." in line:
        meditation_found = True

    if meditation_found:
        if line == '\n':
            break

        meditation = meditation + line

print(meditation)
meditations_text.close()
