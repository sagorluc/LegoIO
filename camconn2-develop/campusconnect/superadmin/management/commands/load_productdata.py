from itertools import product
import json 
import os
from django.apps import apps 
from django.core.management.base import BaseCommand,CommandError
from django.conf import settings
from django.core.management import call_command

file_path = os.path.join(settings.BASE_DIR,'apiv1','data/product-db/')


class Command(BaseCommand):
    help = "Load initial data into database"

    def handle(self, *args, **kwargs):
        call_command('loaddata',file_path+'exp180/exp180.json')
        call_command('loaddata',file_path+'exp180/exp180_serviceoption.json')
        call_command('loaddata', file_path+'coupon_supported_products.json')
        # call_command('loaddata',file_path+'delivery.json')
        # call_command('loaddata',file_path+'/dialogue_cat_list.json')
        # call_command('loaddata',file_path+'/dialogue.json')
        # call_command('loaddata',file_path+'/dialogue_serviceoption.json')
        # call_command('loaddata',file_path+'/dialect_cat_list.json')

        result = {'message':'Successfully Loading initial data'}
        return json.dumps(result)