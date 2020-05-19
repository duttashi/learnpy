This log is in continuation to my previous notes [1]() and [2]()

### Installing python pandas, numpy and any other external packages in AWS Lambda

It took me 45 days of constant failures to install/import pandas package in AWS lambda environment. For this too work, ensure to activate the python3.6 installed on the virtual environment. See this [post]() for details.
 
**Why it took me such a long time to understand**- Because of the following reasons;

1. AWS is built on Linux, and for pandas to work, it requires linux-compatible binaries only.
2. I have been a windows user and understanding linux command's were difficult.
3. I searched the internet, online forums and most answers suggested to use either linux-compatible binaries or suggested path issues like `python/lib/site-packages/`. But none worked. See this question that I posted on [SO](https://stackoverflow.com/questions/57688731/unable-to-import-module-lambda-function-no-module-named-pandas) as proof of my *failed efforts*. 

**How I solved the problem**

In the host OS `Windows` do the following:

1. Navigate to `https://pypi.org/project/pandas/#files` Search for and download newest `manylinux1_x86_64.whl` package. In my case for Python 3.6 is `pandas-0.24.1-cp36-cp36m-manylinux1_x86_64.whl` file.
NumPy. Do the same for NumPy. File is `numpy-1.16.1-cp36-cp36m-manylinux1_x86_64.whl`. 
2. Download `*.whl` files to the directory where you have kept the `lambda_function.py` file.
3. Now copy the directory from step 2 above into the guest OS XUbuntu.
4. It is important to note that most of the libraries depend upon other packages. To determine, the package dependency, do the following:

	    a. Suppose I want to install the matplotlib library
    	
    	b. Then in Google, type `matplotlib dependencies`
    	
    	c. Browse to the location `https://matplotlib.org/3.1.1/users/installing.html#dependencies` to find relevant dependencies.
    	
    	d. After finding out the dependencies, open Google and type `freetype linux whl download`. Select the `pypi.org` link and go to it. On its page, in LHS see `Download files`, click on it and in next page, choose the file that reads like, `filename-manylinux1_i686.whl`. The idea is to choose wheel file for python3. 
    
    	e. Download the `*.whl` file and copy it to Xubuntu shared folder.
    
    	f. In Xubuntu, open terminal in shared folder and type, `unzip` followed by the *.whl` filename, And press enter key to unzip the file.

**Installing the pandas package in myvenv**

Activate your virtual environment
	
	$ source myvenv/bin/activate

1. Unzip the `*.whl` file. Now this is tricky. A `*.whl` file is a linux-file. And no software on windows OS will be able to unzip it. So, I copied these `*.whl` files to the `XUbuntu guest OS on virtual box` and unzipped them.
2. Create a directory and give it any name. I named it `packs`.
2. Open Terminal with `ctrl+alt+T` in the `packs` directory where the `*.whl` files are kept. 
3. Type the following commands to unzip the files:

    `$ unzip numpy-1.16.1-cp36-cp36m-manylinux1_x86_64.whl`

    `$ unzip pandas-0.24.1-cp36-cp36m-manylinux1_x86_64.whl` 

3.1. Install the `pytz` library

    $ pip install -t . pytz

3.2. Remove the following files to decrease folder space

	$ rm -r *.whl *.dist-info __pycache__

3.3. At this stage the packs directory will contain two sub-directories namely `pandas` and `numpy`. It will also contain the `lambda-function.py` file. Copy the `packs` directory from the guest OS to host (windows) OS.

4. In the host OS, enter the packs directory. It  will contain two sub-directories namely `pandas` and `numpy`. It will also contain the `lambda-function.py` file. Select them all and right-click. Select the 7zip software and create a `packs.zip` directory.
5. Open the browser and login to your AWS Lambda. Click on `Function` on RHS to create the function. 
	1. Name it as `lambda-function.py`
	2. Environment is python3.6
	3. Click upload zip file and attach the `packs.zip` file
	4. Test the code. It should now work

----------