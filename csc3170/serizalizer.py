from rest_framework.serializers import Serializer,JSONField
class CreateUserSerizalizer(Serializer):
    args=JSONField()
    class Meta:
        fields=["args"]