import requests
from bs4 import BeautifulSoup


def get_morse_code_dict():
    mors_url = 'http://www.turkishstraits.com/info/morsecode'
    response = requests.get(mors_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    morse_code_dict = {}
    table_cells = soup.findAll(name='td')
    for i in range(0, len(table_cells)-1, 2):
        character = table_cells[i].text.strip().upper()
        morse_code = table_cells[i + 1].text.strip()
        morse_code_dict[character] = morse_code

    return morse_code_dict


def text_to_morse(text, morse_code_dict):
    morse_text = ''
    for char in text:
        char_upper = char.upper()
        if char_upper in morse_code_dict:
            morse_text += morse_code_dict[char_upper] + ' '

    return morse_text.strip()

def main():
    print("Morse Code Converter")
    morse_code_dict = get_morse_code_dict()

    while True:
        input_text = input("Enter the text you want to convert to Morse code (type 'exit' to quit): ")
        if input_text.lower() == 'exit':
            break

        morse_code = text_to_morse(input_text, morse_code_dict)
        print(f"Morse Code: {morse_code}\n")

if __name__ == "__main__":
    main()
