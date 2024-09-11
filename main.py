
PLACEHOLDER="[name]"
###

with open('invite.txt') as names_file:
    names=names_file.readlines()
    print(names)
with open('letter.txt') as letter_file:
    letter_content=letter_file.read()
    print(letter_content)
    for name in names:
        new_letter=letter_content.replace(PLACEHOLDER,name.strip())
        print(new_letter)
        with open(f'C:/Users/Nafim Ahmed/Videos/{name.strip()}.txt', mode="w") as complete_lrtter:
            complete_lrtter.write(new_letter)