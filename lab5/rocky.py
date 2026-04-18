def count(X, Z):
    m = len(X)  # rows
    n = len(Z)  # columns
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m+1):
        dp[i][0] = 1
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Z[j-1]:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[m][n]

if __name__ == '__main__':
    num_test_cases = int(input())
    for test_case in range(num_test_cases):
        x, z = input().split()
        output = count(x, z)
        print(output)
