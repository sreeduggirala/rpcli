from selenium import webdriver

# Launches the browser
driver = webdriver.Chrome()

# Opens the website
driver.get("https://chainlist.org/")

# Finds the chain names, IDs, and RPC URLs

# Organizes chain names, IDs, and RPC URLs into dataframes

# Closes the browser
driver.quit()
