def collatz_conjecture(n):
    # This function calculates the number of steps it takes to reach 1 using the Collatz Conjecture
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

if __name__ == "__main__":
    n_values = [-10, -5, 0, 7, 10, 16, 27]
    for n in n_values:
        steps = collatz_conjecture(n)
        print(f"It takes {steps} steps to reach 1 using the Collatz Conjecture for n = {n}.")
