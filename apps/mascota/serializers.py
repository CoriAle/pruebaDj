from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.mascota.models import Mascota, Vacuna

class MascotaSerializer(ModelSerializer):
	
	"""vacuna = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='nombre'
     )
     """
	vacuna = serializers.PrimaryKeyRelatedField(many=True, queryset=Vacuna.objects.all())
	class Meta:
		"""docstring for Meta"""
		model = Mascota
		fields = ('nombre','sexo', 'edad_aproximada', 'fecha_rescate', 'persona', 'vacuna')
			
class MascotaListSelializer(ModelSerializer):
	vacuna = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='nombre'
     )
	class Meta:
		"""docstring for Meta"""
		model = Mascota
		fields = ('nombre','sexo', 'edad_aproximada', 'fecha_rescate', 'persona', 'vacuna')
			