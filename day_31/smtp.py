import smtplib

DRY_RUN = True


def main():
    smtp_config = {
        "name": "smtp.domain1.com",
        "port": 587
    }
    credentials = {
        "email": "address1@domain1.com",
        "app_password": "password"
    }
    dst_email = "address2@domain2.com"

    mail_subject = "Subject"
    mail_body = """\
    Multi-line
    Body\
    Message"""

    with smtplib.SMTP(smtp_config["name"], port=smtp_config["port"]) as service:
        print("Service started")

        service.starttls()
        print("TLS started")

        service.login(user=credentials["email"],
                      password=credentials["app_password"])
        print("Login is ok")

        try:
            if not DRY_RUN:
                service.sendmail(from_addr=credentials["email"],
                                 to_addrs=dst_email,
                                 msg=f"Subject:{mail_subject}\n\n{mail_body}")
        except Exception as err:
            print(err)
        else:
            print("Email sent")

    print("Service stopped")


if __name__ == "__main__":
    main()
