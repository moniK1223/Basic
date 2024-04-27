'''
selenium :
To install selenium --> Go to command prompt --> pip install selenium
The above command will install the latest version of selenium

If we want to install the specific version of selenium, we give
    pip install selenium==version


pip list --> This will give the list of all the installed packages
'''
import time

# ## launching chrome browser
# from selenium import webdriver
# chrome_driver = webdriver.Chrome()
#
# #----------------------------------------------------------
# ## launch firefox browser
#
# from selenium import webdriver
# firefox_object = webdriver.Firefox()
#
# #-------------------------------------------------------
# ## launching Edge
#
# from selenium import webdriver
# edge_driver = webdriver.Edge()

#----------------------------------------------------------------------------
# from selenium import webdriver
# driver = webdriver.Chrome()
#
# ## The above code will automatically close the browser
#----------------------------------------------------------------------------

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# ## This commands prevents the browser from automatically closing

#---------------------------------------------------------------------------

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

## to launch the webpage
## get() : To launch the url
## SYNTAX : driver.get('url')

driver.get('https://www.flipkart.com/')
time.sleep(2)

## To maximize
driver.maximize_window()
time.sleep(2)

# driver.minimize_window()

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(2)

print(driver.current_url)
print(driver.title)
print(driver.name)

## current_url is a property. This will print the url we are launching
## title is a property, this will print the title of the application we are launching
## name is a property. This will give the browser name

driver.close()
























































