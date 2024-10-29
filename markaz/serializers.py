from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Xona, Oqituvchi, Oquvchilar, Fani

class XonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xona
        fields = ('id', 'nomi', 'sigimi')

    def validate_sigimi(self, sigimi):
        if sigimi <= 0 or sigimi > 20:
            raise ValidationError({
                "status": False,
                "xabar": "Xona sigimi manfiy bo'lishi mumkin emas yoki 20 dan katta bo'lishi mumkin emas"
            })

        return sigimi

    def validate(self, data):
        nomi = data.get("nomi", None)

        print("Nomi -> ", nomi)
        if not nomi.isalpha():
            print("nomda sonlar mavjud")
            raise ValidationError(
                    "Xona nomida sonlar bo'lishi mumkin emas"
            )

        if nomi == "Qxona":
            print("Xona Q")
            raise ValidationError(
                {
                    "status": False,
                    "message": "Bunday nomda saqlash mumkin emas"
                }

            )

        if Xona.objects.filter(nomi__exact=nomi):
            raise ValidationError(
                {
                    "status": False,
                    "xabar": "Bunday xona oldin saqlangan"
                }
            )
        return data


class OqituvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oqituvchi
        fields = '__all__'

class OquvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oquvchilar
        fields = '__all__'

class FanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fani
        fields = '__all__'

