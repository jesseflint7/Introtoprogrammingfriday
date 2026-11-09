def box_me_in(input_text, box_char = '*'):
    box_length = len(input_text) + (2*2) 
    output = box_char * box_length + "\n"
    output += box_char + " " + input_text + " " + box_char + "\n"
    output += box_char * box_length + "\n"
    return output 
#I added return statement here
if __name__ == "__main__":
    user_input = "Hello world" 
    print(box_me_in(user_input))
    #I added user_input inside the print line
    if input("Output to file? (y/n) > ").lower() == 'y':
        with open('boxmein.txt', 'w') as output_file: 
            #I added a "w" instead of "r" to write to the file
            output_file.write(box_me_in(user_input))
            print("A copy of your output is in boxmein.txt")

# This was really complicated to me I still don't know if I actually fixed what I was supposed to
# I think I understand it but I keep second guessing it.