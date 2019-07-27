#!/usr/bin/python
# coding=utf-8
# silakhan recode aja
# author : DulLah

import os,sys,time,json
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.ex import ConnectionError

def keluar():
	print "\033[1;96m[!] \x1b[1;91mKeluar"
	os.sys.exit()

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
class utama:
	os.system('clear')
	print("""  \x1b[1;93m_   _       _____    _                _ \n \x1b[1;94m| | | |_ __ | ___| __(_) ___ _ __   __| | \n \x1b[1;95m| | | | '_ \| |_| '__| |/ _ \ '_ \ / _` | \n \x1b[1;96m| |_| | | | | _|| |  | | __ / | | | (_| | \n  \x1b[1;91m\___/|_| |_|_| |_|  |_|\___|_| |_|\__,_|\n""")
	print('\x1b[1;97mAuthor \x1b[1;91m: \x1b[1;96mDulLah \n\x1b[1;97mGitHub \x1b[1;91m: \x1b[1;92mhttps://github.com/unikers71 \n\x1b[1;97mFB     \x1b[1;91m: \x1b[1;92mhttps://fb.me/un1ker5\n')
	print('\x1b[1;96m[!] \x1b[1;97mAnda bisa mengambil token \ndi \x1b[1;92mhttp://botviet.net \x1b[1;97matau disitus lain')
	print 43*"\033[1;96m="
	token = raw_input('\x1b[1;93mMasukan TOKEN \x1b[1;91m: \x1b[1;92m')
	print 43*"\033[1;96m="
	jalan('\x1b[1;91mNOTE \x1b[1;97mjika akun logout sendiri \nmungkin proses akan tetap berjalan \ntetapi teman tidak terhapus')
	print 43*"\033[1;96m="
	jalan('\033[1;96m[✺] \033[1;93mMulai \033[1;97m...')
	print "\033[1;96m[!] \x1b[1;93mStop \033[1;92mCTRL+C"
	print 43*"\033[1;96m=\x1b[1;97m"
	try:
		pek = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		cok = json.loads(pek.text)
		for i in cok['data']:
			nama = i['name']
			id = i['id']
			requests.delete("https://graph.facebook.com/me/friends?uid="+id+"&access_token="+token)
			print "\033[1;96m[\033[1;92mTerhapus\033[1;96m] \x1b[1;97m"+nama
	except KeyError:
			print"\033[1;96m[!] \x1b[1;91mToken invalid \ncoba ambil ulang token anda"
			time.sleep(1)
			keluar()
	except IndexError: pass
	except KeyboardInterrupt:
		print "\n\033[1;96m[!] \x1b[1;91mTerhenti"
		keluar()
	except ConnectionError:
		print "\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
		time.sleep(1)
		keluar()
	print"\n\033[1;96m[+] \033[1;92mSelesai"
	time.sleep(1)
	keluar()
	
