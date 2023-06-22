# using luhn's algorithm
# consider 11 digits of credit card number
# at odd positions, double the digit. If it goes higher than 10, split them and add together
# at even positions, keep as is.
# keep adding until you get final sum
# if final sum modulo 10 is 0, return valid. else invalid

def break_and_add(number):
    s = 0
    for digit in str(number):
        s += int(digit)
    return s


def credit_card_validator(card_num):
    check_sum = 0
    for idx, i in enumerate(card_num):

        digit_sum = 0
        if idx % 2 != 0:
            # at odd position
            digit_sum = int(i)*2
            if digit_sum >= 10:
                digit_sum = break_and_add(digit_sum)
            check_sum += digit_sum
        else:
            # at even position
            check_sum += int(i)
    if check_sum % 10 == 0:
        print("Credit card valid")
    else:
        print("Credit card not valid")


credit_card_validator("79927398711")
