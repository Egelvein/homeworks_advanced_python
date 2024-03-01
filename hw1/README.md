# Linux utils

Here is the implementation of 3 linux command line utilities: nl, tail, wc

## Contents
- [nl](#nl)
- [tail](#tail)
- [wc](#wc)

### nl
**Task:** You need to implement a CLI application, apart from the code, you need to attach as artefacts a text file of how you tested the operability of your code (just a copy of the commands and outputs from the terminal)

- Write a simplified version of the `nl` utility -- a script that outputs numbered lines from a file to `stdout`.
- If no file is passed, the script reads the lines from `stdin`.
- It should work in the same way as `nl -b a`.

**Usage:** `python3 nl_util.py --textfile example.txt`. You can also use it with .py files in this folder or with your file.

**Example of working:**
![nl.png](images/nl.png)



### tail
**Task:** Write a simplified version of the `tail` utility -- a script that outputs the last 10 lines of each transferred file to `stdout`.

- If more than one file is transferred, output its name before processing the next file. See the original `tail` utility for details, your script should repeat the formatting.
- if no file is passed, you must output the last 17 lines of `stdin`.

**Usage:** `python3 tail_util.py example.txt`. You can also use it with .py files in this folder or with your file.

**Example of working:**
![nl.png](images/tail.png)


### wc
**Task:** Write a script that works the same way as the `wc` utility called without additional options.
That is, for each file transferred, the utility outputs statistics (3 numbers) and the file name.

In this case:
- if more than one file is transferred, the utility displays total statistics at the very end,
- if no file is transferred, the utility reads the whole input and prints statistics for it without a name.

**Usage:** `python3 wc_util.py example.txt`. You can also use it with .py files in this folder or with your file.

**Example of working:**
![nl.png](images/wc.png)
