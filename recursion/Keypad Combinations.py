def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):
    if num <= 1:
        return [""]
    elif 1<num<=9:
        return list(get_characters(num)) # ["abc", "def"]

    last_digit = num % 10  # 3
    small_output = keypad(num // 10)  # 2 [a,b,c]
    keypad_string = get_characters(last_digit)  # def
    output = list()
    for letter in keypad_string:
        for item in small_output:  # a,b,c
            new_item = item + letter  # ad,bd,cd  ae,be,ce  af,bf,cf
            output.append(new_item)
    return output

def test_keypad(input, expected_output):
    if sorted(keypad(input)) == expected_output:
        print("Yay. We got it right.")
    else:
        print("Oops! That was incorrect.")
# Base case: list with empty string
input = 0
expected_output = [""]
test_keypad(input, expected_output)
# Example case
input = 8
expected_output = sorted(["t", "u", "v"])
test_keypad(input, expected_output)