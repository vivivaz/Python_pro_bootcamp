alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text, shift, direction):
    text = list(text)
    message = []
    for i in text:
        n = 0
        for j in alphabet:
            if j == i:
                break
            n += 1
        if direction == "encode":
            message += alphabet[(n + shift) % len(alphabet)]
        elif direction == "decode":
            message += alphabet[(n - shift) % len(alphabet)]
    message = ''.join(message)
    print(f"The {direction}d text is {message}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text, shift, direction)
