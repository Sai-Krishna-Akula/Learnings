# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Bruteforce Approach: Straight approach is repeatedly remove these 3 braces and if no string left return True

def validParanthesis(s: str) -> bool:

    # while True:
    #     prev = s

    #     s = s.replace("[]","")
    #     s = s.replace("{}","")
    #     s = s.replace("()","")

    #     if prev == s:
    #         break
    # return len(s) == 0

    stack = []
    braces_map = {
        '}' : '{',
        ']' : '[',
        ')' : '('
    }

    for ch in s:
        # open brace then append
        if ch not in braces_map:
            stack.append(ch)
        #  close brace then try to pop
        else:
            # if no element in stack when close brace to pop
            if not stack:
                return False
            top = stack.pop()
            if top != braces_map[ch]:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    print(validParanthesis("({[]})"))
    print(validParanthesis("[{()}"))
    print(validParanthesis(""))
    print(validParanthesis("[["))
    print(validParanthesis("()]"))