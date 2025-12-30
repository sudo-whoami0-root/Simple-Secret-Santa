
import resend



resend.api_key = "----------------------------------"

def sendEmail(giver_name, giver_email, receiver_name):
        r = resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": giver_email,
            "subject": "Secret Santa Email",
            "html": f"<p>{giver_name} Your secret Santa is: {receiver_name} </p>"
        })







