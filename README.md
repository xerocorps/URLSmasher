URL to Path Converter
=====================

This is a Python script that takes a list of URLs as input and breaks down the subdirectories in each URL's path into their absolute paths. It then outputs a list of all the possible absolute paths for each URL variant, with the URL prefix added to each path.

Installation
------------

To use this tool, you need to have Python 3 installed on your system. You can download the latest version of Python from the official website: <https://www.python.org/downloads/>

To download the script, you can either clone this repository or download the script file directly. To clone the repository, run the following command:

`git clone https://github.com/xerocorps/URLSmasher.git`

Usage
-----

To use the script, open a terminal or command prompt and navigate to the directory where the script file is located. Then, run the following command:

`python url_to_path.py -u URLS_FILE`

Replace `URLS_FILE` with the name of a file containing a list of URLs, one per line. If no `URLS_FILE` is specified, the script will read URLs from standard input.

The script will then process each URL in the list and output a list of all the possible absolute paths for each URL variant, with the URL prefix added to each path. The output will be displayed on the terminal or command prompt.

Examples
--------

Here are some examples of how to use the script:

### Example: Reading URLs from a file

Suppose you have a file `urls.txt` containing the following URLs:

```
https://www.example.com/path/to/page 
```

To process these URLs with the script, run the following command:

`python url_to_path.py -u urls.txt`

The script will output the following:

```
URL: https://www.example.com/path/to/page
Absolute path: https://www.example.com/
Absolute path: https://www.example.com/path/
Absolute path: https://www.example.com/path/to/
Absolute path: https://www.example.com/path/to/page/
```
