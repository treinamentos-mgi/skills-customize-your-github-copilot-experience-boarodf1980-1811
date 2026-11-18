def is_even(number):
    return number % 2 == 0


def average(numbers):
    if not numbers:
        raise ValueError("a lista não pode estar vazia")
    return sum(numbers) / len(numbers)


def validate_password(password):
    return len(password) >= 8 and any(char.isdigit() for char in password)
