# Libby Fetch

Libby Fetch is a program for downloading MP3 audiobooks from libbyapp.com website
### Warning
Several users have reported that after using this program their library card can no longer access materials they have on loan through the Libby App. For example, issue #19. _Use this program at your own risk!_  
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

    python3 -m pip install -r requirements.txt


## Installation (Windows)

Step 1: Install Python (if necessary)

Step 2: Download the Latest Release
  * Visit the [Releases](https://github.com/jdalbey/libbyfetch/releases) page.
  * Download the zip file for the latest release.

Step 3: Unzip the file

Step 4: Install Dependencies (with pip)

## Installation (MacOS)

Step 1: Install Python (if necessary)

Step 2: Download the Latest Release
  * Visit the [Releases](https://github.com/jdalbey/libbyfetch/releases) page.
  * Download the zip file for the latest release.

Step 3: Unzip the file

Step 4: Install Dependencies (with pip)

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

When complete the MP3 files will appear in the current directory.

Optional:  
  `python3 set_ID3_tags.py`  
This program will set the MP3 filename into the title field of the ID3 tag for each MP3 file in the current directory.  This is helpful as the ID3 tag provides the data most MP3 players display for the book title. 

## Example
```%python libbyfetch.py
Initializing LibbyApp.
Reading library card configuration file.
Loading library page for 'sfpl'
Starting signin to San Francisco Public Library.
Library card number entered.
PIN entered.
Sign In completed.
Loans page loaded.
1. Crow Mary               2. Ask Mr. Bear            3. Black Wolf
4. The Bad Beginning       5. The Three-Body Problem
Enter the number of the desired title: 2
Opening Audiobook.
Retrieving audiobook url...
waiting
waiting
Ready to fetch audio book Ask Mr. Bear.
Ask_Mr._Bear_Part01.mp3
Download progress:  0%  10%  20%  30%  40%  50%  60%  70%  80%  90%  100%
Ask_Mr._Bear_Part02.mp3
Download progress:
Fetch completed.  2 files downloaded.
Removing scrap file:  Ask_Mr._Bear_Part02.mp3
That's all Folks!
```

### Limitations
* Currently only works with Chrome.
* Error checking is rudimentary at best.  I built this for my personal use so it isn't production quality code.
* This program relies on a browser automation tool so it's inherently fragile.  If the libbyapp.com website changes even the smallest bit this program could break.
* Tested only on Linux. Some users report being able to make it work on Windows.
* Tested only with audiobooks with English-language titles.  No attempt has been made at internationalization.
* The displayed list of audiobooks truncates the titles in order to fit a 3-column format.
* The downloaded MP3 files are placed in the current directory.  There is no option to specify a download folder.

## Disclaimer

This software is provided without any warranty of any kind. The authors make no guarantees, express or implied, regarding the functionality or performance of the software.

This software is not affliated, endorsed or certified by OverDrive.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Problem Reporting
Please submit problem reports to the Issues section of this repository.
