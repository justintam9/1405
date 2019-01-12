# ============================================================
#
# Student Name (as it appears on cuLearn): Justin Tam 
# Student ID (9 digits in angle brackets): <101078802>
# Course Code (for this current semester): COMP1405A
#
# ============================================================
'''
This function will load a text file.

@params		file_name, the name of the file to be loaded
@return		an uppercase string containing the data read from the file
'''
def load_text(file_name):
	file_hndl = open (file_name,"r")
	file_data = file_hndl.read()
	file_hndl.close()
	return file_data.upper()

'''
This function will save data to a text file.

@params		file_name, the name of the file to be saved
		file_ata, the data to be written to the file
@return		none
'''
def save_text(file_name,file_data):
	file_hndl = open(file_name,"w")
	file_hndl.write(file_data)
	file_hndl.close()
'''
This function will encode data given.

@params		string, the string to be encoded
		alphabet, the alphabet used to encode
@return		Encoded data
'''
def encode (string,encrypted_alphabet):
	#convert parameters into lists
	if (type(string) is list) == True:
		phrase = string
	else:
		phrase = list(string.upper())
	#validation if parameters are empty
	if encrypted_alphabet == "":
		print ("\n-------------------------------------------------------\n")
		print ("No alphabet to encode.")
		return string
	if string=="":
		print ("\n-------------------------------------------------------\n")
		print ("No string to decode.")
		return string
	temp_list = list ()
	modified_text = list ()
	alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	special_char = True
	#change letters to a corresponding number
	for i in phrase:
		for j in range (26):
			if i == alphabet[j]:
				temp_list.append(j)
				special_char = False
		if special_char == True:
			temp_list.append(i)
		special_char = True
	#convert number to corresponding encrypted letter
	for i in temp_list:
		for j in range (26):
			if i == j:
				modified_text.append(encrypted_alphabet[j])
				special_char = False
		if special_char == True:
			modified_text.append(i)
		special_char = True
	return modified_text
'''
This function will decode data given.

@params		string, the string to be decoded
		alphabet, the alphabet used to decode
@return		Decoded data
'''
def decode (string,decrypted_alphabet):
	#convert parameters into lists
	if (type(string) is list) == True:
		phrase = string
	else:
		phrase = list(string.upper())
	#validation if parameters are empty
	if decrypted_alphabet == "":
		print ("\n-------------------------------------------------------\n")
		print ("No alphabet to encode.")
		return string
	if string=="":
		print ("\n-------------------------------------------------------\n")
		print ("No string to encode.")
		return string
	temp_list = list ()
	modified_text = list ()
	alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	special_char = False
	#convert letters to corresponding numbers
	for i in phrase:
		for j in range (26):
			if i == decrypted_alphabet[j]:
				temp_list.append(j)
				special_char = True
		if special_char == False:
			temp_list.append(i)
		special_char = False
	#convert numbers to corresponding decrypted letter
	for i in temp_list:
		for j in range (26):
			if i == j:
				modified_text.append(alphabet[j])
				special_char = True
		if special_char == False:
			modified_text.append(i)
		special_char = False
	return modified_text

'''
This function will cipher alphabet data given.

@params		string, keyword used to create a new alphabet
@return		alphabet, the alphabet used to encode

'''
def keyboard_cipher_alphabet (string):
	word = list(string.upper())
	modified_alphabet = list()
	alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	#check for duplicates in given string
	for i in word:
		if i not in modified_alphabet:
			modified_alphabet.append (i)
	#remove string from the alphabet
	for i in modified_alphabet:
		if i in alphabet:
			alphabet.remove(i)
	#add string and remaining alphabet together
	for i in alphabet:
		modified_alphabet.append(i)
	return modified_alphabet

'''
This function will cryptogram alphabet data given.

@params		none
@return		string, alphabet

'''
def cryptogram_alphabet ():
	alphabet = list(input("Enter an alphabet of 26 characters : ").upper())
	modified_alphabet = list()
	#check length
	if len(alphabet) ==26:
		#check for duplicates
		for i in alphabet:
			if i not in modified_alphabet:
				modified_alphabet.append (i)
		#length didnt change
		if len(modified_alphabet) == 26:
			return modified_alphabet
		
	#error message
	print ("\n-------------------------------------------------------\n")
	print ("Error. Contains duplicates or not enough characters.")
	return (list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

'''
This function will cryptogram alphabet data given.

@params		integer, number to shift the alphabet
@return		string, shifted alphabet

'''
def caesar_cipher_alphabet (num):
	alphabet = list ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	modified_alphabet = list()
	#validation
	if num >26:
		print ("\n-------------------------------------------------------\n")
		print ("Choose a number less than 26.")
		return ("")
	#save alphabet past given argument
	for i in range (num,len(alphabet)):
		modified_alphabet.append(alphabet[i])
	#save rest of alphabet
	for i in range (num):
		modified_alphabet.append(alphabet[i])
	return modified_alphabet
'''
This is the main function, responsible for the user interface.

@params		none
@return		none
'''
def main():
	initial = "None"
	current = "None"
	alphabet = ""
	filename = "None"
	data = list()
	
	while True:
		#making  current text readable
		current_string = ""
		for i in current:
  			current_string += i
		#instructions
		print ("\n-------------------------------------------------------\n")
		print ("File currently loaded : ",filename)
		print ("\nInitial Text : ", initial)
		print ("Current Text : ", current_string)
		print ("\nEnter the number corresponding with the function you would like to use.\n")
		menu = input("1. Load \n2. Save \n3. Encode \n4. Decode \n5. Caesar Ciper Alphabet \n6. Cryptogram Alphabet \n7. Keyboard Cipher Alphabet \n8. Quit \n \nEnter an option. (1-8) : ")
		#check if number
		if menu == "1" or menu == "2" or menu == "3" or menu == "4" or menu == "5" or menu == "6" or menu == "7" or menu == "8":
			menu = int(menu)
			#load
			if menu == 1:
				filename = input ("Name of the file you wish to load? ")
				data =load_text(filename)
				initial = data
				current = initial
			#save
			elif menu == 2:
				filename = input ("Name of the file you wish to save to? ")
				save_text(filename,current_string)
			#encode
			elif menu == 3:
				current = encode (current,alphabet)
			#decode
			elif menu == 4:
				current = decode (current,alphabet)
			#caesar
			elif menu == 5:
				alphabet = caesar_cipher_alphabet(int(input("Enter number to shift: ")))
			#cryptogram
			elif menu == 6:
				alphabet = cryptogram_alphabet()
			#cipher
			elif menu == 7:
				alphabet = keyboard_cipher_alphabet (input ("Enter string to shift: "))
			#quit
			elif menu == 8:
				break
		#error message
		else:
			print ("\n-------------------------------------------------------\n")
			print ("Error, enter a number from the menu.")
		
main()
