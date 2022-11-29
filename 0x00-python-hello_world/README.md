# 0x00. Python - Hello, World!.

![Python](https://img.shields.io/badge/python-v3.4-blue.svg)

# 0x00. Python - Hello, World #

* [Table of Contents](#table-of-contents) 
	* [Author](#Author)	
	* [Description](#description)
	* [Objectives](#objectives)
	* [Compilation](#compilation)
	* [Requirements](#requirements)
	* [Zen](#zen)
	* [Tasks](#tasks)
	  * [Mandatory 0](#mandatory-0)
	  * [Mandatory 1](#mandatory-1)
	  * [Mandatory 2](#mandatory-2)
	  * [Mandatory 3](#mandatory-3)
	  * [Mandatory 4](#mandatory-4)
	  * [Mandatory 5](#mandatory-5)
	  * [Mandatory 6](#mandatory-6)
	  * [Mandatory 7](#mandatory-7)
	  * [Mandatory 8](#mandatory-8)
	  * [Mandatory 9](#mandatory-8)

### Author ###
* Jeffrey Kanemitsu
	* [Github](https://github.com/jeffreykanemitsu)	
	* [Twitter](https://twitter.com/canofmisosoup)

### Description ###
First project to introduce the high-level programming language:
<p align="center">
<a href="https://www.python.org/"><img src="http://www.bebetterdeveloper.com/img/post_img/python-logo.png"/>
</a>
</p>


### Objectives ###
* At the end of the project, you are expected to explain to anyone, without the help of Google:
 * Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
 * Who created Python
 * Who is Guido van Rossum
 * Where does the name 'Python' come from
 * What is the Zen of Python
 * How to use the Python interpreter
 * How to print text and variables using print
 * How to use strings
 * What are indexing and slicing in Python
 * What is the official Holberton Python coding style and how to check your code with PEP 8

### Compilation ###
All your files will be interpreted/compiled on Ubuntu 14.04 LTS using 'python3' (version 3.4.3)
### Requirements ###
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style
* All your files must be executable
* The length of your files will be tested using wc
### Zen ###
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
### Tasks ###
#### Mandatory 0 ####
0. **Run Python file**
	* [ ] Write a Shell script that runs a Python script.
	* [ ] The Python file name will be saved in the environment variable $PYFILE
#### Mandatory 1 ####
1. **Run inline**
	* [ ] Write a Shell script that runs Python code.
	* [ ] The Python code will be saved in the environment variable $PYCODE
#### Mandatory 2 ####
2. **Hello, print**
	* [ ] Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
	* [ ] Use the function `print`
#### Mandatory 3 ####
3. **Print integer**
	* [ ] Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.
	* The output of the script should be:
		* the number, followed by Battery street,
		* followed by a new line
	* [ ]You are not allowed to cast the variable number into a string
	* [ ] Your code must be 3 lines long
#### Mandatory 4 ####
4. **Print float** 
	* [ ]Complete the [source code](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable number with a precision of 2 digits.
	* The output of the program should be:
		* `Float`:, followed by the float with only 2 digits
		* followed by a new line
	* You are not allowed to cast number to string
	* You have to use the new print formatting [tips](https://pyformat.info/#number_padding)
#### Mandatory 5 ####
5. **Print string**
	* [ ] Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
	* The output of the program should be:
		* 3 times the value of str
		* followed by a new line
		* followed by the 9 first characters of str
		* followed by a new line
	* You are not allowed to use any loops or conditional statement
	* Your program should be maximum 5 lines long
#### Mandatory 6 ####
6. **Play with strings**
	* [ ] Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py) to print `Welcome to Holberton School!`
	* You are not allowed to use any loops or conditional statements.
	* You have to use the variables `str1` and `str2` in your new line of code
	* Your program should be exactly 5 lines long
#### Mandatory 7 ####
7. **Copy - Cut - Paste**
	* [ ] Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py)
	* You are not allowed to use any loops or conditional statements
	* Your program should be exactly 8 lines long
	* [ ] `word_first_3` should contain the first 3 letters of the variable `word`
	* [ ] `word_last_2` should contain the last 2 letters of the variable `word`
	* [ ] `middle_word` should contain the value of the variable `word` without the first and last letters
#### Mandatory 8 ####
8. **Create a new sentence**
	* Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py) to print object-oriented programming with Python, followed by a new line.
	* You are not allowed to use any loops or conditional statements
	* Your program should be exactly 5 lines long
	* You are not allowed to create new variables
	* You are not allowed to use string literals
#### Mandatory 9 ####
9. **Easter Egg**
	* [ ] Write a Python script that prints "The Zen of Python", by TimPeters, followed by a new line.
	* [ ] Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)
