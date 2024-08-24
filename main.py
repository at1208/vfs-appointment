import time
import requests
from seleniumbase import SB
from config import URL, EMAIL, PASSWORD, API_ENDPOINT, API_TOKEN

def open_page(sb, url):
    """Opens the webpage and waits for it to load completely."""
    sb.driver.uc_open_with_reconnect(url, reconnect_time=12)

def enter_credentials(sb, email, password):
    """Enters email and password into the respective fields."""
    sb.wait_for_element("input[id=email]", timeout=20)
    sb.type("input[id=email]", email, by="css selector")
    sb.wait_for_element("input[id=password]", timeout=20)
    sb.type("input[id=password]", password, by="css selector")

def click_button(sb, css_selector, timeout=20, sleep_time=0):
    """Clicks a button if it is visible and enabled."""
    sb.wait_for_element(css_selector, timeout=timeout)
    if sb.is_element_visible(css_selector) and sb.is_element_enabled(css_selector):
        sb.click(css_selector)
        if sleep_time > 0:
            time.sleep(sleep_time)
        return True
    print(f"Button {css_selector} is not visible or enabled.")
    return False

def select_option(sb, dropdown_selector, option_id, timeout=20, sleep_time=0):
    """Selects an option from a dropdown by its ID."""
    sb.wait_for_element(dropdown_selector, timeout=timeout)
    sb.click(dropdown_selector)
    time.sleep(4)  # Ensure the dropdown is fully opened

    options_xpath = '//mat-option//span'
    sb.wait_for_element(options_xpath, timeout=timeout)

    option_selector = f'mat-option[id="{option_id}"]'
    sb.wait_for_element(option_selector, timeout=timeout)
    sb.click(option_selector)
    if sleep_time > 0:
        time.sleep(sleep_time)

def get_slot_text(sb, selector, timeout=20):
    """Retrieves the slot text from the specified container."""
    sb.wait_for_element(selector, timeout=timeout)
    return sb.get_text(selector)

def update_slot_text(slot_text):
    """Sends a PATCH request to update the slotText via API."""
    url = f"{API_ENDPOINT}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "slot": slot_text
    }
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Slot text updated successfully.")
    else:
        print(f"Failed to update slot text. Status code: {response.status_code}, Response: {response.text}")

def click_continue_button(sb):
    """Clicks the 'Continue' button with specific attributes."""
    button_selector = "button[type='button'].mat-focus-indicator.btn.mat-btn-lg.btn-block.btn-brand-orange"
    sb.wait_for_element(button_selector, timeout=20)
    sb.click(button_selector)


def enter_applicant_details(sb):
    """Applicant Details"""
    sb.wait_for_element("input[placeholder='Enter MIGRIS Application Number']", timeout=20)
    sb.type("input[placeholder='Enter MIGRIS Application Number']", "2408-LLG-5199", by="css selector")
    time.sleep(2)

    sb.wait_for_element("input[placeholder='Enter your first name']", timeout=20)
    sb.type("input[placeholder='Enter your first name']", "KAMRAN HAIDER", by="css selector")
    time.sleep(2)

    sb.wait_for_element("input[placeholder='Please enter last name.']", timeout=20)
    sb.type("input[placeholder='Please enter last name.']", "CHEEMA", by="css selector")
    time.sleep(2)

    select_option(sb, 'mat-select[id=mat-select-6]', "mat-option-6", sleep_time=5)
    time.sleep(2)

    sb.wait_for_element("input[id=dateOfBirth]", timeout=20)
    sb.type("input[id=dateOfBirth]", "16061998", by="css selector")
    time.sleep(2)

    select_option(sb, 'mat-select[id=mat-select-8]', "mat-option-164", sleep_time=5)
    time.sleep(2)

    sb.wait_for_element("input[placeholder='Enter passport number']", timeout=20)
    sb.type("input[placeholder='Enter passport number']", "CE4157092", by="css selector")
    time.sleep(2)

    sb.wait_for_element("input[id=passportExpirtyDate]", timeout=20)
    sb.type("input[id=passportExpirtyDate]", "13052027", by="css selector")
    time.sleep(2)

    sb.wait_for_element("input[placeholder='44']", timeout=20)
    sb.type("input[placeholder='44']", "92", by="css selector")
    time.sleep(2)

    sb.wait_for_element("input[placeholder='012345648382']", timeout=20)
    sb.type("input[placeholder='012345648382']", "9876543211", by="css selector")
    time.sleep(2)

    sb.wait_for_element("input[placeholder='Enter Email Address']", timeout=20)
    sb.type("input[placeholder='Enter Email Address']", "aman.geeksocean@gmail.com", by="css selector")


def click_save_button(sb):
    """Clicks the 'Save' button with specific attributes."""
    button_selector = "button.mat-focus-indicator.mat-stroked-button.mat-button-base.btn.btn-block.btn-brand-orange.mat-btn-lg"
    sb.wait_for_element(button_selector, timeout=20)
    sb.click(button_selector)
    print("save button clicked")
    time.sleep(2)

def main():
    """Main function to execute the script."""
    with SB(uc=True, headless=True) as sb:
        open_page(sb, URL)
        enter_credentials(sb, EMAIL, PASSWORD)

        if click_button(sb, "button.mat-focus-indicator", sleep_time=10):
            click_button(sb, "button.mat-focus-indicator.btn.mat-btn-lg.btn-brand-orange.d-none.d-lg-inline-block.position-absolute.top-n3.right-0.z-index-999.mat-raised-button.mat-button-base")

            select_option(sb, 'mat-select[formcontrolname="centerCode"]', "LTRPBK", sleep_time=6)
            select_option(sb, 'mat-select[formcontrolname="selectedSubvisaCategory"]', "TRPVC", sleep_time=4)
            select_option(sb, 'mat-select[formcontrolname="visaCategoryCode"]', "TSV6", sleep_time=5)

            slot_text = get_slot_text(sb, "div.alert")
            update_slot_text(slot_text)
            click_continue_button(sb)
            enter_applicant_details(sb)
            click_save_button(sb)


if __name__ == "__main__":
    main()
