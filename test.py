from Crypto.Hash import SHA256
data = 'btestdata'.encode('utf8')
h = SHA256.new(data)
print(h.hexdigest())