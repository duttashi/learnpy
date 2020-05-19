### Installing XUbuntu on Virtualbox and sharing folders between host windows OS and guest xubuntu OS

Motivation: I think the cost incurred in deploying a machine learning model in AWS Sagemaker is more than that of Lambda. Thus, I have to figure out how to make lambda work with external packages

The general approach is;

  - package all dependencies
  - pack your function
  - upload as a layer to Lambda and attach the layer to the lambda function.

**Important Note**

The external packages that you want to install in AWS Lambda MUST be Linux compiled binaries, because AWS Lambda is linux based.

Being a windows user, I tried and failed in applying the following approaches

- **Approach # 1**: Tried installing pre-compiled [linux binaries](https://github.com/ryfeus/lambda-packs). The lambda function was added and zipped. It was then uploaded to the S3 bucket and linked to a lambda layer - *Failed. Error message, "errorMessage": "Unable to import module 'lambda_function': No module named 'pandas'",   "errorType": Runtime.ImportModuleError"*

- **Approach # 2**: Tried following solutions posted on SO, [1](https://stackoverflow.com/questions/43877692/pandas-in-aws-lambda-gives-numpy-error), [2](https://stackoverflow.com/questions/57534965/unable-to-import-pandas-in-aws-lambda), [3](https://stackoverflow.com/questions/57375042/aws-lambda-deployment-package-in-python-limites), [4](https://stackoverflow.com/questions/44208895/aws-lambda-python-function-with-pandas-dependency), [5](https://stackoverflow.com/questions/34749806/using-moviepy-scipy-and-numpy-in-amazon-lambda?noredirect=1&lq=1) *Failed. Error message, "errorMessage": "Unable to import module 'lambda_function': No module named 'pandas'",   "errorType": Runtime.ImportModuleError"* 
	
- **Approach # 3**: Tried solutions posted elsewhere on the internet, like, [1](https://medium.com/@manivannan_data/import-custom-python-packages-on-aws-lambda-function-5fbac36b40f8), [2](https://medium.com/i-like-big-data-and-i-cannot-lie/how-to-create-an-aws-lambda-python-3-6-deployment-package-using-docker-d0e847207dd6), [3](https://hackersandslackers.com/using-pandas-with-aws-lambda/) *Failed. Error message, "errorMessage": "Unable to import module 'lambda_function': No module named 'pandas'",   "errorType": Runtime.ImportModuleError"*

- **Approach # 4**: Tried unix-compiled `pandas` binaries on a MAC OSX and failed.

**Inference** I think, I need to install a virtual machine with a linux distro like Xubuntu. Then install python and these packages on it. Thereafter, zip them and upload to Lambda..  


### Installing Xubuntu Linux on Virtualbox

Alright, so after several trials-errors, I chose to use Xubuntu as guest OS because of the following reasons;

1. Its lightweight as compared to Ubuntu (primary reason)
2. Does not hog/eat much primary memory(RAM) as compared to Ubuntu. Works for me, as my decade old Dell box has only 4 GB primary memory!!
3. It interface is quite similar to Windows. (*I know I will soon have to forgo the habit of being a windows user but until then let the transistion to linux be smooth and not a rough one*).
 
#### Steps:

1. [Download Xubuntu ISO image](https://xubuntu.org/download#show-all) from a nearby mirror and get going. Note, be careful in downloading the type of image. My Windows 7 machine is `i386`. So, I chose the [16.04 i386 version](releases.ubuntu.com/16.04/). 

2. There are abundant resources available on the internet that discuss how to install xubuntu on virtualbox. So just follow any one of them.

### Mounting VirtualBox shared folders between the host (windows) and guest (XUbuntu) OS

This guide will walk you through steps on how to setup a VirtualBox shared folder inside your XUbuntu 16.04 guest. Tested on XUbuntu 16.04 LTS (Xenial Xerus)

#### Steps:

1. Open Virtualbox
2. Right-click your VM, then click `Settings`
3. Go to `Shared Folders` section
4. Add a new shared folder
5. On Add Share prompt, select the Folder Path in your host that you want to be accessible inside your VM.
6. In the Folder Name field, type `shared`
7. Uncheck the text box, `Read-only` 
8. Check the text box, `Auto-mount`, and check `Make Permanent`
8. Restart your VM
9. You should see the shared folder now in `File Manager`. It will be named something like `sf_yourshared_folder_name`


##### If somehow it does not work then try the following steps:

Installing Guest Additions in Xubuntu

1. In XUbuntu desktop screen, click on `File System` icon.
2. In the LHS menu, you will see the option `Devices` under which will be the `VBOXGuest Additions CD` mounted. Click on it.
3. The window will change to `/media/username/VBox_GAs_6.0.12/`. In here, right click on `Open Terminal Emulator here` to open the command prompt window.
4. In the Terminal Emulator window, type the command:

    `sudo /media/username/VBox_GAs_6.0.12/VBoxLinuxAdditions.run`

Replace `username` with your xubuntu username.

Once the installer finishes, restart by:

- Clicking the blue snail thing in the upper left corner of the Xubuntu screen
- Choosing the power button in the bottom right edge of the menu
- Clicking Restart

Reference: See this [detailed post](http://www.fixedbyvonnie.com/2015/07/how-to-setup-xubuntu-linux-in-virtualbox-step-by-step/#.XYLZay4zbIU)

**Accessing the shared folder in guest OS**

When accessing the shared folder in guest OS, if you get the following error,
**Error: /media/sf_sharedFolder/: Permission denied**

In guest OS `XUbuntu` when accessing the shared folder, If you see the above error then solve it as follows:

- Open the Terminal
- Type the command, `sudo adduser $USER vboxsf`
- Log out and relogin again for the changes to come into affect.

What this command does is to add you to the `vboxsf` group within the guest VM. See this [SO post solution by user Constantin](https://stackoverflow.com/questions/26740113/virtualbox-shared-folder-permissions) 

#### Problems installing Guest Additions

If you can’t install Guest Additions try doing this:

Revisit the **Terminal Emulator** and type in the following commands:

`sudo apt-get install build-essential module-assistant`

And then build the kernel module with:

`sudo m-a prepare`

##### If you still can’t get Guest Additions to work!

If you still can’t install Guest Additions type this in the Terminal Emulator:

`sudo apt-get install virtualbox-guest-dkms`   

That should do the trick. You should now see the shared folder in the `guest OS ie XUbuntu` that the shared folder has a prefix of `sf`. You are all set now to transfer files between host and guest and vice-versa. Hope this helps.

Reference: See this [helpful guide](http://www.fixedbyvonnie.com/2015/07/how-to-setup-xubuntu-linux-in-virtualbox-step-by-step/#.XXCfmi4zbIU) on how to install guest additions on virtualbox.