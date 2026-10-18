selenium import webdriver
selenium.webdriver.comman.by import
selenium.webdriver.support.ui import WebDriverWait
selenium.webdriver.support import expected_conditions as EC

# Initialize the webdriver
driver= webdriver.chrome()

try:

	#1.open TestMu AI Selenium Playground
	driver.get("https://www.testmuai.com/selenium-playground/")
	driver.maximize_window()
	
	#Wait for page load and click on sample demo form
	wait = WebDriverWait(driver,10)
	
	input_form_link = wait.untill(EC.element_to_be_clickable((By.LINK_TEXT,"Input Form Submit")))
	
	input_form_link.click()
	
	#2. click "Submit" without filling in any information n the form
	submit_btn.click()
	
	#3.Assert "Please fill in this filed." error message 
	name_field = driver.find_element((By.ID,"name")
	validation_message =name_filed.get_attribute("validationMessage")
	print(f"Browser HTML5 validation message captured: {validation_message}")
	
	#4. Fill in name, Email and  other fileds
	name_field.send_keys("john Doe")
	driver.find_element(By.ID,"inputEmail4").send_keys("johndoe@example.com")
	driver.find_element(By.ID,"inputPassword4").send_keys("SecurePassword123")
	driver.find_element(By.ID,"company")..send_keys("TestMu AI")
	driver.find_element(By.ID,"websitename").send_keys("https://www.example.com")
	
	#5. from the country drop-down,select "United State"
	country_dropdown =Select(driver.find_element(By.NAME,"country"))
	country_dropdown.select_by_visible_text("United State")
	
	#6. Fill in all remaining fields 
	driver.find_element(By.ID,"inputCity").send_keys("New York")
	driver.find_element(By.ID,"inputAddress1").send_keys("123 Main St")
		driver.find_element(By.ID,"inputAddress2").send_keys("Apt 4B")
	driver.find_element(By.ID,"inputState").send_keys("New York")
	driver.find_element(By.ID,"inputZip").send_keys("10001")
	
	submit_btn.click()
	
	#7. Once submitted validate the success message
	Success_msg_elm = wait.untill(EC.presence_of_element_located((By.XPATH,"//p[@class='sucess-msg']")))
	success_text = sucess-msg_elem.text
	expected_message = "Thanks for contacting us, we will get back to you shortly."
	
	assert expected_message in success_text,f"Mismatch! Expected '{expected_message}',but got '{success_text}'"
	print (f"Validation Successful! Success message displayed:{success_text}'")
	
	finally:
	#close the browser
	driver.quit()
	
	
	
	
	
	
	