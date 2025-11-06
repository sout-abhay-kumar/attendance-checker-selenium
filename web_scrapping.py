from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
from dotenv import load_dotenv
load_dotenv()

# Open Chrome and go to login page
driver = webdriver.Chrome()
driver.get('https://online.uktech.ac.in/ums/Student/Account/Login')

# Fill username/password
driver.find_element(By.ID, "LoginId").send_keys("ST0000043194")
driver.find_element(By.ID, "Password").send_keys(os.getenv("PASSWORD"))

print("Fields filled. Please solve CAPTCHA and press login manually.")
input("Press Enter here after logging in manually...")

# Wait until dashboard/menu is loaded
wait = WebDriverWait(driver, 30)
# Wait for any dashboard element to appear, adjust if needed
wait.until(EC.presence_of_element_located((By.ID, "navbarDropdown")))

#Hover over 'Report' menu
report_menu = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//a[contains(., 'Report')]"))
)
actions = ActionChains(driver)
actions.move_to_element(report_menu).perform()

# Click 'View Attendance' submenu
view_attendance = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/ums/Student/User/ViewAttendance']"))
)
view_attendance.click()

# Wait for Attendance page to load dropdowns
wait.until(EC.presence_of_element_located((By.ID, "SessionYear")))

#Fill dropdowns
Select(driver.find_element(By.ID, "SessionYear")).select_by_visible_text("2025-26")
Select(driver.find_element(By.ID, "CourseBranchDurationId")).select_by_visible_text("3 Semester")
Select(driver.find_element(By.ID, "Year")).select_by_visible_text("2025")
Select(driver.find_element(By.ID, "MonthId")).select_by_visible_text("September")

# Click the input button
view_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@value='View Attendance']"))
)
view_btn.click()

print("View Attendance clicked successfully!")

# Pause to let you check results before closing browser
input("Press Enter here to close the browser...")
driver.quit()
