from actions import contacts, add_contact, show_contacts,update_contact_name, delete_checked_contacts,check_contact

while True:
    print("\n Menu do Gerenciador de Lista de contatos:")
    print("1. Adicionar contato")
    print("2. Ver contato")
    print("3. Atualizar contato")
    print("4. Completar contato")
    print("5. Deletar contatos completadas")
    print("6. Sair ")

    choice = input("Digite sua escolha: ")

    match choice:
        case "1":
            contact_name = (input("Digite o nome do contato que deseja adicionar: "))
            contact_phone = (input("Digite o telefone do contato que deseja adicionar: "))
            contact_email = (input("Digite o email do contato que deseja adicionar: "))
          
            add_contact(contacts, contact_name, contact_email, contact_phone)
        case "2":
            show_contacts(contacts=contacts)    
        case "3":
            show_contacts(contacts=contacts)
            contact_index = input("Digite o numero do contato que deseja atualizar:")
            contact_new_name = input("Digite o novo nome do contato: ")
            contact_new_email = input("Digite o novo email do contato: ")
            contact_new_phone = input("Digite o novo telefone do contato: ")
            update_contact_name(contacts, contact_index, contact_new_name,contact_new_email, contact_new_phone)
            
        case "4":
            show_contacts(contacts)
            contact_index = input("Digite o numero da contato que deseja completar: ")
            check_contact(contacts,contact_index )
              
        case "5":
            delete_checked_contacts(contacts)
            show_contacts(contacts)
        case "6":
            break

        
  
            
            
            

