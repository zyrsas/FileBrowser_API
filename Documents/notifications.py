from Documents.models import User
from pyfcm import FCMNotification


API_KEY = "AAAAhMVvqN0:APA91bGmK5ie-OpBUEihpGVMHqqJ3j5dwqfJ8ZEEAy8s5UkK9Vb7Y8r3niQ9xUpUvW3SLLTkCWYcFBcShgbu3XMkYnpF683iYNHHTZMMS8SgoVtYVSHcDWwQnzyYwqcpjMO-EfpK-oQC"


def sendNotification(count):
    users_regID = User.objects.all().values("regID")

    for user in users_regID:

        user_reg = user['regID']
        print(user_reg)
        if user_reg:
            push_service = FCMNotification(api_key=API_KEY)
            registration_id = user_reg
            message_title = "DirectoryNNR"
            message_body = "Загружено " + str(count) + " новых документов"
            push_service.notify_single_device(registration_id=registration_id,
                                              message_title=message_title,
                                              message_body=message_body,
                                              badge=count)






