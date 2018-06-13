def split_lines(folder):
	# 分裂文件成行
	# 每4个形成一个数组，每个数组形成一个大数组
	lines = open(folder,'r',encoding='utf-8').readlines()
	sum_ = list()
	count = 0
	for i in lines:
		count += 1
		if count%4 == 0:
			sub4 = lines[count-4:count]
			sum_.append(sub4)
	return sum_

if __name__ == '__main__':
	parent = r'F:\downloads\htm school\\'
	chs = parent + '[DownSub.com] HTM Overview (Episode 0).srt'
	eng = parent + '[DownSub.com] HTM Overview (Episode 0) eng.srt'
	new_ = parent + '0.srt'
	chs_list = split_lines(chs)
	eng_list = split_lines(eng)

	# chs 提小数组012放3
	# eng 提小数组23放3
	# 重复写入新合并文件
	with open(new_,'w+',encoding='utf-8') as nf:
		for chs,eng in zip(chs_list,eng_list):
			nf.write(  ''.join(i for i in chs[0:3]+eng[2:4])  )
