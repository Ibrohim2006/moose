import requests
from django.core.exceptions import ValidationError
from django.conf import settings
from urllib.parse import quote_plus

BOT_ID = settings.BOT_ID
CHAT_ID = settings.CHAT_ID
TELEGRAM_API_URL = settings.TELEGRAM_API_URL


def send_message_telegram(obj):
    message = (
        "<b>Project:</b> Moose\n"
        f"📞 <b>Phone number:</b> {obj.phone_number}\n"
        f"👤 <b>First name:</b> {obj.first_name}\n"
        f"👤 <b>Last name:</b> {obj.last_name}\n"
        f"📧 <b>Email:</b> {obj.email}\n"
        f"💬 <b>Message:</b> {obj.message}"
    )

    url = f"https://api.telegram.org/bot{settings.BOT_ID}/sendMessage?chat_id={settings.CHAT_ID}&text={quote_plus(message)}&parse_mode=HTML"
    return requests.get(url)


def phone_number_validation(phone_number):
    if len(phone_number) == 13 and phone_number[:4] == '+998' and phone_number[1:13].isdigit():
        return True
    raise ValidationError('phone_number is invalid')
