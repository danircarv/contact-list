contacts = []   
def add_contact(contacts, contact_name, contact_email, contact_phone ):
    contact = {"name": contact_name,"phone":contact_phone  ,"email": contact_email, "favorite": False}
    contacts.append(contact)
    print(f"Contato {contact_name} foi adicionada com sucesso!")
    return

def show_contacts(contacts):
    print("\nLista de Contatos")
    for index, contact in enumerate(contacts, start=1):
       status = "♡" if contact["favorite"] else " "
       contact_name = contact["name"]
       contact_email = contact["email"]
       contact_phone = contact["phone"]
       print(f"{index}. {status} {contact_name} email:{contact_email} phone:{contact_phone} ")
    return
    
def update_contact_name(contacts, contact_index, contact_new_name, contact_new_email, contact_new_phone):
    corrected_contact_index = int(contact_index) - 1
    if corrected_contact_index >= 0 and corrected_contact_index < len(contacts):
        contacts[corrected_contact_index]["name"] = contact_new_name
        contacts[corrected_contact_index]["email"] = contact_new_email
        contacts[corrected_contact_index]["phone"] = contact_new_phone
        print(f"Contato {contact_index} atualizada para {contact_new_name}, {contact_new_email}, {contact_new_phone}")
    else:
        print("índice de Contato inválido")
    return

def check_contact(contacts, contact_index):
    corrected_contact_index = int(contact_index) - 1
    if corrected_contact_index >= 0 and corrected_contact_index < len(contacts):
        contacts[corrected_contact_index]["favorite"] = True
    print(f"Contato {contact_index} marcada como favorito")
    return

def delete_contact(contacts, contact_index):  # Function name corrected to singular
    corrected_contact_index = int(contact_index) - 1
    if 0 <= corrected_contact_index < len(contacts):
        del contacts[corrected_contact_index]  # Using `del` for efficient deletion
        print(f"Contato {contact_index} deletado com sucesso")
    else:
        print("índice de Contato inválido")
    return