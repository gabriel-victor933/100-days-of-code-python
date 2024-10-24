
def main():
    with open("day-24/input/names/invited_names.txt","r") as file1:
        names = file1.read().split('\n')

    with open("day-24/input/letters/starting_letter.txt","r") as file2:
        message = file2.read()

    for name in names:
        with open(f"day-24/output/ready_to_send/{name}_invite_letter.txt","w") as file_write:
            edited_message = message.replace('[name]',name)
            file_write.write(edited_message)
    

main()