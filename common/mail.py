from flask import render_template

import config


def email_verification(user_id, email):
    try:
        import smtplib, ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        sender_email = config.EMAIL
        receiver_email = email
        password = config.PASSWORD
        message = MIMEMultipart()
        message["Subject"] = "Forgot password"
        message["From"] = sender_email
        message["To"] = receiver_email
        verify_email = config.APP_BASE_URL + "/api/v1/user/ForgotPassword?user_id=" + str(user_id) + ""
        email_part = MIMEText(render_template('sendingMail.html', data=str(verify_email)), "html")
        message.attach(email_part)
        context = ssl.create_default_context()
        print(message)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        return 1
    except Exception as err:
        return 0
