import hashlib
import secrets

class Security(object):
    def __init__(self):
        #generate random xor key
        #Using 32 bytes or more ensures that the number generated is cryptographically secure
        self.binary_key = secrets.token_bytes(32)
    
    
    def xor_encode(self, username, password):
        if username is not None:
            if password is not None:
                # Convert username and password to byte strings
                username_bytes = bytes(username, 'utf-8')
                password_bytes = bytes(password, 'utf-8')

                # Get length of username and password
                u_length = len(username_bytes)
                p_length = len(password_bytes)

                # Perform XOR operation on corresponding bytes
                u_binary_key = self.binary_key[:u_length]
                p_binary_key = self.binary_key[:p_length]
                u_encode_bytes = bytes([a^b for a, b in zip(username_bytes, u_binary_key)])
                p_encode_bytes = bytes([a^b for a, b in zip(password_bytes, p_binary_key)])

                # Convert output to hexadecimal string
                u_encode_hex = u_encode_bytes.hex()
                p_encode_hex = p_encode_bytes.hex()
            else:
                return (f'The username was empty')
        else:
            return (f'The username was empty')
        
        return u_encode_hex, p_encode_hex
    

    def xor_decode(self, username_hex, password_hex):
        # Convert hexadecimal string to byte string
        user_bytes = bytes.fromhex(username_hex)
        pass_bytes = bytes.fromhex(password_hex)
        
        # Get length of username and password
        u_length = len(user_bytes)
        p_length = len(pass_bytes)
        
        u_binary_key = self.binary_key[:u_length]
        p_binary_key = self.binary_key[:p_length]
        u_decode_bytes = bytes([a^b for a, b in zip(user_bytes, u_binary_key)])
        p_decode_bytes = bytes([a^b for a, b in zip(pass_bytes, p_binary_key)])

        # Convert output to original string
        u_decode_string = u_decode_bytes.decode('utf-8')
        p_decode_string = p_decode_bytes.decode('utf-8')

        return u_decode_string, p_decode_string