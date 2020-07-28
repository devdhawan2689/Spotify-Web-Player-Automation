from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.common.action_chains import ActionChains

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.get('https://www.spotify.com/in/')

assign_login_button1 = WebDriverWait(chrome_browser,30).until(
    E.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/header/div/nav/ul/li[6]/a'))
)

if assign_login_button1:
	print('Log In Button 1 Found')
else:
	print('Log In Button 1 Not Found')

login_button1 = chrome_browser.find_element_by_xpath('/html/body/div[2]/div/header/div/nav/ul/li[6]/a')
login_button1.click()


assign_username = WebDriverWait(chrome_browser,30).until(
    E.visibility_of_element_located((By.XPATH, '//*[@id="login-username"]'))
)

if assign_username:
	print('Username Found')
else:
	print('Username Not Found')

username = chrome_browser.find_element_by_xpath('//*[@id="login-username"]')
username.click()
username.send_keys('(Enter your Username)')



assign_password = WebDriverWait(chrome_browser,30).until(
    E.visibility_of_element_located((By.XPATH, '//*[@id="login-password"]'))
)

if assign_password:
	print('Password Found')
else:
	print('Password Not Found')

password = chrome_browser.find_element_by_xpath('//*[@id="login-password"]')
password.click()
password.send_keys('(Enter Your Password)')


assign_login_button2 = WebDriverWait(chrome_browser,30).until(
    E.visibility_of_element_located((By.XPATH, '//*[@id="login-button"]'))
)

if assign_login_button2:
	print('Log In Button 2 Found')
else:
	print('Log In Button 2 Not Found')

login_button2 = chrome_browser.find_element_by_xpath('//*[@id="login-button"]')
login_button2.click()


assign_home = WebDriverWait(chrome_browser,30).until(
    E.visibility_of_element_located((By.XPATH,'//*[@id="mh-footer"]/nav/div[2]/dl[3]/dd[2]/a'))
)

if assign_home:
	print('Home  Found')
else:
	print('Home  Not Found')

home = chrome_browser.find_element_by_xpath('//*[@id="mh-footer"]/nav/div[2]/dl[3]/dd[2]/a')
home.click()


while True:
	assign_search = WebDriverWait(chrome_browser,30).until(E.visibility_of_element_located((By.XPATH,'//*[@id="main"]/div/div[2]/div[2]/nav/ul/li[2]/a')))

	if assign_search:
		print('Home  Found')
	else:
		print('Home  Not Found')

	search = chrome_browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/nav/ul/li[2]/a')
	search.click()

	search_music = input('Enter the name of the song:- ')

	assign_search_field = WebDriverWait(chrome_browser,30).until(E.visibility_of_element_located((By.XPATH,'//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input')))

	if assign_search_field:
		print('Search Field Found')
	else:
		print('Search Field Not Found')

	search_field = chrome_browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[3]/div/div/input')
	search_field.click()
	search_field.clear()
	search_field.send_keys(search_music)

	assign_play_music = WebDriverWait(chrome_browser,30).until(E.visibility_of_element_located((By.XPATH,'//*[@id="searchPage"]/div/div/section[2]/div/div[2]/div[1]/div/div/div[3]/a/span')))

	if assign_play_music:
		print('Play Button Found')
	else:
		print('Play Button Not Found')


	actionchains = ActionChains(chrome_browser)

	play_music = chrome_browser.find_element_by_xpath('//*[@id="searchPage"]/div/div/section[2]/div/div[2]/div[1]/div/div/div[3]/a/span')
	actionchains.move_to_element(play_music)
	actionchains.context_click(play_music)
	actionchains.perform()


	assign_queue_mus = WebDriverWait(chrome_browser,30).until(E.visibility_of_element_located((By.XPATH,'//*[@id="main"]/div/nav[1]/div[3]')))

	if assign_queue_mus:
		print('Queue Button Found')
	else:
		print('Queue Button Not Found')

	queue_music = chrome_browser.find_element_by_xpath('//*[@id="main"]/div/nav[1]/div[3]')
	queue_music.click()





























