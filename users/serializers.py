from rest_framework import serializers

from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "username",
            "password",
            "country",
            "phone",
            "user_payments",
            "user_subscriptions",
        ]
