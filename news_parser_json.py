import json
import codecs
import chardet

def code_detecter(path_to_file_text):
	with open(path_to_file_text, 'rb') as source: # бинарное чтение
		lines = source.read()
		result = chardet.detect(lines)
		if result['encoding'] is None:
			raise Exception("Неизвестная кодировка файла!")
		else:	
			return result['encoding']

def get_text_list(file, encoding):
	with codecs.open(file, encoding = encoding) as news:
		data = json.load(news)
		text = ''
		for element in data['rss']['channel']['item']:
			text += ' ' + element['description']['__cdata']
		return text.split(' ')

def get_large_words_dict(text_list):
	text_set = set(text_list)
	large_words_dict = {}
	for word in text_set:
		if len(word) >= 6:
			counter = text_list.count(word)
			if counter in large_words_dict:
				large_words_dict[counter].append(word)
			else:
				large_words_dict[counter] = [word]
	return large_words_dict

def print_n_words(words_dict, n, direction):
	print(direction)
	entries = list(words_dict.keys())
	entries.sort(reverse = True)
	counter = 0
	for number in entries:
		for word in words_dict[number]:
			print(word, number)
			counter += 1
			if counter == n:
				return

files = {'Africa': 'newsafr.json',
		'Cyprus': 'newscy.json',
		'France': 'newsfr.json',
		'Italy': 'newsit.json'}

for file in files:
	encoding = code_detecter(files[file])
	text_list = get_text_list(files[file], encoding)
	large_words_dict = get_large_words_dict(text_list)
	print_n_words(large_words_dict, 6, file)
	print()







#encoding = code_detecter('newsfr.json')

# with codecs.open('newsfr.json', encoding = encoding) as news:
# 	data = json.load(news)
# 	text = ''
# 	for element in data['rss']['channel']['item']:
# 		text += ' ' + element['description']['__cdata']
#large_words_dict = get_large_words_dict(text_list)
	# for word in text_set:
	# 	if len(word) >= 6:
	# 		counter = text_list.count(word)
	# 		if counter in large_words_dict:
	# 			large_words_dict[counter].append(word)
	# 		else:
	# 			large_words_dict[counter] = [word]
#print_n_words(large_words_dict, 6)






	# print(type(data))
	# print(type(data['rss']['channel']))
	# mas = data['rss']['channel'].get('item')
	# print(mas)
	# print(type(mas))
	# print(len(mas))
	# print(mas[0])
	# print(type(mas[0]))
	# print(mas[0].keys())
	# print(mas[0]['description'])
	# print(type(mas[0]['description']))
	# print(mas[0]['description'].keys())
	# print(type(mas[0]['description']['__cdata']))


	# for element in data['rss']['channel'].items():
	# 	if element == 'item':
	# 		print(element)
	# 		print(type(element))
	# 		print()
	# print(len(data['rss']['channel'])) 
	
	# for elem in data['rss']['channel']:
		
	# 	print(elem)
	# 	print(type(elem))
	# 	print()