def encode_rle(text):
    encoded_text = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            encoded_text += str(count) + text[i-1]
            count = 1

    # Tambahkan karakter terakhir dan jumlahnya ke encoded_text
    encoded_text += str(count) + text[-1]
    return encoded_text

def decode_rle(encoded_text):
    decoded_text = ""
    i = 0
    while i < len(encoded_text):
        count = int(encoded_text[i])
        character = encoded_text[i+1]
        decoded_text += character * count
        i += 2
    return decoded_text

# Contoh penggunaan
text = "ALVINKIRANA"
encoded_text = encode_rle(text)
print("Encoded text:", encoded_text)

decoded_text = decode_rle(encoded_text)
print("Decoded text:", decoded_text)
