from mailerpy import Mailer

my_mailer = Mailer("smtp.gmail.com", 587, "sharadyadav12ta@gmail.com", "jecr eacy zacm zqeh")

to_emails = ["aayushshrestha.078@kathford.edu.np", "ooreo9782@gmail.com"]

subject = "test email from mailerpy"
body = "hello, \n\nthis is a test email sent using mailerpy.\n\nbest regards\nsharad"
for email in to_emails:
    receiver_name = email.split("@")[0]
    body = f"hello,{receiver_name} \n\nthis is a test email sent using mailerpy.\n\nbest regards\nsharad"
    my_mailer.send_mail([email], subject, body)
print("emails sent sucessfully")