from rest_framework import serializers, views
from rest_framework.response import Response
import re


class PasswordValidationSerializer(serializers.Serializer):
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        
        if not re.search(r"[A-Za-z0-9]", value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/']", value):
            raise serializers.ValidationError("Password must contain at least one special character.")
        
        if not re.search(r"\d", value):
            raise serializers.ValidationError("Password must contain at least one number.")
        return value

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError({"confirm_password": "Confirm password does not match password."})
        return data
