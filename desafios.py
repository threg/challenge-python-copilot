# Desafio 1: Crie uma função que recebe um número como parâmetro e retorna se ele é primo.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(11))  # True
print(is_prime(4))   # False

# Desafio 2: Crie uma função que recebe uma lista de números e retorna a soma dos números pares.
def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)
print(sum_even_numbers([1, 2, 3, 4, 5, 6]))  # 12

# Desafio 3: Crie uma função que recebe uma string e retorna a string invertida.
def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))  # "olleh"

# Desafio 4: Crie uma função que recebe uma lista de strings e retorna a
# lista ordenada por comprimento das strings.
def sort_by_length(strings):
    return sorted(strings, key=len)
print(sort_by_length(["apple", "banana", "kiwi", "cherry"]))  # ['kiwi', 'apple', 'cherry', 'banana']

# Desafio 5: Crie uma função que recebe um número e retorna a soma de
# todos os números de 1 até esse número.
def sum_up_to(n):
    return sum(range(1, n + 1))
print(sum_up_to(5))  # 15

# Desafio 6: Crie uma função que recebe uma lista de números e retorna
# a média dos números.
def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
print(average([1, 2, 3, 4, 5]))  # 3.0

# Desafio 7: Crie uma função que recebe uma string e retorna a contagem de vogais na string.
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
print(count_vowels("hello world"))  # 3

# Desafio 8: Crie uma função que recebe uma lista de números e retorna a lista sem números duplicados.
def remove_duplicates(numbers):
    return list(set(numbers))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]