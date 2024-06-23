
#Hi sir This is Rohith H just graduated from PES University
# Now i will demonstrate the second process that is the Automation Test 02 - Functional Testing Case

# I will be showing demo for the automation of the login page and the importing the data


# Below is the code for the same
# On the left side u can see that there is no screenshot of any pages over here
# Now we will be running the Code
# That's it thank you sir

# One more thing sir previously i had no experience using the selenium or any other tool before i got this test link and i am fresher
# I didn't even knew this was possible so after learning all the basics of the selenium drivers from the youtube i have learnt on how to perform the task
# Now i have completed the 2 tasks I am very eager to learn and adapt to the situations very well as u can see i am a fast learner
# I will be much much hapier to work with u guys and learn more and develop my skills and devolop in this field
# It will be great honour for me to get a chance to work with U guys  Once Again Thank you Sir :)
# i will  be looking forward to hear from You sir Thank You :)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def login_to_dealsdray(driver, username, password):
    driver.get("https://demo.dealsdray.com/")
    driver.maximize_window()
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.send_keys(username)

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_field.send_keys(password)

    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        login_button.click()
    except TimeoutException:
        print("Login button not found or not clickable. Please check the login button element.")
        return

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    driver.save_screenshot("Screenshot_After_Login.png")
    print("Login successful.")

def navigate_to_orders(driver):
    try:
        main_menu_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "css-sukebr"))
        )
        main_menu_button.click()

        orders_menu_item = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Orders']/parent::button"))
        )
        orders_menu_item.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        print("Navigated to Orders page.")
    except TimeoutException:
        print("Navigation to Orders page timed out. Please check the menu items.")
    except NoSuchElementException:
        print("Navigation to Orders page failed. Menu items not found.")
    driver.save_screenshot("Screenshot_After_Orderspage.png")
def click_add_bulk_order(driver):
    try:
        add_bulk_order_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButtonBase-root.css-vwfva9"))
        )
        add_bulk_order_button.click()
        print("Clicked 'Add Bulk Order' button.")
    except TimeoutException:
        print("Add Bulk Order button not found or not clickable. Please check the button element.")
    except NoSuchElementException:
        print("Add Bulk Order button not found. Please check the button element.")
    driver.save_screenshot("Screenshot_After_Bulk_order.png")
def upload_file(driver, file_path):
    try:
        import_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "mui-7"))
        )
        import_button.send_keys(file_path)
        print("File uploaded.")
    except TimeoutException:
        print("Import button not found or not clickable. Please check the button element.")
    except NoSuchElementException:
        print("Import button not found. Please check the button element.")
    driver.save_screenshot("Screenshot_After_Upload_file.png")
def click_import_button(driver):
    try:
        import_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButtonBase-root.css-6aomwy"))
        )
        import_button.click()
        print("Clicked 'Import' button.")
    except TimeoutException:
        print("Import button not found or not clickable. Please check the button element.")
    except NoSuchElementException:
        print("Import button not found. Please check the button element.")
    driver.save_screenshot("Screenshot_After_importbutton.png")
def click_validate_data_button(driver):
    try:
        validate_data_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.MuiButtonBase-root.css-6aomwy"))
        )
        validate_data_button.click()
        print("Clicked 'Validate Data' button.")

        # Handle the alert
        handle_alert(driver)

    except TimeoutException:
        print("Validate Data button not found or not clickable. Please check the button element.")
    except NoSuchElementException:
        print("Validate Data button not found. Please check the button element.")
    driver.save_screenshot("Screenshot_After_ValidateButton.png")
def handle_alert(driver):
    try:
        # Wait for the alert to be present
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

        # Accept the alert (clicking OK)
        alert.accept()

        print("Alert accepted.")

    except NoAlertPresentException:
        print("No alert present.")

def take_screenshot(driver, file_path):
    driver.save_screenshot(file_path)
    print(f"Screenshot saved to {file_path}")

# Example usage
username = "prexo.mis@dealsdray.com"
password = "prexo.mis@dealsdray.com"
file_path = "D:\\UI_UX_Course\\Automation_Testing\\Functional_Testing\\demo-data.xlsx"  # Replace with the actual file path
screenshot_path = "Final_page_screenshot.png"

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
login_to_dealsdray(driver, username, password)
navigate_to_orders(driver)
click_add_bulk_order(driver)
upload_file(driver, file_path)
click_import_button(driver)
click_validate_data_button(driver)
take_screenshot(driver, screenshot_path)

print("Browser window remains open. Please close it manually when finished.")
input("Press Enter to close the browser and end the script...")

driver.quit()
