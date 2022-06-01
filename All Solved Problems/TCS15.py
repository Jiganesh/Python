from cryptography.fernet import Fernet


def encrdecr( keyval, textencr, textdecr):
    
    fernet = Fernet(keyval)
    main_list = []
    main_list.append(fernet.encrypt(textencr))
    main_list.append(fernet.decrypt(textdecr).decode())
    
    return main_list

