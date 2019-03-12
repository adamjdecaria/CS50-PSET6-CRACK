from sys import argv
import string
import crypt
import itertools

hash = argv[1]

# remove username from string
colon_index = hash.find(":")
#find the salt used as part of crypt.crypt
salt = hash[colon_index + 1:colon_index + 3]
#the hashed password including salt, to be used for comparison
hash_and_salt = hash[colon_index + 1:]

# list of uppercase and lowercase english letter alphabet
dictionary = list(string.ascii_lowercase) + list(string.ascii_uppercase)

# using itertools and itertools.combinations to create every possible letter combination
# check for success in finding password
for pwdCheck in range(0, len(dictionary)+1):
    for subset in itertools.combinations(dictionary, pwdCheck):
            pwdString = ''.join(subset)
            print(crypt.crypt(pwdString, salt))
            if crypt.crypt(pwdString, salt) == hash_and_salt:
                print("Found!")
                break
