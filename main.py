#main.py
import time
from seleniumbase import SB
from config.config import URL, EMAIL, PASSWORD



def open_page(sb, url):
    """Opens the webpage and waits for it to load completely."""
    sb.driver.uc_open_with_reconnect(url, reconnect_time=24)

def enter_credentials(sb, email, password):
    """Enters email and password into the respective fields."""
    sb.wait_for_element("input[id=email]", timeout=20)
    sb.type("input[id=email]", email, by="css selector")
    sb.wait_for_element("input[id=password]", timeout=20)
    sb.type("input[id=password]", password, by="css selector")

def click_sign_in(sb):
    """Clicks the 'Sign In' button if it is visible and enabled."""
    button_css_selector = "button.mat-focus-indicator"
    sb.wait_for_element(button_css_selector, timeout=40)

    if sb.is_element_visible(button_css_selector) and sb.is_element_enabled(button_css_selector):
        sb.click(button_css_selector)
        # print("Button 'Sign In' clicked.")
        time.sleep(10)  # Wait for the page to load'
        start_button = "button.mat-focus-indicator.btn.mat-btn-lg.btn-brand-orange.d-none.d-lg-inline-block.position-absolute.top-n3.right-0.z-index-999.mat-raised-button.mat-button-base"
        sb.wait_for_element(start_button, timeout=20)
        sb.click(start_button)

        # Open the Visa Center dropdown
        mat_select_center = 'mat-select[formcontrolname="centerCode"]'
        sb.wait_for_element(mat_select_center, timeout=20)
        sb.click(mat_select_center)
        time.sleep(2)  # Ensure the dropdown is fully opened

        # Select the option from the Visa Center dropdown
        option_to_select = 'mat-option[id="LTRPBK"]'
        sb.wait_for_element(option_to_select, timeout=20)
        sb.click(option_to_select)
        time.sleep(4)  # Ensure the option is selected


        # Open the Visa Category dropdown
        mat_select_category = 'mat-select[formcontrolname="selectedSubvisaCategory"]'
        sb.wait_for_element(mat_select_category, timeout=20)
        if sb.is_element_visible(mat_select_category) and sb.is_element_enabled(mat_select_category):
            sb.click(mat_select_category)
            time.sleep(2)  # Ensure the dropdown is fully opened

            # Ensure the options are fully loaded
            category_options_loaded = '//mat-option//span'
            sb.wait_for_element(category_options_loaded, timeout=20)

            # Select the option with id="TRPVC" from the Visa Category dropdown
            category_option = 'mat-option[id="TRPVC"]'
            sb.wait_for_element(category_option, timeout=20)
            sb.click(category_option)
            time.sleep(2)  # Ensure the option is selected
        else:
            print("Visa Category dropdown is not visible or enabled.")


            # Open the Sub Visa Category dropdown
        mat_select_sub_category = 'mat-select[formcontrolname="visaCategoryCode"]'
        sb.wait_for_element(mat_select_sub_category, timeout=20)
        if sb.is_element_visible(mat_select_sub_category) and sb.is_element_enabled(mat_select_sub_category):
            sb.click(mat_select_sub_category)
            time.sleep(2)  # Ensure the dropdown is fully opened

            # Ensure the options are fully loaded
            sub_category_options_loaded = '//mat-option//span'
            sb.wait_for_element(sub_category_options_loaded, timeout=20)

            # Select the option with id="TRPVC" from the Sub Visa Category dropdown
            sub_category_option = 'mat-option[id="TSV6"]'
            sb.wait_for_element(sub_category_option, timeout=20)
            sb.click(sub_category_option)
            time.sleep(5)  # Ensure the option is selected

            slot_container = "div.alert"
            sb.wait_for_element(slot_container, timeout=20)
            slot_text = sb.get_text(slot_container)
            print(slot_text)
        else:
            print("Sub Visa Category dropdown is not visible or enabled.")

    else:
        print("Button is not visible or enabled.")

def main():
    """Main function to execute the script."""
    with SB(uc=True) as sb:
        open_page(sb, URL)
        enter_credentials(sb, EMAIL, PASSWORD)
        click_sign_in(sb)
        # The browser will remain open for further actions
        # Uncomment the line below if you want to close the browser manually later
        # sb.quit()

if __name__ == "__main__":
    main()
