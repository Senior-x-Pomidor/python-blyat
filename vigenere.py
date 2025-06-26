import hangman

crypt_key  = "pfandflaschenrueckgabegeraet"

alphabet = {chr(i + ord('a')): i for i in range(26)}
alphabet.update({
    'ä': 26,
    'ö': 27,
    'ü': 28
})
alphabet_ivert = {v:k for k, v in alphabet.items()}

def encrypt(word):

    word_ls = []
    word_num_ls = []
    key_ls = [] 
    key_num_ls = []
    word_num_encrypt_ls = []
    word_encrypt_ls =[]

    for letter in range(len(word)):

        word_ls.append(word[letter])#to debug
        word_num_ls.append(alphabet[word[letter]])

        key_ls.append(crypt_key[letter%len(crypt_key)])#to debug
        key_num_ls.append(alphabet[crypt_key[letter % len(crypt_key)]])

        letter_num_encrypt = (word_num_ls[letter]+key_num_ls[letter])%len(alphabet)

        word_num_encrypt_ls.append(letter_num_encrypt)
        word_encrypt_ls.append(alphabet_ivert[letter_num_encrypt])

    word_encrypt_ls.insert(0,"#")
    word_encrypt = "".join(word_encrypt_ls)
    return word_encrypt

def decrypt(encrypt_word):


    decrypt_word_ls = []

    encrypt_word_no_hash = encrypt_word[1:]

    for letter in range(len(encrypt_word_no_hash)):

        encrypt_word_num = alphabet[encrypt_word_no_hash[letter]]
        key_num = alphabet[crypt_key[letter % len(crypt_key)]]

        letter_num_decrypt = (encrypt_word_num-key_num+len(alphabet))%len(alphabet)

        decrypt_word_ls.append(alphabet_ivert[letter_num_decrypt])
        
    word_decrypt = "".join(decrypt_word_ls)
    return word_decrypt

def create_chiffre():
    hangman.clear_terminal()
    hangman.big_text("hangman")
    print("Jetzt zu verschlüsselndes Wort eingeben:\n")
    word = str(input())
    hangman.clear_terminal()
    hangman.big_text("hangman")
    print("Das verschlüsselte Wort lautet:\n")
    print("Kopiere es und schicke es jmd. zum erraten:\n")
    print(encrypt(word))
    input("Enter...")
