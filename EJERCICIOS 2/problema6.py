def fibonacci():
    a, b = 0, 1
    print(a,",")
    while b <= 50:
        print(b,", "if b < 50 else "\n")
        a, b = b, a + b
fibonacci()