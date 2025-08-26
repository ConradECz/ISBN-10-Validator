def StripDashes(isbn):
    return isbn.replace("-", "")

def CheckFormat(isbn):
    if len(isbn) != 10:
        return False
    if not isbn[:9].isdigit():
        return False
    if not (isbn[9].isdigit() or isbn[9] == 'X'):
        return False
    return True

def isValidISBN(isbn):
    isbn = StripDashes(isbn)
    
    if not CheckFormat(isbn):
        return False

    digits = [int(ch) if ch.isdigit() else 10 for ch in isbn]
    total = sum((10 - i) * digits[i] for i in range(10))
    
    return total % 11 == 0

test_cases = [
    "0-13-030657-6",
    "08748101986",
    "0-471-58719-2",
    "0-123-45678-9",
    "ABCDEFGHI"
]

for isbn in test_cases:
    print(f"ISBN: {isbn} \n -> Valid: {isValidISBN(isbn)}")
