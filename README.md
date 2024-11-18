# Libby Fetch

Libby Fetch is a program for downloading MP3 audiobooks from libbyapp.com website

## Features
1. The program will signin to the LibbyApp.com website using the user's library card.
2. The program will display a list of current audiobooks on loan
3. The user enters a book title from the list
4. The program downloads one or more MP3 files that comprise the audiobook.

## Background

When backpacking I sometimes enjoy listening to audiobooks. My preferred device for listening is a portable MP3 player (specifically, SanDisk Sport Clip Go). It's small, lightweight, easy to operate, with long battery life and doesn't require an internet connection. In the past I have been able to check out books from the library and download them as MP3 files using OverDrive Media Console. This year Overdrive stopped supporting the media console and transitioned to a new application called Libby. In November of 2024 they are going to discontinue MP3 downloads entirely.  "_There are no plans for Libby to support downloading audiobooks to a desktop computer and transferring them to an MP3 player."_
([Source](https://resources.overdrive.com/libby-faqs/)) ([Read more](https://kcls.org/news/overdrive-desktop-app-and-mp3-support-ends-on-november-13/)). 

The purpose of this program is not to circumvent library policies or DRM constraints. It's definitely for personal use only and not to distribute the audiobooks in any form. I simply want to listen to the audiobook that I have legitimately obtained from the library on a device of my choosing that better meets my needs than a smartphone.

## Prerequisites:
* Python 3.7 or higher. Check your Python version:
     `python3 --version`
* Chrome (or Chromium) web browser.
* An Overdrive account at a participating library.
* An audiobook that has been checked out from your library and appears in your Overdrive account on the Loans page.
* Your library card number (and if required, your PIN) that allows you to sign in to Overdrive.
* The library abbreviation used by Overdrive.  This is the string that precedes "overdrive.com" in the URL for your library's Overdrive page.

   Find your library abbreviation:

1. Browse `https://www.overdrive.com/libraries` and use the search field to find your library.
2. Locate your library in the search results list and click "See Digital Collection"
3. Find the URL in the browser address bar.  The desired abbreviation appears after "`https://`" and before "`.overdrive.com`"
4. For example, the URL for the San Francisco Public Library is https://sfpl.overdrive.com so the abbreviation is "`sfpl`".

### Configuration File
You must edit the configuration file named "`library_card_config.txt`" to provide your own library card information.
The file is plain text and should contain two or three values separated by commas with no spaces.
Example:   `sfpl,12341234123412,4321`  
The first field is the library abbreviation (see above).  
The second field is your library card number.  
The third field is your PIN (or password). If your library doesn't require a PIN omit this field.
Multiple libraries are supported by adding additional lines to the configuration file.

## Installation (Linux)

Step 1: Install Python (if necessary)

Python 3.7 or higher must be installed. To verify:
    `python3 --version`
 
Step 2: Download the Latest Release

  * Visit the [Releases](https://github.com/jdalbey/libbyfetch/releases) page.
  * Download the zip file for the latest release.

Step 3: Unzip the file:

    unzip libbyfetch-1.0.2.zip
    cd libbyfetch-1.0.2

Step 4: Install Dependencies

Install the required Python modules:

    python3 -m pip install selenium selenium-wire pycurl


## Installation (Windows)

Step 1: Install Python (if necessary)

Python 3.7 or higher must be installed:
    Download Python from python.org.
    During installation, ensure you check the box "Add Python to PATH".
    Verify the installation:

    `python3 --version`

pip (Python's package manager) should be included with Python. Verify it by running:

    `python3 -m pip --version`

If it's missing, reinstall Python and ensure "pip" is selected during the installation.


Step 2: Download the Latest Release

  * Visit the [Releases](https://github.com/jdalbey/libbyfetch/releases) page. 
  * Download the zip file for the latest release.

Step 3: Unzip the file:

Right-click the downloaded zip file.
Select `Extract All...` and choose a destination folder.
Open the extracted folder.

Step 4: Install Dependencies

Open a Command Prompt in the extracted folder by right-clicking inside the folder while holding Shift and select "Open PowerShell window here" or "Open Command Prompt window here".
Run the following command to install dependencies:

    `python3 -m pip install selenium selenium-wire pycurl`

## Installation (MacOS)

Step 1: Install Python (if necessary)

Python 3.7 or higher must be installed:
Check if Python 3 is already installed:

`python3 --version`

If not installed, download and install Python from python.org.

Alternatively, install Python using Homebrew:

        brew install python

pip (Python's package manager) should be included with Python. Verify it by running:

    `python3 -m pip --version`

If it's missing, reinstall Python or follow these instructions.

Step 2: Download the Latest Release

  * Visit the [Releases](https://github.com/jdalbey/libbyfetch/releases) page.
  * Download the zip file for the latest release.

Step 3: Unzip the file:

Open Finder and navigate to the downloaded file.
Double-click the zip file to extract it.

Step 4: Install Dependencies

Open the extracted folder in Terminal by right-clicking the folder and select "Services > New Terminal at Folder" (or open Terminal and navigate to the folder manually using cd).
Install the required Python modules:

    `python -m pip install selenium selenium-wire pycurl`

### Dependency note
Note that it may be necessary to uninstall a dependency, `blinker` ver 1.9.0 and downgrade to 1.7.0
Here are the detailed steps, using pip.  
`pip show blinker` This should reveal the version is 1.9.0  
`pip uninstall blinker` Uninstall the module  
`pip install blinker==1.7.0` Install blinker with the specific version we want  
`pip show blinker` Should now have version 1.7 installed.

## Usage 
To run the program, execute the following command:

  `python3 libbyfetch.py`

## Example 
```%python libbyfetch.py
Initializing LibbyApp
Reading library card configuration file.
Available library systems are:
    1. sfpl
Choose a library id (number): 1
Loading library page for 'sfpl'
Starting signin with your library card.
Card Number set successfully.
'Next' Button clicked.
PIN entered.
'Sign In' Button clicked.
Sign In completed.
Loans page loaded.
1. The Bad Beginning       2. The Stinky Cheese Man   3. The Boxcar Children Beg
4. The Sleepless           5. And Tango Makes Three   6. The Three-Body Problem 
Enter the number of the desired title: 1
Open Audiobook button clicked.
Retrieving audiobook url...
waiting
waiting
waiting
Ready to fetch audio book The Bad Beginning
The_Bad_Beginning_Part01.mp3
Download progress:  0%  10%  20%  30%  40%  50%  60%  70%  80%  90%  100% 
The_Bad_Beginning_Part02.mp3
Download progress:  0%  10%  20%  30%  40%  50%  60%  70%  80%  90%  100% 
The_Bad_Beginning_Part03.mp3
Download progress:  0%  10%  20%  30%  40%  50%  60%  70%  80%  90%  100% 
The_Bad_Beginning_Part04.mp3
Download progress: 
Fetch completed.  4 files downloaded.
Removing scrap file:  The_Bad_Beginning_Part04.mp3
That's all Folks!
```

### Limitations
* Currently only works with Chrome.
* Error checking is rudimentary at best.  I built this for my personal use so it isn't production quality code.
* This program relies on a browser automation tool so it's inherently fragile.  If the libbyapp.com website changes even the smallest bit this program could break.
* Tested only on Linux.  Community reports it may work with other systems that have Python installed e.g. Windows.
* Tested only with audiobooks with English-language titles.  No attempt has been made at internationalization.
* The displayed list of audiobooks truncates the titles in order to fit a 3-column format.
* The downloaded MP3 files are placed in the current directory.  There is no option to specify a download folder.

## Error Messages


* `Missing or malformed configuration file`
* `Malformed configuration file`  
Couldn't read the configuration file data. Check that the file is formatted correctly as described above.
* `Choice not in valid range.  Quitting.`
* `Sorry, can't find details for library`
* `Sorry, your library card (or PIN) could not be verified.`
* `Login seems to have failed. Please verify these credentials and retry:`
* `Login failed, sorry.`  
Unable to log you in to Libby.  Verify that the configuration file data is correct.  Sometimes Libby just hiccups and won't recognize the credentials.  It's almost always a transient issue re-running the script will be successful. 

```Card not verified, probably a Libby error, we will retry in a few seconds.```  
Libby frequently gets confused and fails to verify a valid card.  The program will retry 3 times before giving up.

```It appears you have no audiobooks on loan at this library```   
Unable to find any audiobooks on the Loans page.  

```Sorry your choice is not in the list```  
A numeric entry was made that was outside the range of the displayed list.

* `Unable to find 'Sign In With My Card' button.`
* `An error occurred entering card number:`
* `An error occurred finding button:`
* `An error occurred filling PIN:`
* `An error occurred finding Sign In button:`
* `Loans page seems to not have loaded.  Try again.`
* `Exception retrieving book`
* `Failed to delete scrap file - probably programmer error`
* `Abnormal exit.`  
These errors most likely result from flaws in the program.  Try running the program again after a minute and if the error message persists please notify the developers. 

```Choice must be a number. Quitting.```  
When selecting a book title from the list of available audiobooks you must enter the number associated with the list item.  Entering a zero or an alphabetic character will terminate the program (which can be a handy shortcut way to exit at times.)
## Disclaimer

This software is provided without any warranty of any kind. The authors make no guarantees, express or implied, regarding the functionality or performance of the software. 

This software is not affliated, endorsed or certified by OverDrive. 

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Problem Reporting
Please submit problem reports to the Issues section of this repository.
