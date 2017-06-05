import random,string
import datetime
import hashlib,base64


def getNonce():
     return ''.join(random.sample(string.ascii_letters+string.digits, 25))


def getCreated():
    return datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')


def getPasswordDigest(password):
    str1 = getNonce() + getCreated()+password
    hash = hashlib.sha256()
    hash.update(str1.encode('utf-8', 'strict'))
    return base64.b64encode(hash.digest())

str = getPasswordDigest('123456')
print(str)