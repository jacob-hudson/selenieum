#!/usr/bin/env python

from selenium import webdriver

driver = webdriver.PhantomJS()
dx, dy = driver.execute_script("var w=window; return [w.outerWidth - w.innerWidth, w.outerHeight - w.innerHeight];")
driver.set_window_size(1920 + dx, 1080 + dy)
driver.get('https://splunk.com/')
driver.save_screenshot('screen_viewport.png')
