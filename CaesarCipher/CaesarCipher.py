alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(plain_text,shift_amount,direction_new):
  de_cipher_text=""
  for letter in plain_text:
    position = alphabet.index(letter)
    if direction_new=="encode":
       new_position = position + shift_amount
    elif direction_new=="decode":
      new_position = position - shift_amount
    de_cipher_text += alphabet[new_position]
  print(f"The {direction_new}ed text is {de_cipher_text} ")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(plain_text=text,shift_amount=shift,direction_new=direction)