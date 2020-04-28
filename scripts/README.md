#### Required Software information

This project uses the following IDE and python distribution:

**Python**

- IDE is Spyder 3
	- *How to install Spyder*: See [here](https://docs.spyder-ide.org/installation.html). 
		- Open a command prompt window and browse to your local python installation directory. In my case its, `c:\users\myusername\miniconda3` and then type `pip3 install spyder`
		- To launch spyder IDE, open a command prompt window, type the command, `spyder3` and hit the enter key. Spyder IDE will launch
		
- Python 3 distribution is Miniconda 3

#### Script Naming Convention

The following are the various types of python topics that I'll be writing about.

- machine learning abbreviated as `ml_`
- pandas abbreviated as `mlpd_`
- numpy abbreviated as `mlnp_`
- scipy abbreviated as `mlsp_`
- class abbreviated as `cls_`
- dictionary abbreviated as `dict_`
- list abbreviated as `list_`
- series abbreviated as `ser_`
- method abbreviated as `func_`
- web data scrapping abbreviated as `scrp_`
- data extraction from offline content like pdf file or excel file etc will be abbreviated as `extr_`
- I/O (input/output) related topics abbreviated as `io_`
- Boto3 in AWS abbreviated as `aws_`
- loops like `for, while` abbreviated as `loop_`  

**Note:** The prefix name must not exceed more than 4 characters excluding the hyphen sign.

Therefore, as outlined above the script name will always begin with the type it represents. For example, if the script is related to pandas, then it'll be named as `mlpd_exploring_seabed_fauna.py`.

Furthermore, if the script contains code on more than 1 topic outlined above, then the topic that is central to the script will take precedence, in script naming. Example: suppose a script has an exploratory analysis of a dictionary based dataset, then the script will be named as `mlpd_*.py` *where * represents some meaningful script name*

#### General Folder & Variable naming conventions

This repository follows the [PEP 8](https://www.python.org/dev/peps/pep-0008/) standard for Python file and folder naming conventions. Also see the [Google Python Style Guide](http://google.github.io/styleguide/pyguide.html#3164-guidelines-derived-from-guidos-recommendations).

- A Python **File name** must have a `.py` extension and must not contain dashes (-). This allows them to be imported and unittested. It is also called a `module` . It is simply a Python source file, which can expose classes, functions and global variables.
	- Modules: should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Example: `my_module.py`
	- Function: Function names should be lowercase, with words separated by underscores as necessary to improve readability. Example: `my_function`
	- **Function arguments**: Always use `self` for the first argument to instance methods.
		- Always use `cls` for the first argument to class methods.
		- If a function argument's name clashes with a reserved keyword, it is generally better to append a single trailing underscore rather than use an abbreviation or spelling corruption. Thus `class_` is better than clss. (Perhaps better is to avoid such clashes by using a synonym.)
	- **Variable name**: use a lowercase single letter, word, or words. Separate words with underscores to improve readability. Example: `my_variable`
- A Python **package** is simply a directory of Python module(s).
	- Python packages should also have short, all-lowercase names, although the use of underscores is discouraged. Example: `mypackage`
	- **Constant** - Use an uppercase single letter, word, or words. Separate words with underscores to improve readability. Example: `MY_CONSTANT`
	- **Class** - start each word with a capital letter. Do not separate words with underscores. This style is called camel case. Example: `MyClass`



   

