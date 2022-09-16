from case.api.models import UserCredential
from sentinelsat import SentinelAPI, geojson_to_wkt
from case.api.exceptions import RequestExceptions

class ImageService:
    def get_images(self, user, image_id=None, **kwargs):
        user_credentials = self.get_user_credentials(user)
        username = user_credentials['username']
        password = user_credentials['password']
        try:
            api = SentinelAPI(username, password)
            if image_id:
                return api.get_product_odata(image_id)
            data = {}
            footprint = geojson_to_wkt(kwargs)
            products = api.query(footprint,
                                producttype='SLC',
                                orbitdirection='ASCENDING',
                                limit=10)                        
            images = api.to_geojson(products)
            for image in images['features']:
                properties = image['properties']
                data.update({
                    properties['title']: {'id': properties['id'], 'image_url': properties['link_icon']}
                }) 
            return data
        except Exception:
            raise RequestExceptions

    def get_user_credentials(self, user):
        return UserCredential.objects.get(user=user).credentials
         