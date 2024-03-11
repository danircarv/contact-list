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

def delete_checked_contacts(contacts):
   
    for contact in contacts:
        if contact["favorite"]:
            contacts.remove(contact)
            
    print("Contatos favorites foram deletadas")
    return