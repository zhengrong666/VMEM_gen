from Crypto.Hash import cSHAKE256, cSHAKE128

def string_to_binary(s):
    return ''.join(format(ord(c), '08b') for c in s)

s = "OpenTitan"

# binary_s = int(string_to_binary(s))
# # print(binary_s)
# bytes_per_word = 8
to_hash = b''
# to_hash += binary_s.to_bytes(bytes_per_word, byteorder='little')
b=s.encode()
print(b)
to_hash += b

hash_obj = cSHAKE256.new(data=b,
                                 custom='Ibex'.encode('UTF-8'))
digest_bytes = hash_obj.read(16)
digest256 = int.from_bytes(digest_bytes, byteorder='little')
print(hex(digest256))