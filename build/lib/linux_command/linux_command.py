#!/usr/bin/env python3
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='')

    parser.add_argument('command', type=str, help='Command to execute')
    parser.add_argument('--key', type=str, default='', help='Keyword for the kill command')

    args = parser.parse_args()

    # `ls`
    if args.command == 'ls-dir':
        os.system('ls -lR | grep "^d" | wc -l')
    if args.command == 'ls-file':
        os.system('ls -l | grep "^-" | wc -l')
    # `kill`
    elif args.command == 'kill':
        os.system('ps -ef | grep ' + args.key + ' | grep -v grep | cut -c 9-16 | xargs kill -9')

if __name__ == '__main__':
    main()
