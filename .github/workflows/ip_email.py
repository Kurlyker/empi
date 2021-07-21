from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
from sqlalchemy import create_engine
from ssl import create_default_context
import sys

filename = database.db
login = splatash@gmail.com
password = sys.argv[1]
receiver = splatash@gmail.com

engine = engine = create_engine('sqlite:///{}'.format(filename), echo = False)
connection = engine.connect()
ips = connection.execute("SELECT DISTINCT ip_address from access_logs")

subject = 'Сергій-Платаш-343ск Lab5'
body = 'Unique ips:\n' + ', '.join(map(lambda row: row['ip_address'],ips))

message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = login
message["To"] = receiver
message.attach(MIMEText(body, "plain"))

context = create_default_context()
with SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(login, password)
    server.sendmail(login, receiver, message.as_string())
