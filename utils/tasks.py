from celery import shared_task


@shared_task(bind=True)
def SendMial(self, subject, message, sent_from, sent_to):
    print(f"Subject: {subject} | Messsage: {message} | Sent From: {sent_from} | Sent To: {sent_to}")
    return "Email Successfully Send to the user"