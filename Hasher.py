import hashlib

filepath = "/home/attila/Pictures/images.jpg"

def md5Checksum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

print('The MD5 checksum of the file is', md5Checksum(filepath))

