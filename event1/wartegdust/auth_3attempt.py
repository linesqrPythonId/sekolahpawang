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
	with open(name_file, 'r') as output:
		data = output.read()
	return data

# write_file(file, 'ya\tyayaya\n')
print(read_file(file))
# counter_ve = 0
# counter_atmpt = 0
# while True:
# 	print("======================")
# 	print("1.Login")
# 	print("2.Register")
# 	print("3.Keluar")
# 	print("======================")
# 	try:
# 		pilih = int(input('pilihan : '))
# 		if pilih == 1:
# 			name = data
# 	except ValueError:
# 		counter_atmpt+=1
# 		if counter_atmpt <3:
# 			break
# 		message = 'PERHATIKAN INPUTAN ANDA, Sisa {}'.format(3 - counter_ve)
# 		pilih = int(input(message))