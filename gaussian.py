import numpy as np

salmon_data = []
def extract_data_salmon(filename): 
	infile = open(filename, 'r')
	for line in infile:
		line = line.replace('\n', '')
		length = line.split(' ')
		for l in length:
			try:
				l = float(l)
				if isinstance(l, float) and l > 0 and l < 100:
					salmon_data.append(l)
			except:
				pass
	return np.mean(salmon_data), np.std(salmon_data)

bass_data = []
def extract_data_bass(filename): 
	infile = open(filename, 'r')
	for line in infile:
		line = line.replace('\n', '')
		length = line.split(',')
		for l in length:
			try:
				l = float(l)
				if isinstance(l, float) and l > 0 and l < 100:
					bass_data.append(l)
			except:
				pass
	return np.mean(bass_data), np.std(bass_data)

trout_data = []
def extract_data_trout(filename): 
	infile = open(filename, 'r')
	for line in infile:
		line = line.replace('\n', '')
		length = line.split(' ')
		for l in length:
			try:
				l = float(l)
				if isinstance(l, float) and l > 0 and l < 100:
					trout_data.append(l)
			except:
				pass
	return np.mean(trout_data), np.std(trout_data)

mean1, std1 = extract_data_salmon('Atlantic_salmon.txt') 
mean2, std2 = extract_data_bass('Largemouth_bass.txt') 
mean3, std3 = extract_data_trout('Rainbow_trout.txt') 
print(mean1, std1) 
print(mean2, std2) 
print(mean3, std3)
# write your code here to generate/write a new file named 'result.txt'
with open('result.txt', 'w') as f:
    f.write(f'Mean and standard deviation of Gaussian of Atlantic salmon are {mean1} and {std1}\n')
    f.write(f'Mean and standard deviation of Gaussian of Largemouth bass are {mean2} and {std2}\n')
    f.write(f'Mean and standard deviation of Gaussian of Rainbow trout are {mean3} and {std3}\n')