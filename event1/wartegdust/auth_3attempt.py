"""
	code for auth attempt
	by
	warteg dust
"""
file = 'hai.txt'

def write_file(name_file, content):
	with open(name_file, 'a') as output:
		output.write(content)

def read_file(name_file):
	data = ''
	uname = []
	passwd = []
	with open(name_file, 'r') as output:
		data = output.read()
	split_data =  [item.split(';') for item in data.split()]
	uname = [un for un,_,_ in split_data]
	passwd = [pwd for _,pwd,_ in split_data]
	role = [role for _,_,role in split_data]
	return uname, passwd, role

counter_ve = 0
counter_atmpt = 0

while True:
	print("======================")
	print("1.Login")
	print("2.Register")
	print("3.Keluar")
	print("======================")
	try:
		pilih = int(input('pilihan : '))
		if pilih == 1:
			data = read_file(file)
			name = input('name \t\t:')
			passwd = input('password \t:')
			if name in data[0]:
				print(name)
				u_idx = data[0].index(name)
				if passwd == data[1][u_idx]:
					print("role anda {}".format(data[2][u_idx]))
					lanjut = input('lanjut (y) ?').lower()
					counter_ve = 0
					counter_atmpt = 0
					if lanjut != 'y':
						break
					else:
						continue
			else:
				counter_atmpt+=1
				if counter_atmpt <4:
					print('Maaf tidak terdaftar')
					continue
				break

		elif pilih ==2:
			name = input('name \t\t:')
			passwd = input('password \t:')
			role = input('role \t\t:')
			content = name+';'+passwd+';'+role+'\n'
			write_file(file,content)
			print('SUCCESS')
			continue
		if pilih ==3:
			print("TERIMAKASIH")
			break
		
		else:
			counter_ve+=1
			if counter_ve >3:
				break
			message = 'PERHATIKAN INPUTAN ANDA, Sisa {}'.format(4 - counter_ve)
			print(message)
			continue

	except ValueError:
		counter_ve+=1
		if counter_ve >3:
			break
		message = 'PERHATIKAN INPUTAN ANDA, Sisa {}'.format(4 - counter_ve)
		print(message)
		continue