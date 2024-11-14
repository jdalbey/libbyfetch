# LibbyFetch - Download MP3 audiobooks from libbyapp.com
#
# Copyright (c) 2024 John Dalbey
#

#pip install selenium selenium-wire pycurl
# Note: must uninstall Blinker 1.9 and install v1.7
import time, os, pycurl
from selenium.common import TimeoutException
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def do_login_steps(driver):
    config_filename = "library_card_config.txt"
    try:
        print ("Reading library card configuration file.")
        library_config = []
        # Read library card configuration info: library code, card #, PIN
        f = open(config_filename, 'r')
        library_config = f.read().split(",")
        library_id = library_config[0]
        library_cardnum = library_config[1]
        library_pin = None
        # Check if a PIN parameter is included
        if len(library_config) == 3:
            library_pin = library_config[2]

        print (f"Loading library page for '{library_id}'")
        driver.get(f"https://libbyapp.com/library/{library_id}")
        WebDriverWait(driver, 10)

        # Find the "Sign In" button by its class name and text content
        button_xpath = "//button[contains(@class, 'interview-answer-action') and contains(@class, 'halo') and .//span[@role='text' and (text()='Sign In With My Card' or text()='Try Again')]]"
        try: # Find the button using XPath
            button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
            # Locate the prompt element
            span_element = driver.find_element(By.CSS_SELECTOR, '.interview-episode-say span')
            # Get the text from the span element
            span_text = span_element.text
            if span_text.endswith("details about this library."):
                print (f"Sorry, can't find details for library '{library_id}'")
                print ("Please confirm the library abbreviation and try again.")
                exit()
            else:
                button.click()
                print("Starting signin with your library card.")
        except Exception as e:
            print(f"Unable to find 'Sign In With My Card' button.")
            exit()

        # Find and fill the Card Number input field
        input_xpath = "//input[@class='shibui-form-input-control shibui-form-field-control' and @placeholder='card number']"
        try:  # Wait for the input field to be present
            input_field = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, input_xpath)) )
            # Fill in the value
            input_field.send_keys(library_cardnum)
            time.sleep(1)
        except Exception as e:
            print(f"An error occurred entering card number: {e}")

        # See if the config has a PIN,
        if library_pin is not None:
            # Find the "Next" button by its class name and text content
            button_xpath = "//button[contains(@class, 'interview-answer-action') and contains(@class, 'halo') and .//span[@role='text' and text()='Next']]"
            try: # Find the button using XPath
                button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
                print("Card Number set successfully.")
                button.click()
                print("'Next' Button clicked.")
            except Exception as e:
                print(f"An error occurred finding button: {e}")
                exit()

            # Find and fill the PIN input field
            input_id = "shibui-form-input-control-0002"
            try:  # Wait for the input field to be present
                input_field = WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.ID, input_id)) )
                # Fill in the value
                input_field.send_keys(library_pin)
                time.sleep(1)
                print("PIN entered.")
            except Exception as e:
                print(f"An error occurred filling PIN: {e}")
                exit()

        # if no PIN continue here
        retry_count = 0
        signin_complete = False
        while not signin_complete and retry_count <= 3:
            # Find and click the "Sign In" button by its class name and text content
            button_xpath = "//button[contains(@class, 'interview-answer-action') and contains(@class, 'halo') and .//span[@role='text' and text()='Sign In']]"
            try: # Find the button using XPath
                button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
                button.click()
                print("'Sign In' Button clicked.")
            except Exception as e:
                print(f"An error occurred finding Sign In button: {e}")
                exit()


            # "Next" button will appear at this point.
            button_xpath = "//button[contains(@class, 'interview-answer-action') and contains(@class, 'halo') and .//span[@role='text' and (text()='Next' or text()='Try Again')]]"
            try: # Find the button using XPath
                button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
                # Locate the prompt element
                span_element = driver.find_element(By.CSS_SELECTOR, '.interview-episode-say span')
                # Get the text from the span element
                span_text = span_element.text
                if span_text.startswith("Unfortunately"):
                    print("Card not verified, probably a Libby error, we will retry in a few seconds.")
                    retry_count += 1
                    time.sleep(5)
                    print ("Retrying...")
                    # Click "Try Again" and the card number field reappears.
                    button.click()
                elif span_text.startswith("We could not verify your card"):
                    print (f"Sorry, your library card (or PIN) could not be verified.")
                    print(f"Please confirm these credentials and try again: {library_config}")
                    exit()
                else:
                    button.click()
                    print("Sign In completed.")
                    signin_complete = True
            except Exception as e:
                print(f"Login seems to have failed. ")
                print (f"Please verify these credentials and retry: {library_config}")
                exit()
        if retry_count > 3:
            print (f"Giving up after {retry_count} retries.")
            exit()
    except FileNotFoundError:
        print(f"Missing or malformed configuration file: {config_filename}")
        exit()
    except IndexError:
        print(f"Malformed configuration file: {config_filename}")
        exit()
    except Exception as e:
        print (f"{e} Login failed, sorry.")
        exit()

def display_in_columns(items):
    # Determine the number of rows needed
    rows = (len(items) + 2) // 3

    for i in range(rows):
        # Get the items for the current row
        row_items = []
        for j in range(3):
            index = i*3 + j
            if index < len(items):
                # Extract the text from the span with class "title-tile-title"
                title_text = items[index].find_element(By.CLASS_NAME, "title-tile-title").text
                # Preface the title with an index number
                brief_title = str(index+1) + ". " + title_text.strip()[:23]
                row_items.append(brief_title)
            else:
                row_items.append("")

        # Format the row items to be 26 characters wide
        formatted_row = f"{row_items[0]:<26} {row_items[1]:<26} {row_items[2]:<26}"
        # Print the formatted row
        print(formatted_row)


def list_titles(driver):
    # Find all title-tile divs
    titles = driver.find_elements(By.CLASS_NAME, "title-tile")
    if len(titles) == 0:
        print ("\nIt appears you have no audiobooks on loan at this library.")
        print ("Nothing to download, quitting.")
        exit()

    # Display the list in columns
    display_in_columns(titles)

    title_list = []
    for index, title in enumerate(titles, start=1):
        # Extract the text from the span with class "title-tile-title"
        title_text = title.find_element(By.CLASS_NAME, "title-tile-title").text
        title_list.append(title_text)
        #print(f"{index}. {title_text}")
    return titles, title_list

def open_audiobook(titles, choice):
    try:
        if choice < 1:
            raise IndexError
        # Find the specific title-tile div based on user choice
        chosen_title = titles[choice - 1]
        # Find and click the "Open Audiobook" button within the chosen div
        open_button = chosen_title.find_element(By.XPATH, ".//button[span[text()='Open Audiobook']]")
        open_button.click()
        print("Open Audiobook button clicked.")
        return chosen_title
    except IndexError:
        print("Sorry your choice is not in the list.")
        exit()

def choose_book(driver):
    try:
        # Navigate to the page listing audiobooks on loan
        driver.get("http://libbyapp.com/shelf/loans/default,audiobook")

        try:
            # Wait for the <h1> Loan element
            # NB: Even after the H1 element is present it never becomes "visible".  There's a graphical fade-in
            # effect that is probably interfering.
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "screen-shelf-collation-heading"))
            )

            # For future reference:
            # title_list = driver.find_elements(By.CLASS_NAME, "title-list")
            # collation_empty_state = driver.find_elements(By.CLASS_NAME, "collation-empty-state")
            # print (f"title-list classes: {len(title_list)}  empty-state classes: {len(collation_empty_state)} ")
            # titles = driver.find_elements(By.CLASS_NAME, "title-tile")
            # print (f"Number of titles found: {len(titles)}")
            # Title list length: 0  Empty state list: 1    when there are zero audiobook loans
            # title-list classes: 1  empty-state classes: 0  When we have loans
            # number of titles found can be > 0 even if the book titles aren't yet available.

            # The following sleep() allows the animation to complete
            # at which time the audiobook titles can be viewed and accessed.
            # There may be a better way to achieve this than a hardcoded sleep.
            time.sleep(2)
            print("Loans page loaded.")
        except TimeoutException:
            print("Loans page seems to not have loaded.  Try again.")
            exit()

        # List all titles and get the titles elements
        titles, title_names = list_titles(driver)

        # Prompt the user to enter the number of the desired title
        choice = int(input("Enter the number of the desired title: "))

        # Open the audiobook for the chosen title
        open_audiobook(titles, choice)
        selected_title = title_names[choice - 1] # save this so we can show it when we start download

        # This is the 'secret' that allows this script to do its magic
        # Once the audiobook is opened in the browser, libbyapp will use a GET request to obtain the MP3 file.
        # Our script will snoop on the network requests looking for a GET request with an URL that contains
        # a specific phrase that identifies the MP3 file.
        print ("Retrieving audiobook url...")
        magic_phrase = "Fmt425-Part"  # a unique phrase that identifies Libby's request for an MP3
        cookies = None
        book_url = ""
        while (cookies == None):
            time.sleep(2)
            print (f"waiting")
            for request in driver.requests:
                if request.method == "GET":
                    book_url = request.url
                    # Look for the request that has the MP3 name
                    if book_url.find(magic_phrase) > 0:
                        cookies = request.headers["cookie"]
                        break
        return selected_title, book_url, cookies
    except ValueError:
        print ("Choice must be a number. Quitting.")
        exit()
    except Exception as e:
        print (f"Exception retrieving book {e}")
        exit()

# Initialize a variable to track the last reported percentage
last_reported_percent = -1

def do_pycurl_cmd(book_title, deweyURL, cookie):
    # Progress callback function to print only at multiples of 10%
    def progress(download_t, download_d, up_t, up_d):
        global last_reported_percent

        if download_t > 0:  # Only calculate percentage if total size is known
            percent = int((download_d / download_t) * 100)

            # Print progress if it is a multiple of 10 and hasn't been reported yet
            if percent % 10 == 0 and percent != last_reported_percent:
                print(f" {percent}% ", end='')
                last_reported_percent = percent

    # Initialize pycURL object
    c = pycurl.Curl()
    # Set URL
    c.setopt(c.URL, deweyURL)

    # Follow redirects (equivalent to `-L`)
    c.setopt(c.FOLLOWLOCATION, True)

    # Set custom headers
    c.setopt(c.HTTPHEADER, [
        'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0',
        'Accept: audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5',
        'Accept-Language: en-US,en;q=0.5',
        'Range: bytes=0-',
        'DNT: 1',
        'Connection: keep-alive',
        'Sec-Fetch-Dest: audio',
        'Sec-Fetch-Mode: cors',
        'Sec-Fetch-Site: same-origin',
        'Sec-GPC: 1',
        'Accept-Encoding: identity',
        'Priority: u=4',
        'TE: trailers'
    ])
    # Set cookies as a single string (format: "cookie1=value1; cookie2=value2")
    c.setopt(c.COOKIE, cookie)
    # Specify the path to your CA certificates bundle
    c.setopt(c.CAINFO, '/etc/ssl/certs/ca-certificates.crt')

    # Output file
    with open(book_title, 'wb') as f:
        c.setopt(c.WRITEDATA, f)
        # Set up the progress function callback
        c.setopt(c.XFERINFOFUNCTION, progress)
        c.setopt(c.NOPROGRESS, False)  # Enable the progress function
        print ("Download progress: ", end='')
        # Perform the request
        c.perform()
        print ()
        c.close()


def fetch_audio_files(title, deweyURL, cookie):
    audio_filename = title + "_Part01.mp3"
    filesize = 99
    part_counter = 1
    # Since we don't know in advance how many mp3 files comprises the audiobook
    # we just iterate fetching files until we get one with a size of 1 byte.
    while filesize > 1:
        # Rename the command with the current part number
        part_num = "Part" + f"{part_counter:02}"
        audio_filename = title + "_" + part_num + ".mp3"
        currentURL = deweyURL.replace("Part01",part_num)
        print (audio_filename)
        do_pycurl_cmd(audio_filename, currentURL, cookie)
        # Retrieve the filesize of the downloaded .mp3 file
        filesize = os.path.getsize(audio_filename)
        # increment the part number for the next iteration
        part_counter += 1

    print(f"Fetch completed.  {part_counter - 1} files downloaded.")
    # Delete the last file since it is only 1 byte long.
    print("Removing scrap file: ", audio_filename)
    try:
        os.remove(audio_filename)
    except FileNotFoundError:
        print("Failed to delete scrap file - probably programmer error")
        exit()


# Entry point for the application
if __name__ == "__main__":
    driver = None
    try:
        # Initialize the WebDriver
        # Known Issue: Apparently there's a known issue with the Chrome webdriver. If the user manually minimizes
        # the browser window while the script is running it causes the driver to lose focus or fail to interact with
        # the page elements properly.  Firefox doesn't have this problem.  The workaround is to run in headless mode,
        # as shown below.
        print ("Initializing LibbyApp")
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        do_login_steps(driver)

        book_name, deweyURL, cookie = choose_book(driver)
        book_title = book_name.replace(" ", "_")
        print (f"Ready to fetch audio book {book_name}")

        fetch_audio_files(book_title, deweyURL, cookie)
        print ("That's all Folks!")
        driver.quit()
    except Exception as e:
        print ("Abnormal exit.",e)
        driver.quit()
        exit(-1)

