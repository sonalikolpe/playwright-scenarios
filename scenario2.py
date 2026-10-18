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
	
	#Click on "Drag and drop "
	drag_drop_link = wait.until(EC.element_to_be_clickable((By.LINK_text,"Drag & Drop Sliders"))
	drag_drop_link.click()
	
	#2. Select the slider "Default value 15" and drag the bar to make it 95
	# Locate the range input slider starting with 15
	slider =wait.until(EC.presence_of_element_located((By.XPATH,"//input[@value='15']")))
	
	#set the value to 95
	driver.execute_script("arguments[0].value='95';arguments[0].dispatchEvent(new Event('input'));",slider)
	
	
	#validations for range value
	#Locate the output element displaying the range value
	output_elem = wait.until(EC.presence_of_element_located((BY.XPATH,"//input[@value='95']/following-sibling::output | //output[@id='range']")))
	
	#Verify the value 
	final_value =slider.get_attribute("Value")
	displayed_text = output_elem.text
	
	assert final_value =="95" or displayed_text =="95", f"validations failed! Slider value is {final_value},displayed text is {displayed_text}"
	print (f"Validation Successful! The range value correctly shows:'{displayed_text or final_value}'")
	
	Finally:
		# close the browser
		driver.quit()