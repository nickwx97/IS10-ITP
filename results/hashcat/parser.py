import re

name = "hashcat"

for i in range(1,11):
	file = open(f'{name}-{i}',mode='r')
	text = file.read()
	file.close()
	head_remove = re.compile(".*optimized-kernel-enable\n\n", re.DOTALL)
	tail_remove = re.compile("Started.*", re.DOTALL)
	text = head_remove.sub("",text)
	text = re.sub(r'Speed\.', '', text)
	text = re.sub(r'\.\.\.\.\.\.\.\.\.:\W*', ',', text)
	text = re.sub(r's \(.*', 's', text)
	text = tail_remove.sub("",text)
	file = open(f'{name}-{i}.csv',mode='w')
	file.write(text)
	file.close()
	print(f"#{name}-{i}")
