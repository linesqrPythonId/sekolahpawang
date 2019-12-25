"""
	program for grating based time at computer (local)
	by
	warteg dust
"""
import datetime

tanggal,jam = str(datetime.datetime.now()).split(' ')

ucapan = ['Selamat Pagi', 'Selamat Siang', 'Selamat Malam']
# <8 = 'pagi', 8<hour<16 = 'siang', '16-24' = 'malam'
get_ucapan_id = int(jam.split(':')[0])//8
print(ucapan[get_ucapan_id])
