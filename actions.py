contacts = []   
def add_contact(contacts, contact_name):
    contact = {"name": contact_name, "favorite": False}
    contacts.append(contact)
    print(f"Contato {contact_name} foi adicionada com sucesso!")
    return

def show_contacts(contacts):
    print("\nLista de Contatos")
    for index, contact in enumerate(contacts, start=1):
       status = "✓" if contact["favorite"] else " "
       contact_name = contact["name"]
       print(f"{index}. [{status}] {contact_name} ")
    return
    
def update_contact_name(contacts, contact_index, contact_new_name):
    corrected_contact_index = int(contact_index) - 1
    if corrected_contact_index >= 0 and corrected_contact_index < len(contacts):
        contacts[corrected_contact_index]["name"] = contact_new_name
        print(f"Contato {contact_index} atualizada para {contact_new_name}")
    else:
        print("índice de Contato inválido")
    return

def check_contact(contacts, contact_index):
    corrected_contact_index = int(contact_index) - 1
    if corrected_contact_index >= 0 and corrected_contact_index < len(contacts):
        contacts[corrected_contact_index]["favorite"] = True
    print(f"Contato {corrected_contact_index} marcada como favorite")
    return

def delete_checked_contacts(contacts):
   
    for contact in contacts:
        if contact["favorite"]:
            contacts.remove(contact)
            
    print("Contatos favorites foram deletadas")
    return