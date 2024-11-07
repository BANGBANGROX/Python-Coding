def countRev(s):
    # your code here
    n = len(s)

    if (n & 1) > 0:
        return -1

    stack = []

    for ch in s:
        if ch == "}":
            if len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(ch)
        else:
            stack.append(ch)

    answer = len(stack) // 2
    open_brackets = 0

    while len(stack) > 0 and stack[-1] == "{":
        stack.pop()
        open_brackets += 1

    answer += open_brackets % 2

    return answer


# {
# Driver Code Starts
t = int(input())
for tc in range(t):
    s = input()
    print(countRev(s))

    print("~")
