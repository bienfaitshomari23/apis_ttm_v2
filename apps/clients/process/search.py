from rest_framework import serializers
from apps.dash.process.routes import RouteProcess

from apps.dash.process.tarif import get_tarif_of_route
from ..models import ResearchReservation
from apps.dash.models import Journey
from apps.dash.serializers import JourneyClassSerializer, CoverCitySerializer, JourneySerializer


class SearchJourneyResultSerializers(serializers.Serializer):
    campanyName = serializers.CharField()
    cars = serializers.CharField()
    journey = JourneySerializer()
    adultPrice = serializers.CharField()
    childPrice = serializers.CharField()
    babyPrice = serializers.CharField()
    total = serializers.CharField()
    journeyClass = JourneyClassSerializer()
    scales = CoverCitySerializer(many=True)
    depart = CoverCitySerializer()
    destination = CoverCitySerializer()


class SearchProcess:
    @classmethod
    def process_data(cls, values: ResearchReservation):
        journies = []
        queryset = cls.get_queryset()
        for journey in queryset:
            jrny: Journey = journey
            price = get_tarif_of_route(jrny.route).filter(
                journey_class=values.journey_class).first()
            # price...
            adult = price.pttc_adulte() * values.adult
            child = price.pttc_child() * values.child
            inch = price.pttc_baby() * values.baby
            total = adult + child + inch

            journies.append({
                "journey": jrny,
                "cars": jrny.cars.codeAppareil,
                "campanyName": jrny.company.nom,
                "adultPrice": f"{adult} {price.devise}",
                "childPrice": f"{child} {price.devise}",
                "babyPrice": f"{inch} {price.devise}",
                "total": f"{total} {price.devise}",
                "journeyClass": values.journey_class,
                "scales": RouteProcess.get_scale(jrny.route),
                "depart": RouteProcess.first(jrny.route),
                "destination": RouteProcess.last(jrny.route),
            })
        return journies

    @classmethod
    def search(cls, values: ResearchReservation):
        return SearchJourneyResultSerializers(cls.process_data(values), many=True).data

    @classmethod
    def get_queryset(cls):
        return Journey.objects.all()