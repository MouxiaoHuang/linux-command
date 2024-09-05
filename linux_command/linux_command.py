#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Linux Command Wrapper

Copyright (c) 2024 Mouxiao Huang (huangmouxiao@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

For more information, visit the project page: https://github.com/MouxiaoHuang/linux-command
"""
import argparse
import os
import glob


# Define the version 
VERSION = "0.1.0"
PROJECT_URL = "https://github.com/MouxiaoHuang/linux-command" 


def confirm_action(message):
    """Ask the user to confirm an action, accepting y/n or yes/no"""
    confirmation = input(f"{message} (yes/no or y/n): ").strip().lower()
    return confirmation in ['yes', 'y']


def main():
    # Set up argparse
    parser = argparse.ArgumentParser(
        description="Linux Command Wrapper - Execute common Linux commands easily",
        epilog=f"Project page: {PROJECT_URL}",
        add_help=True
    )

    # Add version option
    parser.add_argument('-V', '--version', action='version', version=f'linux-command {VERSION}')
    
    # Main command and subcommands
    parser.add_argument('command', type=str, help='Command to execute')
    parser.add_argument('extra', nargs='*', help='Additional arguments for the command')

    # Parse the arguments
    args = parser.parse_args()

    # `ls` commands
    if args.command == 'ls':
        if len(args.extra) == 0:
            # List current directory
            os.system('ls')
        else:
            options = ' '.join(args.extra)
            os.system(f'ls {options}')
    
    # Advanced `ls` commands

    elif args.command == 'ls-dir':
        # Count the number of directories
        os.system('ls -lR | grep "^d" | wc -l')
    
    elif args.command == 'ls-file':
        # Count the number of files
        os.system('ls -l | grep "^-" | wc -l')
    
    elif args.command == 'ls-reverse':
        # List files and directories in reverse order
        if len(args.extra) == 0:
            os.system('ls -r')
        else:
            options = ' '.join(args.extra)
            os.system(f'ls -r {options}')
    
    elif args.command == 'ls-time':
        # Sort by modification time, newest first
        if len(args.extra) == 0:
            os.system('ls -lt')
        else:
            options = ' '.join(args.extra)
            os.system(f'ls -lt {options}')
    
    elif args.command == 'ls-recursive-size':
        # List all files and directories recursively, with sizes in human-readable format
        if len(args.extra) == 0:
            os.system('ls -lRh')
        else:
            options = ' '.join(args.extra)
            os.system(f'ls -lRh {options}')
    
    elif args.command == 'ls-block-size':
        # Display the size of each file in specified block size
        if len(args.extra) == 1:
            block_size = args.extra[0]
            os.system(f'ls --block-size={block_size}')
        else:
            print('Please provide a valid block size (e.g., K, M, G).')
    
    # `ps` commands
    elif args.command == 'ps':
        # Basic process list
        os.system('ps')

    elif args.command == 'ps-all':
        # Show all processes
        os.system('ps -A')
    
    elif args.command == 'ps-user':
        # Show processes for a specific user
        if len(args.extra) > 0:
            user = args.extra[0]
            os.system(f'ps -u {user}')
        else:
            print('Please provide a username to show processes for that user')

    elif args.command == 'ps-aux':
        # Show detailed information about all processes
        os.system('ps aux')

    elif args.command == 'ps-sort-memory':
        # Sort processes by memory usage
        os.system('ps aux --sort=-%mem')

    elif args.command == 'ps-sort-cpu':
        # Sort processes by CPU usage
        os.system('ps aux --sort=-%cpu')

    elif args.command == 'ps-grep':
        # Search for a specific process by name or keyword
        if len(args.extra) > 0:
            keyword = args.extra[0]
            os.system(f'ps aux | grep {keyword}')
        else:
            print('Please provide a keyword to search for in process list')

    # `kill` command
    elif args.command == 'kill':
        if len(args.extra) > 0:
            os.system(f'ps -ef | grep {args.extra[0]} | grep -v grep | cut -c 9-16 | xargs kill -9')
        else:
            print('Please provide a process name or PID for kill command')

    # Disk usage and free space commands
    elif args.command == 'df':
        os.system('df -h')

    elif args.command == 'du':
        if len(args.extra) > 0:
            os.system(f'du -sh {args.extra[0]}')
        else:
            print('Please provide a valid path for du command')

    # Remove files or directories with confirmation and support for bulk removal
    elif args.command == 'rm':
        if len(args.extra) == 1:
            target = args.extra[0]
            if confirm_action(f"Are you sure you want to remove '{target}'?"):
                if os.path.isdir(target):
                    os.system(f'rm -rf {target}')
                else:
                    os.system(f'rm {target}')
                print(f"'{target}' has been removed.")
            else:
                print(f"Operation canceled. '{target}' was not removed.")
        elif len(args.extra) > 1:
            path = args.extra[0]
            patterns = args.extra[1:]
            for pattern in patterns:
                files_to_remove = glob.glob(os.path.join(path, pattern))
                if files_to_remove:
                    print(f"Found {len(files_to_remove)} files to remove: {files_to_remove}")
                    if confirm_action(f"Are you sure you want to remove these files?"):
                        for file in files_to_remove:
                            os.system(f'rm {file}')
                        print(f"Removed files matching {pattern}.")
                    else:
                        print(f"Operation canceled for files matching {pattern}.")
                else:
                    print(f"No files found for pattern '{pattern}' in '{path}'.")

    # Search for a pattern in files or output
    elif args.command == 'grep':
        if len(args.extra) == 2:
            os.system(f'grep "{args.extra[0]}" {args.extra[1]}')
        else:
            print('Please provide a keyword and file path for grep command')

    # Tar compression and decompression
    elif args.command == 'tar-compress':
        if len(args.extra) == 2:
            source = args.extra[0]
            output = args.extra[1]
            if output.endswith('.tar.gz'):
                os.system(f'tar -czvf {output} {source}')
            elif output.endswith('.tar'):
                os.system(f'tar -cvf {output} {source}')
            else:
                print('Unsupported output format. Please provide .tar or .tar.gz as the output file extension.')
        else:
            print('Please provide a source and output file for tar compression')

    elif args.command == 'tar-extract':
        if len(args.extra) == 2:
            archive = args.extra[0]
            destination = args.extra[1]
            if archive.endswith('.tar.gz'):
                os.system(f'tar -xzvf {archive} -C {destination}')
            elif archive.endswith('.tar'):
                os.system(f'tar -xvf {archive} -C {destination}')
            else:
                print('Unsupported file format. Please provide a .tar or .tar.gz file for extraction.')
        else:
            print('Please provide a tar file and destination for extraction')

    elif args.command == 'tar-list':
        if len(args.extra) > 0:
            os.system(f'tar -tvf {args.extra[0]}')
        else:
            print('Please provide a tar file to list contents')

    elif args.command == 'tar-add':
        if len(args.extra) == 2:
            os.system(f'tar -rvf {args.extra[1]} {args.extra[0]}')
        else:
            print('Please provide a file to add and the target tar file')

if __name__ == '__main__':
    main()
