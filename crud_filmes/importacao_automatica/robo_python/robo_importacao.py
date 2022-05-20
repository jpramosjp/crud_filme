from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get('https://www.adorocinema.com/filmes-todos/')

time.sleep(15)
#sim = driver.find_element_by_class_name('header-main').click()
tabelaFilmes = driver.find_element_by_xpath('//*[@id="content-layout"]/section[3]/div[2]/ul')
listasFilmes = tabelaFilmes.find_elements_by_class_name('mdl')

# print(len(teste3))
# print(teste3[-1].find_element_by_class_name('synopsis').find_element_by_class_name('content-txt').get_attribute('innerHTML'))
