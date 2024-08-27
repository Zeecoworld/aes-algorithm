def encrypt(self,value):   
           try:
                init_vector = self.get_16_sha1_digits("INITIAL-KEY").encode('utf-8') 
                key = self.get_16_sha1_digits("INITIAL-KEY").encode('utf-8')
                cipher = AES.new(key, AES.MODE_CBC, iv=init_vector)
                encrypted = cipher.encrypt(pad(value.encode('utf-8'),AES.block_size))
                return binascii.hexlify(encrypted).decode('utf-8')
           except Exception as ex:
                # print(ex)
                return None
                
                
def get_16_sha1_digits(self,input_str):
    sha1 = hashlib.sha1()
    sha1.update(input_str.encode('utf-8'))
    sha1_str = sha1.hexdigest()
    return sha1_str[:16]
