
import random

#Function_1

def get_def_and_pop( word_list, word_dict):
	#this function will return the value by getting the key where key is the word and defination is a value
	random_index = random.randrange(len(word_list))
	#get indexes as the size of the word_list
	word = word_list.pop(random_index)
	#pop words from the list
	defination = word_dict.get(word)
	#get value by key random
	return word,defination
	#return tuple word and its defination


#function_2

def get_word_defination(rawstring):
    word, defination = rawstring.split(',', 1)   
    return word, defination 



fh = open("data.csv","r")
#for reading a file named data
wd_list = fh.readlines()


wd_set = set(wd_list)

fh = open("dataSet.csv", "w")
#ceating a file with no duplicates for dictionary
fh.writelines(wd_set)


#create dictionary

word_dict = dict()

for rawstring in wd_set:
    word, defination = get_word_defination(rawstring)

    word_dict[word] = defination
	#word is ket and defination is a function



while True:
	wd_list = list(word_dict)

	#will gave us list of keys
	choice_list = []

	#first of all we will create the empty choice_list
	for x in range(4):

		#we will create 4 choices

		word, defination = get_def_and_pop(wd_list, word_dict)
		choice_list.append(defination)

	#shuffle the choices
	random.shuffle(choice_list)
	print(word)

	#gave word and they will chose defination correct
	print("-------------")


	#print the choices using for each loop
	for idx, choice in enumerate(choice_list):
		print(idx+1, choice)
	#print index start with one and then choice

	choice = int(input("Enter 1,2,3,4; 0 to exit"))
	#get input from user

	if choice_list[choice-1] == defination:
		print("Correct!\n")
	elif choice == 0:
		exit(0)
	else:
		print("Incorrect You lose this\n")


