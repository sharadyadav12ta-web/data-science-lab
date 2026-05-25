from mailerpy import Mailer

my_mailer = Mailer("smtp.gmail.com", 587, "sharadyadav12ta@gmail.com", "jecr eacy zacm zqeh")

to_emails = ["aayushshrestha.078@kathford.edu.np", "ooreo9782@gmail.com", "rabindra@sapkotarabindra.com.np"]

subject = "test email from mailerpy"

attachment_list = [r"C:\Users\vs\Pictures\Saved Pictures\968100d2d047b3e9a186780cc2f3b264.jpg"]
body = "hello, \n\nthis is a test email sent using mailerpy.\n\nbest regards\nsharad"
for email in to_emails:
    receiver_name = email.split("@")[0]
    body = f"hello,{receiver_name} \n\nthis is a test email sent using mailerpy.\n\nbest regards\nsharad"
    my_mailer.send_mail([email], subject, body, attachments=attachment_list)
print("emails sent successfully")