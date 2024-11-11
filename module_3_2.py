# Teplova // create a function with three parametres, the first two of them are usual arguments, the last one is a named argument
def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    # create a variable to write the ends. It's more reasonable because you can add more ends and you won't need to rewrite a condition
    end = (".ru", ".com", ".net")
    if "@" not in recipient or not recipient.endswith(end): # use method endswith to check the ends
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient: # a condition
        print(f"Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com": # a condition
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else: # # a condition, if not
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email("message", 'teplova@gidrokor.')
send_email("message", 'university.help@gmail.com')
send_email("message", 'teplova@gidrokor.com')
send_email("message", 'teplova@gidrokor.ru', sender= "university..c")