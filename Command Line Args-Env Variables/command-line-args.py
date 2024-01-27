import sys
def addition(num1, num2):
    add = num1 + num2
    return add

def sub(num1, num2):
    s = num1 - num2
    return s

def multiplication(num1, num2):
    m = num1 * num2
    return m

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

# to run the code on the command line use this command to test the code:
#  python command-line-args.py 2 addition 3
# N.B: note that instead of float you can use int()


if operation == "addition":
    output = addition(num1, num2)
    print(output)

