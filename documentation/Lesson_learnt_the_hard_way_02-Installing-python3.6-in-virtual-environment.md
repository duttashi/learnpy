This log is in continuation to my previous notes [1]() 

### Installing python3.6 in a virtual environment

Alright so far, I installed Xubuntu as a guest OS on a virtualbox. See this [post]() for details.

Next step, is to install a virtual environment within the Xubuntu to install python 3.6 on it. I have understood that Xubuntu 16.04 LTS is built on python2.7 and also comes with python3.5. Both these python versions are incompatible with AWS Lambda. I can't install a new version of Xubuntu because my decade old Dell machine architecture does not support it. It sucks so much. 

Note: I installed XUbuntu 16.04 on virtualbox. The 16.04, comes with Python 2.7 and Python 3.5.

In the guest OS `Xubuntu` do the following

1. Open Terminal and create a virtual-environment. Because XUbuntu is built on python2.7. For pandas package to work in Lambda requires python 3.6 or 3.7 version. We do not want to mess up with XUbuntu environment. That is why creating a virtual-environment will help. 

*Do not try to create a virtual environment in the shared folder. It will not work. I have tested it.*
3. 4. So open a terminal and type the commands


   Install pip first

    $ sudo apt-get install python3-pip

   Then install virtualenv using pip3

    $ sudo pip3 install virtualenv 

   Now create a virtual environment

    $ virtualenv myvenv

  The virtual environment will be created at location, `/home/username/myvenv/bin/python` 	

   OR use `$ python3 -m venv myvenv` to create the virtual environment
     
   You can use any name for virtual environment.

   Activate your virtual environment
	
	$ source myvenv/bin/activate

   The virtual environment prompt will look something like, `(myvenv)username@username-VirtualBox:~$`  
 
   Install python 3 in the virtual environment  	
	
	(myvenv)username@username-VirtualBox:~$ sudo apt-get update

Note: In executing the above command, if it fails with an error like, `Error in appstreamcli`, then solve it by the command, `sudo apt-get purge libappstream3`. Now try the update command again, `sudo apt-get update`. It should now work.

After this, type the following command,
	
	(myvenv) ashoo@ashoo-VirtualBox:~$ sudo add-apt-repository ppa:jonathonf/python-3.6
	(myvenv) ashoo@ashoo-VirtualBox:~$ sudo apt-get update 
	(myvenv) ashoo@ashoo-VirtualBox:~$ sudo apt-get install python3.6
	(myvenv) ashoo@ashoo-VirtualBox:~$ python3.6 -V
	Python 3.6.8

To make python3 use the new installed python 3.6 instead of the default 3.5 release, run following 2 commands

    (myvenv) ashoo@ashoo-VirtualBox:~$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1

    # if the above command succeeds then this message will be printed: update-alternatives: using /usr/bin/python3.5 to provide /usr/bin/python3 (python3) in auto mode

    (myvenv) ashoo@ashoo-VirtualBox:~$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2

    # if the above command succeeds then this message will be printed: update-alternatives: using /usr/bin/python3.6 to provide /usr/bin/python3 (python3) in auto mode

Finally switch between the two python versions for python3 via command

    (myvenv) ashoo@ashoo-VirtualBox:~$ sudo update-alternatives --config python3

    There are 2 choices for the alternative python3 (providing /usr/bin/python3).
    
      SelectionPathPriority   Status
    ------------------------------------------------------------
    * 0/usr/bin/python3.6   2 auto mode
      1/usr/bin/python3.5   1 manual mode
      2/usr/bin/python3.6   2 manual mode
    
    Press <enter> to keep the current choice[*], or type selection number: 0

After selecting version 3.6: 

    (myvenv) ashoo@ashoo-VirtualBox:~$ python3.6 -V
    Python 3.6.8

Congratulations, you have installed `python3.6.8` in a virtual environment within the virtual environment of the guest OS. Note the location of this virtual environment is at, `/home/username/myvenv/bin/python`. This path will help later to copy the linux compiled binaries of external packages to the shared folder. 

----------




 


