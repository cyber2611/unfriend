#!/usr/bin/python
# coding=utf-8
# silakhan recode aja
# author : DulLah

import os,sys,time,json,hashlib
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.exceptions import ConnectionError

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\033[1;97m[!] Keluar"
	os.sys.exit()

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
logo ="""  \x1b[1;93m_   _       _____    _                _ \n \x1b[1;94m| | | |_ __ | ___| __(_) ___ _ __   __| | \n \x1b[1;95m| | | | '_ \| |_| '__| |/ _ \ '_ \ / _` | \n \x1b[1;96m| |_| | | | | _|| |  | | __ / | | | (_| | \n  \x1b[1;91m\___/|_| |_|_| |_|  |_|\___|_| |_|\__,_|\n"""
	
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[●] Tunggu sebentar "+o),;sys.stdout.flush();time.sleep(1)
		

def ambil_token():
	os.system('clear')
	print('\x1b[1;97m[!] Login akun FB untuk mengambil token\n')
	id = raw_input('\x1b[1;97m[+] Email/ID : ')
	pwd = raw_input('\x1b[1;97m[+] Password : ')
	tik()
	try:
		br.open('https://m.facebook.com')
	except mechanize.URLError:
		print"\n\033[1;97m[!] Tidak ada koneksi"
		keluar()
	br._factory.is_html = True
	br.select_form(nr=0)
	br.form['email'] = id
	br.form['pass'] = pwd
	br.submit()
	url = br.geturl()
	if 'save-device' in url:
		try:
			sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
			data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
			x=hashlib.new("md5")
			x.update(sig)
			a=x.hexdigest()
			data.update({'sig':a})
			url = "https://api.facebook.com/restserver.php"
			r=requests.get(url,params=data)
			z=json.loads(r.text)
			print '\n\x1b[1;97m[✓] Token berhasil terambil'
			time.sleep(2)
			os.system('clear')
			print("\x1b[1;93mToken anda adalah \x1b[1;91m: \n\n\x1b[1;92m" +z['access_token'])
			print("\n\x1b[1;96m[!] \x1b[1;97mSilahkan copy token anda")
			raw_input("\n\x1b[1;97mKlik enter untuk melanjutkan")
			hapus_teman_jancuk()
		except requests.exceptions.ConnectionError:
			print"\n\033[1;97m[!] Tidak ada koneksi"
			time.sleep(1)
			keluar()
	if 'checkpoint' in url:
		print("\n\033[1;97m[!] Akun cekpoint")
		time.sleep(1)
		keluar()
	else:
		print("\n\033[1;97m[!] gagal")
		time.sleep(1)
		ambil_token()
	

def hapus_teman_jancuk():
	os.system('clear')
	print logo
	print('\x1b[1;97mAuthor \x1b[1;91m: \x1b[1;96mDulLah \n\x1b[1;97mGitHub \x1b[1;91m: \x1b[1;92mhttps://github.com/unikers71 \n\x1b[1;97mFB     \x1b[1;91m: \x1b[1;92mhttps://fb.me/un1ker5\n')
	print 43*"\033[1;96m="
	print('\x1b[1;91mNOTE \x1b[1;97mjika akun logout sendiri \nmungkin proses akan tetap berjalan \ntetapi teman tidak terhapus')
	print 43*"\033[1;96m="
	token = raw_input('\x1b[1;93mMasukan token anda \x1b[1;91m: \x1b[1;92m')
	print 43*"\033[1;96m="
	jalan('\033[1;96m[✺] \033[1;93mMulai \033[1;97m...')
	print "\033[1;96m[!] \x1b[1;93mStop \033[1;92mCTRL+C"
	print 43*"\033[1;96m=\x1b[1;97m"
	try:
		gasmank = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		oketod = json.loads(gasmank.text)
		for i in oketod['data']:
			nama = i['name']
			id = i['id']
			requests.delete("https://graph.facebook.com/me/friends?uid="+id+"&access_token="+token)
			print "\033[1;96m[\033[1;92mTerhapus\033[1;96m] \x1b[1;97m"+nama
	except KeyError:
			print"\033[1;96m[!] \x1b[1;91mToken invalid \ncoba ambil ulang token anda"
			time.sleep(1)
			y_n()
	except IndexError: pass
	except KeyboardInterrupt:
		print "\n\033[1;96m[!] \x1b[1;91mTerhenti"
		time.sleep(1)
		keluar()
	except ConnectionError:
		print "\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
		time.sleep(1)
		keluar()
	print"\n\033[1;96m[+] \033[1;92mSelesai"
	time.sleep(1)
	keluar()

def y_n():
	njer = raw_input("\x1b[1;97mApakah anda ingin mengambil token lagi \x1b[1;96m(\x1b[1;97my/t\x1b[1;96m) \x1b[1;91m:\x1b[1;97m ")
	if njer =="":
		print('\x1b[1;96m[!] \x1b[1;91mInput yang benar')
		time.sleep(1)
		y_n()
	elif njer =="y":
		ambil_token()
	elif njer =="t":
		keluar()
	else:
		print('\x1b[1;96m[!] \x1b[1;91mInput yang benar')
		time.sleep(1)
		y_n()
		
if __name__ == "__main__":
	ambil_token()
