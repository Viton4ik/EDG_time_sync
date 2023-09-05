from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import datetime

# Time synchronization script
while True:
    # Browser initialization in the background
    driver_options = Options()
    driver_options.add_argument("--headless") 

    # Use Edge (or Chrome if needed)
    # driver = webdriver.Edge(options=driver_options) 
    driver = webdriver.Edge() 

    # Open the PLC control panel
    Number_edg = [1, 2]
    for edg_N in Number_edg:
        driver.get(f"http://10.200.37.43/c{edg_N}/control.htm")

        # Find the field with the password and set it
        password_field = driver.find_element(By.ID, "psw_id")
        password_field.clear()
        password_field.send_keys(0)

        # Push the access button
        password_accept = driver.find_element(By.CLASS_NAME, "w_bok")
        password_accept.click()
        # Delay in 2 sec
        time.sleep(2)  

        # Go to the page with the time options
        driver.get(f"http://10.200.37.43/c{edg_N}/WRPAR_E.HTM?ws=300&wd=16&wl=0&wh=65535")
        # Delay in 1 sec
        time.sleep(1)  

        # Find the time field and clear it
        time_input = driver.find_element(By.CLASS_NAME, "w_vi")
        time_input.clear()

        # Take the system time with an appropriate format and put it down
        current_time = datetime.datetime.now().time()
        formatted_time = current_time.strftime("%H:%M:%S")  
        time_input.send_keys(formatted_time)

        # Push the access button
        button_accept = driver.find_element(By.CLASS_NAME, "w_bok")
        button_accept.click()

        # Delay in 1 sec
        time.sleep(1)  

    # Find close button and press it
    close_button = driver.find_element(By.CLASS_NAME, "tb_exa")
    driver.get(close_button.get_attribute("href"))
    # Delay in 2 sec
    time.sleep(2)  

    # Close the connection
    driver.quit()

    # Wait for half a day and repeat
    # time.sleep(43200)  
    time.sleep(20)  

    #pythonw.exe appW.pyw
    #TASKKILL /F /IM pythonw.exe
