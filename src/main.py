import smtplib, receiver, sendEmail

"""
message = 'hi'
server.sendmail('test.mattketk@gmail.com', 'test.mattketk@gmail.com', message)
server.quit()
"""

# CONFIG #
_imap_url = 'imap.gmail.com'
_email = 'test.mattketk@gmail.com'
_server = 'smtp.gmail.com'
##########

loginSuccess = False
login = ""



server = smtplib.SMTP(_server, 587)
server.starttls()

while not loginSuccess:
    try:
        login = input("pass: ")
        loginSuccess = True
        server.login(_email, login)

    except smtplib.SMTPAuthenticationError:
        print("invalid login...")
        loginSuccess = False

con = imaplib.IMAP4_SSL(_imap_url)
con.login(_email, login)

print("login successful\nawaiting incoming emails...")

con.select('INBOX')
