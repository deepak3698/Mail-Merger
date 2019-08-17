import os #import os module for using their methods

# open names.txt for reading
with open("name.txt",'r') as names_file:
    # findig names for deletion.
    for name in names_file:
        mail = f"{name.strip()}.txt"
        try:
            # deleting files
            os.remove(mail)
        except:
            # if file is not in the names.txt then skip.
            pass

print("!!!!!!!!Work Done!!!!!!!!")
