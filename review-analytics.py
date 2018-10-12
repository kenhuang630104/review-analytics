
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
		    print(len(data))

sum_len = 0
for d in data:
	sum_len += len(d)
print('the average string lengh is', sum_len/len(data), 'charactor')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有', len(new), '長度小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('總共有', len(good), '筆有good的留言')

bad = []
for d in data:
	if 'bad' in d:
		bad.append(d)
print('總共有', len(bad), '筆有bad的留言')
print('good佔', (len(good)/len(data))*100, '%')
print('bad佔', (len(bad)/len(data))*100, '%')