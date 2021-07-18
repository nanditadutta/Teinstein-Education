def machine():
    keys ="abcdefghijklmnopqrstuvwxyz !"
    values = keys[-1] + keys[0:-1]
    encryptDict = dict(zip(keys,values))
    decryptDict = dict(zip(values,keys))

    message = input("Please enter the secert message  ")
    mode = input("Please enter the mode: Encode(E) OR Decode(D)  ")

    if mode.upper()  =='E': #If the user entered the small e it will be converted to uppercase E and operate the program further.
        newMessage = ''.join([encryptDict[letter] for letter in message.lower()])# for fetching key and its values respectively.
    elif mode.upper()== 'D':
        newMessage = ''.join([decryptDict[letter] for letter in message.lower()])
    else:
        print("please enter a correct choice")

    return newMessage.capitalize()


print(machine())        