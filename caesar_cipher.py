alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text_enc, shift_enc):
  #creating empty str
  shifted_letters = ''
  #nested for loop that checks letters in text against letters/index of letters in alphabet
  for letter_index_text in range(0, len(text)):
    for letter_index in range(0, len(alphabet)):
      if alphabet[letter_index] == text[letter_index_text]:
        #if statement to go in reverse direction if adding shift goes outside of alphabet length
        if (letter_index + shift) > (len(alphabet) - 1):
          shifted_letters += alphabet[letter_index + shift - 26]
        else:
          shifted_letters += alphabet[letter_index + shift]

#Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.           
  print(f"Cipher text: {shifted_letters}")

#Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
  #TInside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
def decrypt(text_dec, shift_dec):
  #creating new empty str
  decrypt_letters = ''
  #for loop that does opposite of encrypt
  for letter_index_text in range(0, len(text)):
    for letter_index in range(0, len(alphabet)):
      if alphabet[letter_index] == text[letter_index_text]:
        if (letter_index - shift) < 0:
          decrypt_letters += alphabet[letter_index - shift + 26]
        else:
          decrypt_letters += alphabet[letter_index - shift]
  print(f"Decoded text: {decrypt_letters}")

#Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction.lower() == "encode":
  encrypt(text_enc = text, shift_enc = shift)
elif direction.lower() == "decode":
  decrypt(text_dec = text, shift_dec = shift)
else:
  print("Please enter a valid direction.")

