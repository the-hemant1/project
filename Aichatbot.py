from tkinter import *
from tkinter import scrolledtext
root = Tk()
root.title("Vex")
root.geometry("600x715")
root.resizable(False, False)
root.config(bg="#B1B1B1")

def get_response(user_input):
    user_input = user_input.lower()
    
    if user_input == "my name is":
        return "Please complete the phrase"
    elif "my name is " in user_input:
        name = user_input.split("my name is ")[1]
        return f"Hello {name}, How are you today?"
    
    elif "hi" in user_input or "hello" in user_input or "hey" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm doing well, thank you! How about you?"
    elif "sorry" in user_input:
        return "It's alright, no worries!"
    elif "what is your name" in user_input:
        return "I am a simple chatbot created by you."
    elif "what is your favorite color" in user_input:
        return "I don't have a favorite color, but I like the idea of blue!"
    elif "what is the capital of America" in user_input:
        return "The capital of France is Washington DC."
    elif "quit" in user_input:
        return "Bye, take care. See you soon!"
    elif "how many genders are there" in user_input:
        return "only 2"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"


def send_message(event=None):
    user_input = user_entry.get()
    if user_input.strip() == "":
        return
    chat_history.insert(END, "You:  " + user_input + '\n')
    response = get_response(user_input)
    chat_history.insert(END, "Vex:  " + response + '\n')
    user_entry.delete(0, END)
    if "quit" in user_input.lower():
        root.quit()

frame =Label(root)
chat_history = scrolledtext.ScrolledText(frame, wrap=WORD, width=50, height=20, bd=9, font=("cambria 15 bold"), relief=SUNKEN)
chat_history.pack(padx=10, pady=10)
frame.pack(padx=10, pady=10)

label = Label(root, text="ASK HERE", font=("cambria 18 bold"), bd=9)
label.pack(pady=1, padx=5)

user_entry = Entry(root, width=30, font=("cambria 20 bold"), bd=9, fg="black")
user_entry.pack(pady=10)
user_entry.bind("<Return>", send_message)  

send_button = Button(root, text="Send", bd=9, fg="#fff", bg="#2a2d36", command=send_message)
send_button.pack(padx=5, pady=5)
root.mainloop()