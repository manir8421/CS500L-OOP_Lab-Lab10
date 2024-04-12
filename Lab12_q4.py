from abc import ABC, abstractmethod


class LegacyNotificationSystem:
    def sms_notification(self, phone_number: str, message: str) -> None:
        print("Simulates sending an SMS notification")

class NewNotificationSystem(ABC):
    @abstractmethod
    def send_email_notification(self, emailAddress: str, subject: str, body: str) -> None:
        pass
    @abstractmethod
    def sendPushNotification(self, deviceToken: str, title: str, message: str) -> None:
        pass
    @abstractmethod
    def send_social_media_update(self, social_media_platform: str, postContent: str) -> None:
        pass

class NotificationAdapter(NewNotificationSystem):
    def __init__(self, legacy_system: LegacyNotificationSystem) -> None:
        self.__legacy_system = legacy_system

    def sms_notification(self, phone_number: str, message: str) -> None:
        self.__legacy_system.sms_notification(phone_number, message)
        email_address = self.get_email()
        subject = self.get_subject()
        deviceToken = self.get_device()
        social_media = self.get_social_media()

        self.send_email_notification(email_address, subject, message)
        self.sendPushNotification(deviceToken, subject, message)
        self.send_social_media_update(social_media, message)

    def send_email_notification(self, emailAddress: str, subject: str, body: str) -> None:
         print(f"Sending a notification via email\t : {emailAddress} -{subject}: {body}")

    def sendPushNotification(self, deviceToken: str, title: str, message: str) -> None:
         print(f"Sending a push notification to device\t : {deviceToken} \t-{title}: {message}")

    def send_social_media_update(self, social_media_platform: str, postContent: str) -> None:
         print(f"Sending a social media update to LinkedIn: {social_media_platform} \t    : {postContent}")

    def get_email(self):
        return "all@sfbu.com"
    
    def get_subject(self):
        return "Spring 2024"
    
    def get_device(self):
        return "01234abc"
    
    def get_social_media(self):
        return "@LinkedIn_Media"
    
class SMSFactory:
    @staticmethod
    def get_sms_system(obj):
        return NotificationAdapter(obj)

def main():
    obj = LegacyNotificationSystem()
    sms_adapter = SMSFactory.get_sms_system(obj)
    sms_adapter.sms_notification("+1-123-456-7890", "Dear student, Make sure your registration for 'Spring semester 2024'.")

if __name__ == "__main__":
    main()
