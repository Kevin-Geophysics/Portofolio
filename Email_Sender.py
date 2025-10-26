
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
def send_contact_email(name, email, message):
    """
    Send contact form submission via email.
    To enable this feature, set the following environment variables:
    - SMTP_SERVER: Your SMTP server (e.g., smtp.gmail.com)
    - SMTP_PORT: SMTP port (e.g., 587 for TLS)
    - SMTP_USERNAME: Your email address
    - SMTP_PASSWORD: Your email password or app-specific password
    - RECIPIENT_EMAIL: Email address to receive contact form submissions
    """
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT', '587'))
    smtp_username = os.getenv('SMTP_USERNAME')
    smtp_password = os.getenv('SMTP_PASSWORD')
    recipient_email = os.getenv('RECIPIENT_EMAIL')
    if not all([smtp_server, smtp_username, smtp_password, recipient_email]):
         return False, "Email configuration is incomplete. Please set SMTP environment variables."
    try:
         msg = MIMEMultipart('alternative')
         msg['Subject'] = f"Portfolio Contact Form: Message from {name}"
         msg['From'] = smtp_username
         msg['To'] = recipient_email
         msg['Reply-To'] = email
         text_body = f"""
         New contact form submission:
         Name: {name}
         Email: {email}
         Message:
         {message}
         """
         html_body = f"""
         &lt;html&gt;
             &lt;body style="font-family: Arial, sans-serif; padding: 20px;"&gt;
                  &lt;h2 style="color: #667eea;"&gt;New Contact Form Submission&lt;/h2&gt;
                  &lt;div style="background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;"&gt;
                      &lt;p&gt;&lt;strong&gt;Name:&lt;/strong&gt; {name}&lt;/p&gt;
                      &lt;p&gt;&lt;strong&gt;Email:&lt;/strong&gt; &lt;a href="mailto:{email}"&gt;{email}&lt;/a&gt;&lt
                  &lt;/div&gt;
                  &lt;div style="background-color: #ffffff; padding: 15px; border: 1px solid #ddd; border-radius: 5px;
                      &lt;h3&gt;Message:&lt;/h3&gt;
                      &lt;p&gt;{message.replace(chr(10), '&lt;br&gt;')}&lt;/p&gt;
                  &lt;/div&gt;
             &lt;/body&gt;
         &lt;/html&gt;
         """
         part1 = MIMEText(text_body, 'plain')
         part2 = MIMEText(html_body, 'html')
         msg.attach(part1)
         msg.attach(part2)
         with smtplib.SMTP(str(smtp_server), smtp_port) as server:
             server.starttls()
             server.login(str(smtp_username), str(smtp_password))
             server.send_message(msg)
         return True, "Email sent successfully!"
    except Exception as e:
         return False, f"Failed to send email: {str(e)}"
