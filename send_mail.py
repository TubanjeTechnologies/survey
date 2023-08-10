import smtplib
from email.mime.text import MIMEText


def send_mail(fullname, artist, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '22da4145a3f4ff'
    password = 'be83b0e94eb89c'
    message = f"<h3>New Feedback Submission</h3><ul>" \
              f"<Li>Contributor's name: {fullname}</li>" \
              f"<Li>Artist's name: {artist}</li>" \
              f"<Li>Rating: {rating}</li>" \
              f"<Li>Comment: {comments}</li>" \
              f"</ul> "

    sender_email = 'emmanuelkaingu1@gmail.com'
    receiver_email = 'tubanje1@outlook.com'
    msg = MIMEText(message, 'html')
    msg['SUBJECT'] = 'Artist Survey Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

#     send the email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
