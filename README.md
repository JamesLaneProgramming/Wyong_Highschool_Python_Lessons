A collection of python graphing scripts to be run on Raspberry PI which utilises the Matplotlib library.

NB* For all commands that use 'sudo' in this installation you may also be required to enter your password for the root user after running the specified command.

NB* For commands that install packages or libraries onto your machine, you may be prompted to confirm the installation. These prompts will usually look something like this <Enter image of package confirmation here>. Just confirm by typing 'y' meaning yes and hitting the 'Enter' key.

Installation
------------

Unix/Linux:
1) To begin, clone the repository into a chosen directory by running 'sudo git clone https://github.com/JamesLaneProgramming/Wyong_Highschool_Python_Lessons.git'. Now that we have all of the source code we can install the required packages and libraries.

2) Check that you have Python3 installed by entering 'python3 --version' into the terminal. If there is a version number returned, we can skip to step X. If the command line did not return a version number, enter 'sudo apt-get install python3' and refer back to the NB* section above if additional steps are required.

3) For the purposes of this tutorial we are also going to install the 'python3-dev' package onto our machines which has a lot of useful libraries built in. This will skip a few steps that would otherwise be time consuming. Follow the instructions found in step 2 replacing 'python3' with 'python3-dev'. For a step by step guild to installing the barebones packages and libraries, follow this tutorial here <Enter link to barebones installation>

4) Check that 'pip3' which is a python library manager is installed. As we did in step 2 and 3, check for a version and install if neccesary.

5) Using 'pip3' we are now going to install all the required libraries for these scripts. The libraries that we need to install will be:
	- matplotlib
Enter 'sudo pip3 install matplotlib' into the terminal and wait. 'matplotlib' is a big library and depending on your internet connection and processing power, may take a while to download and install.

6) For us to view the graphs that are being generated by our python scripts we need to install a GUI. In older versions of python there was not a de facto(default) GUI installed automatically. Tkinter is the GUI that we are going to be installing, the package name is 'python3-tk' and can be installed using the methods using step 2.