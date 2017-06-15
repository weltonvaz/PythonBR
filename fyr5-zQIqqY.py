def expecto_palindronum():
    s = list(input())
    c = []

    while s != s[::-1]:
        c.append(s.pop())

    return (len(s) + len(c) * 2)

print(expecto_palindronum())