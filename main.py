import csv
import time
import io
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import base64
import re
import urllib

import pytesseract
from PIL import Image

# Add the path to the Tesseract executable if not available in the system PATH

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        driver = webdriver.Chrome()
        driver.get('https://service2.diplo.de/rktermin/extern/appointment_showForm.do?locationCode=isla&realmId=108&categoryId=1600')
        time.sleep(1)

        lastname = driver.find_element(By.XPATH, '//*[@id="appointment_newAppointmentForm_lastname"]')
        lastname.send_keys(line[0])

        firstname = driver.find_element(By.XPATH, '//*[@id="appointment_newAppointmentForm_firstname"]')
        firstname.send_keys(line[1])

        email = driver.find_element(By.XPATH, '//*[@id="appointment_newAppointmentForm_email"]')
        email.send_keys(line[2])

        repeatemail = driver.find_element(By.XPATH, '//*[@id="appointment_newAppointmentForm_emailrepeat"]')
        repeatemail.send_keys(line[3])

        passport = driver.find_element(By.XPATH, '//*[@id="appointment_newAppointmentForm_fields_0__content"]')
        passport.send_keys(line[4])

        citizenship = Select(driver.find_element(By.XPATH, '//*[@id="appointment_newAppointmentForm_fields_1__content"]'))
        citizenship.select_by_value(line[5])

        number = driver.find_element(By.XPATH, '//*[@id="appointment_newAppointmentForm_fields_2__content"]')
        number.send_keys(line[6])

        purpose = Select(driver.find_element(By.XPATH, '//*[@id="appointment_newAppointmentForm_fields_3__content"]'))
        purpose.select_by_value(line[7])

        # Get the CAPTCHA image element
        captcha_image_element = driver.find_element(By.XPATH, '//captcha/div')

        # Get the base64-encoded image data
        captcha_image_data = captcha_image_element.get_attribute('style')
        url_pattern = r'data:(.*?)"'
        match = re.search(url_pattern, captcha_image_data)
        if match:
            url = match.group(0).rstrip('"')

        urllib.request.urlretrieve(url, "local-filename.jpg")

        

        # Find the CAPTCHA input element and enter the text
        # captcha_input_element = driver.find_element(By.XPATH, '//*[@id="appointment_newAppointmentForm_captchaText"]')
        # captcha_input_element.send_keys(captcha_text)

        # Uncomment the following lines to submit the form (if needed)
        # submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        # submit.click()

        time.sleep(10)
        driver.quit()
