def solution(phone_book):
    answer = True
    phone_book_dict = {}
    for phone_num in phone_book:
        phone_book_dict[phone_num] = 1
    
    for phone_num in phone_book:
        for i in range(1, len(phone_num)):
            if phone_book_dict.get(phone_num[:i]):
                return False
    return answer