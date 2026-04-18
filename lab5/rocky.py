def count(X, Z):
    m = len(X)  # rows
    n = len(Z)  # columns
    dp = [[0] * (n + 1) for _ in range(m + 1)]



if __name__ == '__main__':
    num_test_cases = int(input())
    for test_case in range(num_test_cases):
        x, z = input().split()
        output = count(x, z)
        print(output)
