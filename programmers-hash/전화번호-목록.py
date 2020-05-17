def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            if phone_book[i]==phone_book[j][:len(phone_book[i])]:
                return False
            if phone_book[j]==phone_book[i][:len(phone_book[j])]:
                return False
    return True
