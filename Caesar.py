#凯撒密码
from __future__ import annotations

from string import ascii_letters

def encrypt(input_string: str, key: int, alphabet: str | None = None) -> str:
    '''
    
    参数：
    ----------
    * input_string: 需要编码的明文
    * 键：将消息移动的字母数
    选修的：
    *字母表（无）：用于编码密码的字母表，如果不是
        指定，标准的英文字母大小写
        使用字母
    return：
    * 包含编码密文的字符串

    '''
    alpha = alphabet or ascii_letters

    result = ""

    for character in input_string:
        if character not in alpha:
             # Append without encryption if character is not in the alphabet
             result += character

        else:
            new_key = (alpha.index(character)+key) % len(alpha)
             # Get the index of the new key and make sure it isn't too large
            result += alpha[new_key]
            # Append the encoded character to the alphabet

    return result
def decrypt(input_string: str, key: int, alphabet: str | None = None) -> str:

    key *= -1

    return encrypt(input_string, key, alphabet)
def brute_force(input_string: str, alphabet:str | None = None) -> dict[int,str]:
    '''
    ===========
    返回所有可能的键组合和解码后的字符串
    字典的形式

     参数：
    ----------
    * input_string: 暴力破解时需要使用的密文
    选修的：
    *字母表：（无）：用于解码密码的字母表，如果不是
        指定，标准的英文字母大小写
        使用字母

    '''
    alpha = alphabet or ascii_letters

    brute_force_data = {}
    # To store data on all the combinations

    # Cycle through each combination
    for key in range(1,len(alpha)+1):
        # Decrypt the message and store the result in the data
        brute_force_data[key] = decrypt(input_string,key,alpha)

        return brute_force_data
if __name__ == "__main__":
    while True:
        print(f'\n{"-" * 10}\n Menu\n{"-" * 10}')
        print(*["1.Encrypt", "2.Decrypt", "3.BruteForce", "4.Quit"], sep="\n")
            # get user input
        choice = input("\nwhat would you like to do?: ").strip() or "4" 
            # run functions based on what the user chose
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice, please enter a valid choice")
        elif choice =="1":
            input_string = input("please enter the string to be encrypted:")
            key = int(input("plaese enter off-set: ").strip())

            print(encrypt(input_string,key))
        elif choice =="2":
            input_string = input("please enter the string to br decrypted:")
            key = int(input("please enter off-set:").strip())

            print(decrypt(input_string,key))
        elif choice =="3":
            input_string = input("please enter the string to be decrypted:")
            brute_force_data = brute_force(input_string)

            for key,value in brute_force_data.items():
                print(f"key:{key} | message : {value}\n")

        elif choice =="4":
            print("goodbye!")
            break