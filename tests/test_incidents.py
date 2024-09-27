from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/path/to/chromedriver")
driver.get("http://localhost:5000/")

# Test case for submitting an incident
textarea = driver.find_element_by_id("incident")
textarea.send_keys("Test Incident")
textarea.send_keys(Keys.RETURN)

assert "Incident logged successfully!" in driver.page_source
driver.quit()
