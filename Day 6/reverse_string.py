def reverseString(S: str) -> str:
    ch = list(S)
    left, right = 0, len(S)-1

    while left < right:
        ch[left], ch[right] = ch[right], ch[left]
        left += 1
        right -= 1

    return ''.join(ch)


if __name__ == "__main__":
    print(reverseString("Sai Krishna Akula"))
    print(reverseString("  "))