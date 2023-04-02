from rest_framework import serializers

class CropPredictionSerializers(serializers.Serializer):
	N_SOIL = serializers.IntegerField()
	P_SOIL = serializers.IntegerField()
	K_SOIL = serializers.IntegerField()
	TEMPARATURE = serializers.FloatField()
	HUMIDITY = serializers.FloatField()
	PH = serializers.FloatField()
	RAINFALL = serializers.FloatField()
  
	class Meta:
		fields = ["N_SOIL","P_SOIL","K_SOIL","TEMPARATURE","HUMIDITY","PH","RAINFALL"]
