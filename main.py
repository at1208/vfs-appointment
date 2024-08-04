#main.py
import time
from seleniumbase import SB
from config.config import URL, EMAIL, PASSWORD



def open_page(sb, url):
    """Opens the webpage and waits for it to load completely."""
    sb.driver.uc_open_with_reconnect(url, reconnect_time=12)

def enter_credentials(sb, email, password):
    """Enters email and password into the respective fields."""
    sb.wait_for_element("input[id=email]", timeout=20)
    sb.type("input[id=email]", email, by="css selector")
    sb.wait_for_element("input[id=password]", timeout=20)
    sb.type("input[id=password]", password, by="css selector")

def click_sign_in(sb):
    """Clicks the 'Sign In' button if it is visible and enabled."""
    button_css_selector = "button.mat-focus-indicator"
    sb.wait_for_element(button_css_selector, timeout=20)

    if sb.is_element_visible(button_css_selector) and sb.is_element_enabled(button_css_selector):
        sb.click(button_css_selector)
        print("Button 'Sign In' clicked.")
        time.sleep(10)  # Wait for the page to load'
        start_booking_button = "button.mat-focus-indicator.btn.mat-btn-lg.btn-brand-orange.d-none.d-lg-inline-block.position-absolute.top-n3.right-0.z-index-999.mat-raised-button.mat-button-base"
        sb.wait_for_element(start_booking_button)
        sb.click(start_booking_button)

        form_element = sb.wait_for_element("mat-select[formcontrolname=centerCode]")

        print(sb.get_attribute(form_element, "outerHTML"))



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
