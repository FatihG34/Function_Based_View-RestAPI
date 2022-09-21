from rest_framework import serializers
from fbv.models import Countries, People


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ["id", "country_name"]


class PeopleSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    country_id = serializers.IntegerField()

    class Meta:
        model = People
        fields = ["id", "first_name", "last_name",
                  "age", "country_id", "country"]
