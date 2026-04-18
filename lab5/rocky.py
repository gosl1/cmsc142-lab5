def count(X, Z):
    #Make changes here, remove pass
    pass


if __name__ == '__main__':
    num_test_cases = int(input())
    for test_case in range(num_test_cases):
        x, z = input().split()
        output = count(x, z)
        print(output)

        test