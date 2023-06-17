# using luhn's algorithm

def credit_card_validator(card_num):
    sum = 0
    for idx, i in enumerate(card_num):

        digit_sum = 0
        if idx % 2 == 0:
            print(idx, i)
            digit_sum = int(i)*2
            if sum >= 10:
                digit_sum = sum(int(digit) for digit in str(digit_sum))
            sum += digit_sum
        else:
            sum += int(i)
    print(sum)


credit_card_validator("12345678901")
