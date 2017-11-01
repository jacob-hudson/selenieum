from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image

driver = webdriver.PhantomJS()
driver.get('http://stackoverflow.com/')

element = driver.find_element(By.XPATH, '/html/body/header/div/div[1]/a/span')
location = element.location
size = element.size
driver.save_screenshot('screenshot.png')
driver.quit()

im = Image.open('screenshot.png') # uses PIL library to open image in memory

left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']


im = im.crop((left, top, right, bottom)) # defines crop points
im.save('screenshot.png') # saves new cropped image
