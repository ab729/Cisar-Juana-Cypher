alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

code = [2, 8, 14, 9, 8]

def encryption():

    msg = input("Enter your message:- ")
    arr = []
    encrypted_msg = []
    for ch in msg:
        arr.append(ch)

    # print(arr)

    if len(code) < len(arr):
        for n in range(len(arr)):
            code.append(code[n])

    # print(code)
    counter = 0
    for num in range(len(arr)):
        if arr[num] in alphabet :
            # print(arr[num])
            place = alphabet.index(arr[num])

            # print(f"the char {arr[num]} code is {alphabet[code[counter]+place]}")
            
            
            encrypted_msg.append(alphabet[code[counter]+place])
            counter = counter + 1
        else :
                encrypted_msg.append(' ')         




    return print(''.join(encrypted_msg))

def decryption():
    arr = []
    answer = []
    encrypted_msg = input("Enter the code you want to solve:- ")
    
    for ch in encrypted_msg:
         arr.append(ch)

    if len(code) < (len(arr)):
         for n in range(len(arr)):
              code.append(code[n])

    counter = 0
    for num in range(len(encrypted_msg)):
        if encrypted_msg[num] in alphabet:
              place = alphabet.index(encrypted_msg[num])
              answer.append(alphabet[place-code[counter]])
              counter = counter + 1
        else:
             answer.append(" ")
    return print("".join(answer))


choice = input("type 1 for encryption\nor 2 for decryption\nyour choice:-")
     
if choice == "1":
    encryption()
elif choice == '2':
    decryption()
else:
    print("Your input is not valid !!!")