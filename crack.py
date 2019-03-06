from sys import argv
import string
import crypt

hash = argv[1]

# remove username from string
colon_index = hash.find(":")
salt = hash[colon_index + 1:colon_index + 3]
hash_nosalt = hash[colon_index + 3:]

# list of uppercase and lowercase english letter alphabet
lowercase_dict = list(string.ascii_lowercase)
uppercase_dict = list(string.ascii_uppercase)

# the final string with numbers, etc... removed
final_hash = ""

for char in hash_nosalt:
    if char not in lowercase_dict and char not in uppercase_dict:
        continue
    else:
        final_hash = final_hash + char

for letter, position in enumerate(lowercase_dict, uppercase_dict):
    test1 = lowercase_dict[letter]
    if test1 == crypt.crypt(hash, salt):
        print("found!")
        break

    for letter in range(len(lowercase_dict)):
        test2 = test1 + lowercase_dict[letter]
        if test2 == crypt.crypt(hash, salt):
            print("found!")
            break

        for letter in range(len(lowercase_dict)):
            test3 = test2 + lowercase_dict[letter]
            if test3 == crypt.crypt(hash, salt):
                print("found!")
                break

            for letter in range(len(lowercase_dict)):
                test4 = test3 + lowercase_dict[letter]
                if test4 == crypt.crypt(hash, salt):
                    print("found!")
                    break

                for letter in range(len(lowercase_dict)):
                    test5 = test4 + lowercase_dict[letter]
                    if test5 == crypt.crypt(hash, salt):
                        print("found!")
                        break
