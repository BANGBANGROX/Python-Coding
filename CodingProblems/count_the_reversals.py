def countRev(s: str) -> int:
    # your code here
    n: int = len(s)

    if (n & 1) > 0:
        return -1

    stack: list[str] = []

    for ch in s:
        if ch == "}":
            if len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(ch)
        else:
            stack.append(ch)

    answer: int = len(stack) // 2
    open_brackets: int = 0

    while len(stack) > 0 and stack[-1] == "{":
        stack.pop()
        open_brackets += 1

    answer += open_brackets % 2

    return answer


# {
# Driver Code Starts
t: int = int(input())
for tc in range(t):
    s: str = input()
    print(countRev(s))

    print("~")
