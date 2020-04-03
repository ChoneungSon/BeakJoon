def solution(phone_book):
    for i in range(len(phone_book)):
        n = len(phone_book[i])
        for j in range(len(phone_book)):
            if j != i and n <= len(phone_book[j]) and phone_book[:n] == phone_book[i]: return False
    return True