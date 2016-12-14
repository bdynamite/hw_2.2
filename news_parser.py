import xml.etree.ElementTree as ET
import codecs
import chardet

# функция возвращает кодировку текстового файла
def code_detecter(path_to_file_text): 
	with open(path_to_file_text, 'rb') as source: # бинарное чтение
		lines = source.read()
		result = chardet.detect(lines)
		if result['encoding'] is None:
			raise Exception("Неизвестная кодировка файла!")
		else:	
			return result['encoding']

# возвращает список всех слов всех новостей
def get_text_list(path, encoding): 
	file = codecs.open(path, mode = 'r', encoding = encoding)
	content_file = "".join([line for line in file.readlines()])
	root = ET.fromstring(content_file)
	text = "".join(element.text for element in root.iter(tag = 'description'))
	return text.split(' ')

# возвращает словарь вхождений слов, которые длиннее 6 символов
# ключ = число вхождений, зачение = список слов
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

# выводит n самых часто встречающихся слов
def print_n_words(words_dict, n, direction, exception):
	entries = list(words_dict.keys())
	entries.sort(reverse = True)
	counter = 0
	for number in entries:
		for word in words_dict[number]:
			if not(word in exceptions):
				print('{}) cлово "{}" встречается {} раз(а)'.format(counter + 1, word, number))
				counter += 1
				if counter == n:
					return

# получим список слов-исключений
def get_exceptions_list():
	file = open('exceptions.txt', 'r')
	content = file.read()
	file.close()
	return content.split()

files = {'Africa': 'newsafr.xml',
		'Cyprus': 'newscy.xml', #файлы кипра и франции абсолютно идентичны!
		'France': 'newsfr.xml',
		'Italy': 'newsit.xml'}

exceptions = get_exceptions_list()

for file in files:
	print(file)
	encoding = code_detecter(files[file])
	text_list = get_text_list(files[file], encoding)
	large_words_dict = get_large_words_dict(text_list)
	print_n_words(large_words_dict, 10, file, exceptions)
	print()












