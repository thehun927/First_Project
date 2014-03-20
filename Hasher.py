import hashlib

filePath = "/home/attila/Pictures/images (1).jpg"

def md5Checksum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()
print(filePath)
print('The MD5 checksum of the file is', md5Checksum(filePath))

