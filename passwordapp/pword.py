from main import num_only, letters_only, mixed

print("Welcome to CipherMaster\n")

ptype = input("""enter n, for numeric passkey, l for alpha-based passkey, and M for mixed passkey\n""").lower()

plength = int(input("Enter password length\n"))

opt_dict = {'n':num_only, 'l':letters_only,'m':mixed}

password = opt_dict.get(ptype)(plength)
password = "".join(str(i) for i in password)
print(password)
