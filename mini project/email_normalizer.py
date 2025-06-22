#Using all the String methods together

mail=input("Please enter your email id:")

clean_mail=mail.strip()

normalized_mail=clean_mail.lower()

index_mail=normalized_mail.find("@")

if index_mail !=-1:
    part= normalized_mail.split("@")
    username=part[0]
    domain=part[1]
    
    new_domain="outlook.com"
    
    mail1=normalized_mail.replace(domain, new_domain)
    
    print("Original email:",mail)
    print("New Mail id:", mail1)
    
else:
    print("The @ is missing in the email id ")