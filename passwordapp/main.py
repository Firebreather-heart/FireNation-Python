import random, string

letters = [i for i in string.ascii_letters]

punct = [ i for i in (string.punctuation + string.whitespace) ]

nums = [i for i in range(10)]

#print(letters, nums, punct)

def num_only(length:int):
    """ this function will generatea random passkey containing numbers only
    params:
         length: an integer specifying the length of the password
         """
    if length > 10:
        return "Length must be less or equal to ten"
    else:
        pkey = random.sample(nums, length)
        return pkey

def letters_only(length:int):
    """return a random list of letters"""
    if length > 26:
        return "length must be less than kr equal to 26"
    else:
        pkey = random.sample(letters, length)
        return pkey

def mixed(length):
    """.........."""
    if length > 40:
      return "length must not be greater han 40"
    else:
        joint_ls = nums + letters + punct
        return random.sample(joint_ls, length)
