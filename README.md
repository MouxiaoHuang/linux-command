
# linux-command

`linux-command` is a versatile package that provides a collection of frequently used Linux commands in a convenient wrapper. It can be installed via pip and accessed using the `cmd` command in the terminal.

## Installation

To install the package, run the following command:

```bash
pip install linux-command
```

## Usage

Once installed, you can access all commands using `cmd` followed by the specific command name. Below is a list of supported commands along with examples for each.

---

### 1. `ls` - List files in the current directory

```bash
cmd ls
```

### 2. `ls-all` - List all files, including hidden ones

```bash
cmd ls-all
```

### 3. `ls-long` - Long format listing

```bash
cmd ls-long
```

### 4. `ls-human` - List in human-readable format (file sizes)

```bash
cmd ls-human
```

### 5. `ls-size` - Sort files by size

```bash
cmd ls-size
```

### 6. `ls-recursive` - Recursively list files in directories and subdirectories

```bash
cmd ls-recursive
```

### 7. `ls-dir` - Count the number of directories

```bash
cmd ls-dir
```

### 8. `ls-file` - Count the number of files

```bash
cmd ls-file
```

### 9. `ls-reverse` - List files and directories in reverse order

```bash
cmd ls-reverse
```

### 10. `ls-time` - Sort by modification time (newest first)

```bash
cmd ls-time
```

### 11. `ls-recursive-size` - List files and directories recursively with human-readable sizes

```bash
cmd ls-recursive-size
```

### 12. `ls-block-size` - Display the size of each file in a specified block size (e.g., K, M, G)

```bash
cmd ls-block-size M
```

---

### 13. `ps` - Show running processes

```bash
cmd ps
```

### 14. `ps-all` - Show all processes

```bash
cmd ps-all
```

### 15. `ps-user [username]` - Show processes for a specific user

```bash
cmd ps-user username
```

### 16. `ps-aux` - Show detailed information about all processes

```bash
cmd ps-aux
```

### 17. `ps-sort-memory` - Sort processes by memory usage

```bash
cmd ps-sort-memory
```

### 18. `ps-sort-cpu` - Sort processes by CPU usage

```bash
cmd ps-sort-cpu
```

### 19. `ps-grep [keyword]` - Search for a specific process by name or keyword

```bash
cmd ps-grep python
```

---

### 20. `kill [process_name_or_PID]` - Kill a process by name or PID

```bash
cmd kill process_name
```

---

### 21. `df` - Show disk usage in human-readable format

```bash
cmd df
```

### 22. `du [path]` - Show disk usage for a specific file or directory

```bash
cmd du /path/to/directory
```

---

### 23. `rm [file_or_directory]` - Remove a file or directory with confirmation

```bash
cmd rm /path/to/file_or_directory
```

### 24. `rm [directory] [file_patterns...]` - Remove multiple files by pattern (e.g., *.txt)

```bash
cmd rm /path/to/directory *.txt *.log
```

---

### 25. `grep [pattern] [file]` - Search for a pattern in a file

```bash
cmd grep "search_term" /path/to/file
```

---

### 26. `tar-compress [source] [output]` - Compress files into a `.tar` or `.tar.gz` archive

- For `.tar.gz`:

```bash
cmd tar-compress /path/to/source archive.tar.gz
```

- For `.tar`:

```bash
cmd tar-compress /path/to/source archive.tar
```

### 27. `tar-extract [archive] [destination]` - Extract a `.tar` or `.tar.gz` archive

- For `.tar.gz`:

```bash
cmd tar-extract archive.tar.gz /path/to/destination
```

- For `.tar`:

```bash
cmd tar-extract archive.tar /path/to/destination
```

### 28. `tar-list [archive]` - List contents of a `.tar` or `.tar.gz` archive

```bash
cmd tar-list archive.tar.gz
```

### 29. `tar-add [file] [archive]` - Add a file to an existing `.tar` archive

```bash
cmd tar-add newfile.txt archive.tar
```

---

## Contributing

We welcome contributions from the community! If you'd like to help improve `linux-command`, including reporting issues and submitting pull requests.

### Guidelines for Contributors

- Follow the existing coding style where possible.
- Make sure your changes do not break existing functionality.
- Before submitting a major feature, it’s often a good idea to first discuss it by opening an issue.

### Thank you!

Thank you for your interest in contributing to `linux-command`! Your contributions are greatly appreciated and help make this tool better for everyone. For any questions or to get started, feel free to reach out or open an issue.

---

## License

This project is licensed under the MIT License.
