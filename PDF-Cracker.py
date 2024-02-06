import PyPDF2
import time

def open_pdf_with_password(pdf_file, password):
    start_time = time.time()
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        if reader.isEncrypted:
            reader.decrypt(password)
        # Check if the decryption was successful
        if reader.decrypt(password) == 1:
            print(f"PDF súbor bol úspešne otvorený s heslom: {password}")
        else:
            print(f"PDF súbor sa nepodarilo otvoriť s heslom: {password}")
        end_time = time.time()
        print(f"Čas potrebný na otvorenie súboru s heslom '{password}': {end_time - start_time} sekúnd")

# Názov PDF súboru
pdf_file = "furniture.pdf"

# Načítanie hesiel zo súboru
with open("list.txt", "r") as f:
    passwords = f.read().splitlines()

# Pre každé heslo otvorte PDF súbor
for password in passwords:
    open_pdf_with_password(pdf_file, password)
