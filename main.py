import logging,base64,time,secrets,string,sys

sys.tracebacklimit = 0

def Info():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.info('Hello, World!')


Info()
time.sleep(1)


def Cipher(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


def DeCipher(words):
    base64_bytes = words.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('ascii')

def PwdGenerator(pwd_length):
    [letters,digits,special_chars] = [string.ascii_letters,string.digits,string.punctuation]
    alphabet = letters + digits + special_chars
    if pwd_length < 8:
        raise Exception('Password is too short')
    else:
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))
        return pwd


words = input("Input message to encryption...")
coded = Cipher(words)
print(coded)
print(DeCipher(coded))
print(PwdGenerator(int(input("How long should be your password ?"))))