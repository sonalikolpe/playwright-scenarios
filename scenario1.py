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
	simple_form_link = wait.until(EC.element_to_be_clickable((BY.LINK_TEXT,"Simple Form Demo"))
	
	#2. Click "simple form demo"
	Simple_form_link.click()
	
	#3. Validate that the url contains "simple form demo"	
	wait.until(EC.url_contains("Simple-form-demo")
	assert "simple-form-demo" in driver.current_url,f"URL  validation failed! Current URL:{driver.current_url}"
	print("URL validation passed: URL contains 'simple-form-demo'")
	
	
	#4. Create a variable for a string value
	message_text = "Welcome to TestMu AI"
	
	#5. Use this variable to enter values in the "Enter Message" text box
	# Locating the text box by its placeholde or id 
	enter_message_box = wait.until(EC.presence_of_element_located(BY.XPATH,"//input[@id='user-message']"))
	enter_message_box.clear()
	enter_message_box.send_keys(message_text)
	
	#6. Click "Get Checked values"
	#Locating the button by its id	
	get_checked_value_btn =wait.until(EC element_to_be_clickable((By.XPATH,"//button[@id='showInput']")))
	get_checked_value_btn.click()
	
	#7. validate for the same message displayed 
	displayed_message_elem= wait.until(EC.presence_of_element_located((BY.XPATH,"//p[@id='message']")))	
	displayed_text =displayed_message_elem.text
	
	assert displayed_text ==message_text,f"Mismatch! Expected '{message_text}',but got '{displayed_text}'"
	print (f"Validation Successful! The displayed message matches:'{displayed_text}'")
	
	Finally:
		# close the browser
		driver.quit()
	

	