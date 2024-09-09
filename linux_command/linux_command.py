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
VERSION = "0.2.3"
PROJECT_URL = "https://github.com/MouxiaoHuang/linux-command" 


# Command descriptions
commands = {
    'ls': 'List contents.',
    'lsf': 'Count all files or filter by a specified pattern, extension or keyword. Same as `ls-file`.',
    'ls-file': 'Count all files or filter by a specified pattern, extension or keyword. Same as `lsf`.',
    'lsd': 'Count all directories. Same as `ls-dir`.',
    'ls-dir': 'Count all directories. Same as `lsd`.',
    'ls-reverse': 'List files and directories in reverse order.',
    'ls-time': 'List sorted by modification time, newest first.',
    'ls-human': 'List in human-readable format (for file sizes)',
    'ls-long': 'Long format listing',
    'ls-size': 'Sort files by size',
    'ls-recursive-size': 'List all files and directories recursively, with sizes in human-readable format',
    'ls-bs': 'Display the size of each file in specified block size (e.g., K, M, G).',
    'ls-block-size': 'Display the size of each file in specified block size (e.g., K, M, G).',
    'ps': 'Basic process list.',
    'ps-all': 'Show all processes.',
    'ps-user': 'Show processes for a specific user',
    'ps-aux': 'Show detailed information about all processes.',
    'ps-sort-memory': 'Sort processes by memory usage.',
    'ps-sort-cpu': 'Sort processes by CPU usage.',
    'ps-grep': 'Search for a specific process by name or keyword.',
    'kill': 'Kill a process with PID or keyword in its name.',
    'df': 'Show disk usage.',
    'du': 'Show disk usage of a directory. Default: current directory.',
    'disk': 'Show disk usage of a directory. Default: current directory.',
    'rm': 'Remove file, directory, or multiple files by patterns (e.g., *.txt)',
    'grep': 'Search for a pattern in files or output.',
    'tar': 'Pack into .tar or .tar.gz file.',
    'tar-comress': 'Pack into .tar or .tar.gz file.',
    'untar': 'Unpack .tar or .tar.gz file, or batch process in a directory.',
    'tar-extract': 'Unpack .tar or .tar.gz file, or batch process in a directory.',
    'tar-list': 'List all contents in a tar file.',
    'tar-add': 'Add a file to a tar file.',
    'zip': 'Pack a folder to a .zip file.',
    'zip-all': 'Pack a folder to a .zip file.',
    'unzip': 'Unpack all .zip files in a directory to another.',
    'unzip-all': 'Unpack all .zip files in a directory to another.',
    'convert-vid': 'Video pattern trans. Usage: convert-video [source file or pattern] [destination file or pattern]',
    'convert-video': 'Video pattern trans. Usage: convert-video [source file or pattern] [destination file or pattern]',
}


def custom_help():
    print("Available commands:")
    for command, description in commands.items():
        print(f'[{command}]: {description}')
    print(f"For more information, visit: {PROJECT_URL}")



def confirm_action(message):
    """Ask the user to confirm an action, accepting y/n or yes/no"""
    confirmation = input(f"{message} (yes/no or y/n): ").strip().lower()
    return confirmation in ['yes', 'y']


def main():
    # Set up argparse
    parser = argparse.ArgumentParser(
        description="Linux Command Wrapper - Execute common Linux commands easily",
        epilog=f"Project page: {PROJECT_URL}",
        add_help=False
    )

    parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')
    parser.add_argument('-V', '--version', action='store_true', help='Show program\'s version number and exit')
    
    # Main command and subcommands
    parser.add_argument('command', nargs='?', help='Command to execute')
    parser.add_argument('extra', nargs='*', help='Additional arguments for the command')

    # Parse the arguments
    args = parser.parse_args()

    if args.help:
        custom_help()
        return

    if args.version:
        print(f'linux-command {VERSION}')
        return

    # `ls` commands
    if args.command == 'ls':
        if len(args.extra) == 0:
            # List current directory
            os.system('ls')
        else:
            options = ' '.join(args.extra)
            os.system(f'ls {options}')
    
    # Advanced `ls` commands

    elif args.command == 'ls-dir' or args.command == 'lsd':
        # Count the number of directories
        os.system('ls -lR | grep "^d" | wc -l')
    
    elif args.command == 'ls-file' or args.command == 'lsf':
        if len(args.extra) == 0:
            # Count the number of all files
            os.system('ls -l | grep "^-" | wc -l')
        else:
            # Count files of a specific type based on provided extension or pattern
            pattern = args.extra[0]  # First extra argument as file pattern
            os.system(f'ls -l | grep "^-" | grep "{pattern}" | wc -l')
    
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
    
    elif args.command == 'ls-long':
        # Long format listing
        if len(args.extra) == 0:
            os.system('ls -l')
        else:
            options = ' '.join(args.extra)
            os.system(f'ls -l {options}')

    elif args.command == 'ls-human':
        # List in human-readable format (for file sizes)
        if len(args.extra) == 0:
            os.system('ls -lh')
        else:
            options = ' '.join(args.extra)
            os.system(f'ls -lh {options}')
    
    elif args.command == 'ls-recursive-size':
        # List all files and directories recursively, with sizes in human-readable format
        if len(args.extra) == 0:
            os.system('ls -lRh')
        else:
            options = ' '.join(args.extra)
            os.system(f'ls -lRh {options}')
    
    elif args.command == 'ls-size':
        # Sort files by size
        if len(args.extra) == 0:
            os.system('ls -lS')
        else:
            options = ' '.join(args.extra)
            os.system(f'ls -lS {options}')
    
    elif args.command == 'ls-block-size' or args.command == 'ls-bs':
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

    elif args.command == 'du' or args.command == 'disk':
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
    elif args.command == 'tar-compress' or args.command == 'tar':
        if len(args.extra) >= 2:
            source = args.extra[0]
            output = args.extra[1]
            exclude = args.extra[2:]  # Additional arguments as exclude patterns
            exclude_params = ' '.join(f'--exclude={x}' for x in exclude)
            if output.endswith('.tar.gz'):
                os.system(f'tar -czvf {output} {exclude_params} {source}')
            elif output.endswith('.tar'):
                os.system(f'tar -cvf {output} {exclude_params} {source}')
            else:
                print('Unsupported output format. Please provide .tar or .tar.gz as the output file extension.')
        else:
            print('Please provide a source and output file for tar compression')

    elif args.command == 'tar-extract' or args.command == 'untar':
        if len(args.extra) >= 2:
            source = args.extra[0]
            destination = args.extra[1]
            file_type = args.extra[2] if len(args.extra) > 2 else "all"  # Optional file type filter

            if os.path.isdir(source):  # Check if source is a directory
                if file_type[-3:] == "tar":
                    tar_files = glob.glob(os.path.join(source, '*.tar'))
                elif file_type[-2:] == "gz":
                    tar_files = glob.glob(os.path.join(source, '*.tar.gz'))
                else:  # Extract all tar and tar.gz files
                    tar_files = glob.glob(os.path.join(source, '*.tar')) + glob.glob(os.path.join(source, '*.tar.gz'))

                for tar_file in tar_files:
                    if tar_file.endswith('.tar'):
                        os.system(f'tar -xvf {tar_file} -C {destination}')
                    elif tar_file.endswith('.tar.gz'):
                        os.system(f'tar -xzvf {tar_file} -C {destination}')
            # Extract a single tar file
            elif source.endswith('.tar.gz'):
                os.system(f'tar -xzvf {source} -C {destination}')
            elif source.endswith('.tar'):
                os.system(f'tar -xvf {source} -C {destination}')
            else:
                print('Please provide a valid .tar or .tar.gz file, or a directory containing such files.')



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
    
    # Unzip
    elif args.command == 'unzip-all' or args.command == 'unzip':
        if len(args.extra) == 2:
            source_dir = args.extra[0]
            target_dir = args.extra[1]
            os.system(f'find {source_dir} -name "*.zip" -exec unzip {{}} -d {target_dir} \;')
        else:
            print('Please provide both a source and a target directory.')
    
    # Zip compress
    elif args.command == 'zip-all' or args.command == 'zip':
        if len(args.extra) >= 2:
            output = args.extra[0]
            sources = args.extra[1:]  # All other arguments as sources to be zipped
            source_params = ' '.join(sources)
            os.system(f'zip -r {output} {source_params}')
        else:
            print('Please provide an output file name and at least one source to compress.')

    # ffmpeg
    elif args.command == 'convert-video' or args.command == 'convert-vid':
        if len(args.extra) == 2:
            source = args.extra[0]
            destination = args.extra[1]

            if '*' in source:
                # Handle wildcard batch conversion
                source_files = glob.glob(source)
                destination_dir = os.path.dirname(destination)
                file_extension = destination.split('.')[-1]

                for src_file in source_files:
                    basename = os.path.splitext(os.path.basename(src_file))[0]
                    dest_file = os.path.join(destination_dir, f'{basename}.{file_extension}')
                    os.system(f'ffmpeg -i "{src_file}" -c copy "{dest_file}" -y')
            else:
                # Handle single file conversion
                os.system(f'ffmpeg -i "{source}" -c copy "{destination}" -y')
        else:
            print('Usage: convert-video [source file or pattern] [destination file or pattern]')



if __name__ == '__main__':
    main()
