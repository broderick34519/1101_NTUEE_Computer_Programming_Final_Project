def main(now_time):
	card_ID = ''
	filename = 'nfc_output.txt'
	with open(filename,'a') as f:
		f.write(now_time)
	with open(filename,'r') as f:
		file_str = f.readlines()
		print('Card ID (Hex): ' + file_str[5][21:].replace('\n',''))
		card_ID = file_str[5][21:].replace('\n','').replace('  ','')
	with open('card_ID.txt','w') as ff:
		ff.write(card_ID)
