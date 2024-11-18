# Frequently Asked Questions

### Features

- **1.** Is this program legal?
  - **Answer:** The most likely U.S. regulation regarding this program would be the DMCA which prohibits circumventing copy-protection schemes. This program does **not** violate the DMCA.

### Installation
- **1.** I'm getting this error `ModuleNotFoundError: No module named 'blinker._saferef'`
  - ** Answer:** See the "Dependency note" in the README.

### Error Messages

- **1.** Are there explanations for error messages issued by the program?
  - **Answer:** See the list below.


* `Missing or malformed configuration file`
* `Malformed configuration file`  
Couldn't read the configuration file data. Check that the file is formatted correctly as described above.

* `Sorry, can't find details for library`
* `Sorry, your library card (or PIN) could not be verified.`
* `Login seems to have failed. Please verify these credentials and retry:`
* `Login failed, cause unknown.`  
Unable to log you in to Libby.  Verify that the configuration file data is correct.  Sometimes Libby just hiccups and won't recognize the credentials.  It's almost always a transient issue re-running the script will be successful. 

```Card not verified, probably a Libby error, we will retry in a few seconds.```  
Libby frequently gets confused and fails to verify a valid card.  The program will retry 3 times before giving up.

```It appears you have no audiobooks on loan at this library```   
Unable to find any audiobooks on the Loans page.  

```Sorry your choice is not in the list```  
A numeric entry was made that was outside the range of the displayed list.

* `Unable to find 'Sign In With My Card' button.`
* `Unable to find full library name where expected.`
* `An error occurred entering card number:`
* `An error occurred finding button:`
* `An unknown error occurred completing PIN field.`
* `An error occurred finding Sign In button:`
* `An error occurred for an unknown cause.` 
* `Internal error - expected button not found after entering card number.`
* `Loans page seems to not have loaded.  Try again.`
* `Exception retrieving book`
* `Failed to delete scrap file - probably programmer error`  
These errors most likely result from flaws in the program.  Try running the program again after a minute and if the error message persists please notify the developers. 

`Choice must be a number. Quitting.`  
`Sorry your choice is not in the list. Quitting.`  
When selecting a book title from the list of available audiobooks you must enter the number associated with the list item.  Entering a zero or an alphabetic character will terminate the program (which can be a handy shortcut way to exit at times.)
