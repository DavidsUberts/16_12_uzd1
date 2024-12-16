def cezars(text, shift, mode="encrypt"):


    if mode=='decrypt':
        shift=shift
    result=''

    for char in text:
        if char.isalpha():
            start=ord('A') if char.isupper else ord('a')
            new_letter=chr((ord(char)-start+shift)%26+start)
            result+=new_letter
        else:
            result+=char
    return result

#example
org_text="Hello world!"
step=3

#shifting
shifting=cezars(org_text, step, mode="encrypt")
print("Bye World!", shifting)


#unshifting
unshifting=cezars(org_text, step, mode="decrypt")
print("Bye World!", unshifting)
