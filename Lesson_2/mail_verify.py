# checking if mai address is vaid
mails = ["abc@aa.com", "ssss.com", "sss@rerrr.com"]

for mail in mails:
    if "@" not in mail:
        print(mail)
        mails.remove(mail)


        print(mails)


