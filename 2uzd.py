#making safe password.
import string
import secrets

def make_pas(lenght=65536):
    # define letters
    abcd=string.ascii_letters+string.digits+string.punctuation
    password=''.join(secrets.choice(abcd) for i in range(lenght))
    return password
# call func and show password

password=make_pas(65536) # what is 20?
print(f"Good password is: {password}")  