import json

# Kamus Morse Code
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': ' '  # untuk memisahkan kata
}

# Membalik kamus Morse Code untuk decoding
inverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

# Fungsi untuk menerjemahkan teks ke Morse code
def translate_to_morse(text):
    morse_translated = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_translated += morse_code_dict[char] + ' '
        else:
            morse_translated += '? '  # karakter yang tidak dikenali
    return morse_translated.strip()

# Fungsi untuk menerjemahkan Morse code ke teks
def translate_to_text(morse_code):
    words = morse_code.split('   ')  # menggunakan tiga spasi untuk memisahkan kata
    decoded_text = ''
    for word in words:
        characters = word.split()
        for char in characters:
            if char in inverse_morse_code_dict:
                decoded_text += inverse_morse_code_dict[char]
            else:
                decoded_text += '?'  # kode morse yang tidak dikenali
        decoded_text += ' '
    return decoded_text.strip()

# Fungsi untuk mencetak hasil terjemahan yang lebih rapi
def print_translation(type, original, translated):
    print("\nHasil Terjemahan:")
    print("-----------------")
    if type == 'text_to_morse':
        print(f"Teks Asli: {original}")
        print(f"Kode Morse: {translated}")
    elif type == 'morse_to_text':
        print(f"Kode Morse Asli: {original}")
        print(f"Teks Terjemahan: {translated}")
    print("-----------------\n")

# Fungsi untuk menyimpan hasil terjemahan ke dalam file JSON
def save_to_json(file_name, original, translated, type):
    data = {
        "Original": original,
        "Translated": translated,
        "Type": type
    }
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Hasil berhasil disimpan dalam file JSON: {file_name}")

# Fungsi untuk membaca teks dari file
def read_text_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"File '{file_name}' tidak ditemukan.")
        return None

# Fungsi utama
def main():
    print("Selamat datang di Aplikasi Penerjemah Morse Code!")
    while True:
        print("\nPilih opsi:")
        print("1. Teks ke Kode Morse")
        print("2. Kode Morse ke Teks")
        print("3. Terjemahkan menggunakan file")
        print("4. Keluar")
        choice = input("Masukkan pilihan Anda (1/2/3/4): ")
        
        if choice == '1':
            user_input = input("Masukkan teks yang ingin diterjemahkan: ")
            translated_text = translate_to_morse(user_input)
            print_translation('text_to_morse', user_input, translated_text)
            save_option = input("Apakah Anda ingin menyimpan hasil terjemahan ke dalam file JSON? (y/n): ").lower()
            if save_option == 'y':
                file_name = input("Masukkan nama file untuk menyimpan hasil (contoh: output.json): ")
                save_to_json(file_name, user_input, translated_text, 'text_to_morse')
        elif choice == '2':
            user_input = input("Masukkan kode Morse yang ingin diterjemahkan (gunakan spasi tunggal untuk memisahkan karakter dan tiga spasi untuk memisahkan kata): ")
            translated_text = translate_to_text(user_input)
            print_translation('morse_to_text', user_input, translated_text)
            save_option = input("Apakah Anda ingin menyimpan hasil terjemahan ke dalam file JSON? (y/n): ").lower()
            if save_option == 'y':
                file_name = input("Masukkan nama file untuk menyimpan hasil (contoh: output.json): ")
                save_to_json(file_name, user_input, translated_text, 'morse_to_text')
        elif choice == '3':
            file_name = input("Masukkan nama file yang ingin dijadikan input: ")
            file_content = read_text_from_file(file_name)
            if file_content:
                file_type = input("Apakah file tersebut berisi teks (1) atau kode Morse (2)? Masukkan pilihan Anda (1/2): ")
                if file_type == '1':
                    translated_text = translate_to_morse(file_content)
                    print_translation('text_to_morse', file_content, translated_text)
                    save_to_json("output_morse.json", file_content, translated_text, 'text_to_morse')
                elif file_type == '2':
                    translated_text = translate_to_text(file_content)
                    print_translation('morse_to_text', file_content, translated_text)
                    save_to_json("output_text.json", file_content, translated_text, 'morse_to_text')
                else:
                    print("Pilihan tidak valid.")
        elif choice == '4':
            print("Terima kasih telah menggunakan aplikasi ini. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
