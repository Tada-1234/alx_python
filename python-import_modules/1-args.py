import sys

def print_arguments(argv):
    num_arguments = len(argv)

    if num_arguments == 0:
        print("0 argument.")
        return

    print(f"{num_arguments} argument{'s' if num_arguments > 1 else ''}:")
    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    args = sys.argv[1:]
    print_arguments(args)
