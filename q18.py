from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def automate_demoqa_textbox():
  # Initialize WebDriver
  driver = webdriver.Chrome()
  driver.maximize_window()

  try:
    print('Navigating to DemoQA Text Box page. Entering data...')
    driver.get('https://demoqa.com/text-box')

    # Test data to fill
    test_data = {
        'full_name': 'Anna George',
        'email': 'anna@example.com',
        'current_address': '123 Main Street',
        'permanent_address': '456 Side Avenue',
    }

    # Fill the form fields using explicit waits
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'userName'))
    ).send_keys(test_data['full_name'])

    driver.find_element(By.ID, 'userEmail').send_keys(test_data['email'])
    driver.find_element(By.ID, 'currentAddress').send_keys(
        test_data['current_address']
    )
    driver.find_element(By.ID, 'permanentAddress').send_keys(
        test_data['permanent_address']
    )
# Scroll down to the submit button
    submit_btn = driver.find_element(By.ID, 'submit')
    driver.execute_script('arguments[0].scrollIntoView(true);', submit_btn)

    # Use JavaScript to click the button directly (bypasses overlapping footers)
    driver.execute_script('arguments[0].click();', submit_btn)
    print('Form submitted successfully. Verifying output...')

    # Wait for the output section to appear and grab all its text
    output_div = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'output'))
    )
    output_text = output_div.text

    # Robust verification: check if your input values exist anywhere in the output box
    assert (
        test_data['full_name'] in output_text
    ), f"Full Name verification failed! Got: {output_text}"
    assert (
        test_data['email'] in output_text
    ), f"Email verification failed! Got: {output_text}"
    assert (
        test_data['current_address'] in output_text
    ), f"Current address verification failed! Got: {output_text}"
    assert (
        test_data['permanent_address'] in output_text
    ), f"Permanent address verification failed! Got: {output_text}"

    print('All assertions and verifications passed successfully!')

  except Exception as e:
    print(f'An error occurred during automation: {e}')
    raise
  finally:
    print('Closing the browser.')
    driver.quit()


if __name__ == '__main__':
  automate_demoqa_textbox()