def decode_caesar(encoded_message, shift):
    decoded_message = ""
    for char in encoded_message:
        if char.isalpha():
            if char.islower():
                decoded_char = chr((ord(char) - shift - 97) % 26 + 97)
            else:
                decoded_char = chr((ord(char) - shift - 65) % 26 + 65)
            decoded_message += decoded_char
        else:
            decoded_message += char
    return decoded_message

# Example usage:
encoded_message = "Ymfy ujwxts nx htrnsl ktw rj! Nk dtz knsi ymnx styj, qttp fwtzsi rd uwtujwyd. Mnsy: N anxnyji ymj fwjf bnym rd ywtqqjd kwtr ymj lfwijs xmji. - 5"
shift = 5

decoded_message = decode_caesar(encoded_message, shift)
print(decoded_message)
