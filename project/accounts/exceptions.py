from rest_framework.exceptions import APIException


class EmailServiceUnavaliable(APIException):
    status_code = 503
    default_detail = (
        "Não foi possivel enviar email com instruções. Tente mais tarde por favor."
    )
    default_code = "email_service_unavaliable"
