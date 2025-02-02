import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "audrius13toto@gmail.com"
password = "cqdx bfes xmyt zxuo"

receiver = "audrius13toto@gmail.com"
my_context = ssl.create_default_context()
message = """\
    subject: Test!
    Hello, how are you?
    Bye!
"""

with smtplib.SMTP_SSL(host, port, context = my_context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
