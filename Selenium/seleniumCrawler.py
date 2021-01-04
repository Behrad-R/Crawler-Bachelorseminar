from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import pandas as pd
import re

binary = FirefoxBinary(*path to binary*)
driver = webdriver.Firefox(firefox_binary=binary)

starting_node = *dark web url*

found_nodes = []

p = re.compile('\S+onion')
for post in posts:
    nodes = p.findall(post)
    found_nodes.append(nodes)
