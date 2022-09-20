from rest_framework.test import APITestCase
from case.api import serializers

class GeoJsonSerializer(APITestCase):
    def setUp(self) -> None:
        self.serializer = serializers.GeoJsonSerializer
        self.data = {
            
            "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                    [
                        28.928954601287845,
                        41.046224905995146
                    ],
                    [
                        28.933852314949036,
                        41.046224905995146
                    ],
                    [
                        28.933852314949036,
                        41.04820728726991
                    ],
                    [
                        28.928954601287845,
                        41.04820728726991
                    ],
                    [
                        28.928954601287845,
                        41.046224905995146
                    ]
                    ]
                ]
                }
            }
            ]
        }
    
    def test_serializer(self):
        serializer = self.serializer(data=self.data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.data, self.data)
