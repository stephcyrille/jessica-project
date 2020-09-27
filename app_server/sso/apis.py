from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.parsers import  JSONParser
from rest_framework.permissions import AllowAny
from sso.lib.code_encrypt_decrypt import decrypt_message
from encrypted_login.models import AuthChecker


class CheckEncryptedCodeAPIView(APIView):
    permission_classes = [AllowAny]
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        encrypted_code = request.data["code"]
        print (encrypted_code)
        decrypted_code = decrypt_message(encrypted_code, settings.OTP_SECRET_KEY)
        print (decrypted_code)
        # session_user = request.user
        auth_checker = AuthChecker.objects.filter(status="wait").first()
        if auth_checker is not None:
            if auth_checker.q_code == decrypted_code.decode():
                code = { 
                    "code" : decrypted_code.decode()
                }
                return Response(code, status=status.HTTP_200_OK)
            return Response({"error" : "Code doesn't match"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error" : "No model"}, status=status.HTTP_400_BAD_REQUEST)