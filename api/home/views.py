import traceback
from uuid import uuid1
import jwt
from config import Config as config
from common.utils.time_utils import get_auth_exp,createToken
from common.blueprint import Blueprint
from common.utils.json_utils import query_list_to_dict
from api.user.models import  User, Address, TempUser
from common.connection import  add_item, raw_select, update_item, delete_item
from common.response import success, failure
from flask import request
import json

home_api = Blueprint('home', __name__, url_postfix='home')


@home_api.route('/getOverViewData', methods=['GET'])
def getOverViewData():
    try:

        lat = request.args['lat']
        long = request.args['lng']
        from math import radians
        lat1 = radians(float(lat))
        lon1 = radians(float(long))
        distance = '(6371.01 * (2 * atan2(sqrt((power(sin((radians(latitude::float) - ' + \
            str(lat1) + ') / 2),2) + cos(' + str(lat1) + ') * cos(radians(latitude::float)) * \
                power(sin((radians(longitude::float) - ' + str(lon1) + ') / 2),2))), sqrt(1 - \
                    (power(sin((radians(latitude::float) - ' + str(lat1) + ') / 2),2) + cos(' + str(lat1) + ') \
                        * cos(radians(latitude::float)) * power(sin((radians(longitude::float) - ' + str(lon1) + ') / 2)\
                            ,2))))))'
        time = '((' + distance + '/ 20) * 60)'

    
        outlet_query = "SELECT *," + distance + " as distance," + time + " as time from market where deleted_at IS " \
                                                                                "Null ORDER BY distance ASC LIMIT 1" 
        print(outlet_query)
        results = raw_select(outlet_query)

        res = {}
        if len(results):
            result =  results[0]

            available_product_query =  raw_select(f"select p.name,p.id from product_market_mapping pm inner join product p on p.id=pm.product_id where pm.market_id='{result['id']}'")

            if not len(available_product_query)>0:
                available_product_query =[]
            else:
                bres= []
                for available_product in available_product_query:
                    temp= {}
                    temp['name'] = available_product['name']
                    temp['id'] = available_product['id']


            res = {

                "head_card" : {
                "available_products" : available_product_query,
                "market_name" : result['name'],
                "market_id": result['id'],
                "total_sales" :4450,
                "total_expenses" : 222.5,
                "total_profit" :2057.5,
                "total_products" : 89,
                "todays_sales" :2280 ,
                }
                }
        return success("success",res)
    except:
        print(traceback.print_exc())
        return failure("failed")