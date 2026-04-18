import sys
import os
import time

def print_usage():
    print("Usage: python checker.py <option>")
    print("<option>: small, large")

def main():
    if len(sys.argv) != 2:
        print_usage()
        return

    option = sys.argv[1].lower().strip()

    if option == "small":
        in_file = "data/small_input"
        sol_file = "data/small_solution"
    elif option == "large":
        in_file = "data/large_input"
        sol_file = "data/large_solution"
    else:
        print("Error: <option> not found")
        print_usage()
        return

    out_file = "data/output"

    command = f"python rocky.py < {in_file} > {out_file}"
    os.system(command)

    with open(sol_file, "r") as f:
        exp = f.readlines()

    with open(out_file, "r") as f:
        out = f.readlines()

    correct = 0
    wrong = 0
    total = min(len(exp), len(out))

    for i, (e, o) in enumerate(zip(exp, out)):
        e = e.strip()
        o = o.strip()
        
        if (e == o):
            correct += 1
        else:
            print(f"Detected incorrect @ test case #{i+1}")
            wrong += 1

    wrong += abs(len(exp) - len(out))

    print(f"Correct: {correct} / {total}")
    print(f"Wrong: {wrong}")

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Ran for: {end-start}")