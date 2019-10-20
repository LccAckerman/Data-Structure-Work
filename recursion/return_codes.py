# Problem statement
# In an encryption system where ASCII lower case letters represent numbers in the pattern a=1, b=2, c=3... and so on, find out all the codes that are possible for a given input number.
#
# Example 1
#
# number = 123
# codes_possible = ["aw", "abc", "lc"]
# Explanation: The codes are for the following number:
#
# 1 . 23 = "aw"
# 1 . 2 . 3 = "abc"
# 12 . 3 = "lc"
# Example 2
#
# number = 145
# codes_possible = ["ade", "ne"]
# Return the codes in a list. The order of codes in the list is not important.
#
# Note: you can assume that the input number will not contain any 0s


def all_codes(number):
    """n
    :param: number - input integer
    Return - list() of all codes possible for this number
    TODO: complete this method and return a list with all possible codes for the input number
    """
    if number == 0:
        print("hit the base, return """)
        return [""]

    # calculation for two right-most digits e.g. if number = 1123, this calculation is meant for 23
    remainder = number % 100
    output_100 = list()
    print("part 1")
    print("remainder:", remainder, "number:", number)
    if remainder <= 26 and number > 9:
        # get all codes for the remaining number
        print("number//100:", number//100)
        output_100 = all_codes(number//100)
        alphabet = get_alphabet(remainder)
        print("get alphabet:", alphabet)
        for index, element in enumerate(output_100):
            output_100[index] = element + alphabet
    # calculation for right-most digit e.g. if number = 1123, this calculation is meant for 3
    print("part2")
    remainder = number % 10
    print("remainder", remainder, "number:",number)
    # get all codes for the remaining number
    print("number//10:", number//10)
    output_10 = all_codes(number//10)
    alphabet = get_alphabet(remainder)
    print("get alphabet2:", alphabet)
    for index, element in enumerate(output_10):
        output_10[index] = element + alphabet

    output = list()
    output.extend(output_100)
    output.extend(output_10)

    return output

def get_alphabet(number):
    return chr(number + 96)

a = 123
all_codes(a)