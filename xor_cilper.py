class crypt:
    def __init__(self, key: int = 0):
        self.__key = key

    def encrypt(self, content: str, key: int) -> list[str]:
        assert isinstance(key, int) and isinstance(content, str)

        key = key or self.__key or 1

        key %= 255

        return [chr(ord(ch) ^ key) for ch in content]

    def decrypt(self, content: str, key: int) -> list[str]:
        assert isinstance(key, int) and isinstance(content, list)

        key = key or self.__key or 1

        key %= 255

        return [chr(ord(ch) ^ key) for ch in content]

    def encrypt_string(self, content: str, key: int = 0) -> str:
        assert isinstance(key, int) and isinstance(content, str)

        key = key or self.__key or 1

        # make sure key can be any size

        while key > 255:
            key -= 255
        # This will be returned
        ans = ""

        for ch in content:
            ans += chr(ord(ch) ^ key)

        return ans

    def decrypt_string(self, content: str, key: int = 0) -> str:
        assert isinstance(key, int) and isinstance(content, str)

        key = key or self.__key or 1

        while key > 255:
            key -= 255

        ans = ""

        for ch in content:
            ans += chr(ord(ch) ^ key)

        return ans

    def encrypt_file(self, file: str, key: int = 0) -> bool:
        assert isinstance(key, int) and isinstance(file, str)

        try:
            with open(file) as fin, open("D:\\PYTHON-TEST\\out\\encrypt.out", "w+") as fout:
                for line in fin:
                    fout.write(self.encrypt_string(line, key))
        except OSError:
            return False
        return True

    def decrypt_file(self, file: str, key: int = 0) -> bool:
        assert isinstance(key, int) and isinstance(file, str)

        try:
            with open(file) as fin, open("D:\\PYTHON-TEST\\out\\dencrypt.out", "w+") as fout:
                for line in fin:
                    fout.write(self.decrypt_string(line, key))
        except OSError:
            return False
        return True


cipher = crypt()

key = 67
print(cipher.encrypt("hallo welt", key))
print(cipher.encrypt("hallo welt", key))
print(cipher.decrypt(cipher.encrypt("hallo welt",key), key))
print(cipher.encrypt_string("hallo welt", key))
print(cipher.decrypt_string(cipher.encrypt_string("hallo welt", key), key))

if (cipher.encrypt_file("D:\\PYTHON-TEST\\out\\1.txt",key)):
    print("encrypt successful!")
else:
    print("encrypt unsuccessful!")
if(cipher.decrypt_file("D:\\PYTHON-TEST\\out\encrypt.out",key)):
    print("decrypt successful")
else:
    print("decrypt unsuccessful")


#
# 定义的 crypt 是一个类，所以你需要先实例化一个对象来用
# 刚刚装的 autopep8 是 python 代码的格式化插件，右键格式化可以统一格式
