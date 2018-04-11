import smtplib


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login('test.mattketk@gmail.com', 'N3wp0rt_1234')
message = 'hi'
server.sendmail('test.mattketk@gmail.com', 'test.mattketk@gmail.com', message)
server.quit()
