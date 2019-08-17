# Python mail with merge data
# Names are in the file names.txt
# Body of the mail is in body.txt
with open("name.txt") as names_file:# open names.txt for reading
   with open("body.txt") as body_file:# open body.txt for reading  
       # read entire content of the body
       body = body_file.read()
       # iterate over names
       for name in names_file:
           mail = f"Dear {name.strip()},\n\n{body}"
           # write the mails to individual files
           with open(name.strip()+".txt",'w') as mail_file:
               mail_file.write(mail)

print("!!!!!!!!Work Done!!!!!!!!")