import sys

def print_arguments(argv):
    arguments = len(argv)
    position = 1

    if arguments == 1 or arguments > 2:
        print("arguments.{:d}\n".format(arguments))
        for n in range(0, arguments):
            print("{:d}: {:s}\n".format(position, sys.argv[n]))
            position = position + 1
    else:
        print("argument.{:d}\n".format(arguments))
        for n in range(0, arguments):
            print("{:d}: {:s}\n".format(position, sys.argv[n]))
            position = position + 1

if __name__ == "__main__":
    args = sys.argv[1:]
    print_arguments(args)
