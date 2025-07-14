#!/usr/bin/env python3

from gendiff import cli, generate_diff


def main():
    '''
    This function is the entry point of the program.
    It retrieves file paths and format name
    from the command line interface, generates the difference
    between the files, and prints the difference.
    '''
    diff = generate_diff(cli())
    print(diff)


if __name__ == "__main__":
    main()
