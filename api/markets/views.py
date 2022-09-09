import traceback
from uuid import uuid1
import jwt
from config import Config as config
from common.utils.time_utils import get_auth_exp,createToken
from common.blueprint import Blueprint
from common.utils.json_utils import query_list_to_dict
from api.user.models import  User, Address, TempUser
from api.markets.models import Warehouses
from common.connection import  add_item, raw_select, update_item, delete_item
from common.response import success, failure
from flask import request, jsonify

market_api = Blueprint('market', __name__, url_postfix='market')



@market_api.route('/getNearbyMarket', methods=['GET'])
def getNearbyMarket():


    res = {
            "nearby_markets": [
                {
                "lat": "70",
                "lng": "80",
                "distance": "4.1",
                "opening_time": "8:00pm",
                "is_open": True,
                "market_name": "Shivaji Nagar",
                "market_id": "ksdioiw-02ow-20wo2-w2-w0w2-0w",
                "products": [
                    {
                    "product_name": "wheat",
                    "product_id": "i3iii3434343409343ewpewopie3"
                    },
                    {
                    "product_name": "wheat",
                    "product_id": "i3iii3434343409343ewpewopie3"
                    }
                ]
                },
                {
                "lat": "70",
                "lng": "80",
                "distance": "4.1",
                "opening_time": "8:00pm",
                "is_open": True,
                "market_name": "Shivaji Nagar",
                "market_id": "ksdioiw-02ow-20wo2-w2-w0w2-0w",
                "products": [
                    {
                    "product_name": "wheat",
                    "product_id": "i3iii3434343409343ewpewopie3"
                    },
                    {
                    "product_name": "wheat",
                    "product_id": "i3iii3434343409343ewpewopie3"
                    }
                ]
                },
                {
                "lat": "70",
                "lng": "80",
                "distance": "4.1",
                "opening_time": "8:00pm",
                "is_open": True,
                "market_name": "Shivaji Nagar",
                "market_id": "ksdioiw-02ow-20wo2-w2-w0w2-0w",
                "products": [
                    {
                    "product_name": "wheat",
                    "product_id": "i3iii3434343409343ewpewopie3"
                    },
                    {
                    "product_name": "wheat",
                    "product_id": "i3iii3434343409343ewpewopie3"
                    }
                ]
                }
            ]
            }


    return success("success", res)

@market_api.route('/addWarehouses', methods=['POST'])
def addWarehouses():

    try:
        payload = request.get_json()
        name = payload.get("name",None)
        area = payload.get("area",None)
        city = payload.get("city",None)
        state = payload.get("state",None)
        longitude = payload.get("longitude",None)
        latitude = payload.get("latitude",None)
        open_time = payload.get("open_time",None)
        close_time = payload.get("close_time",None)
        is_open = payload.get("is_open",None)
    
        Warehouse =  Warehouses(name = name, area = area, city = city, state = state, longitude = longitude, latitude = latitude, open_time = open_time, close_time = close_time, is_open = is_open)

        if add_item(Warehouse):
            return success

    except:
        print(traceback.print_exc)
        return failure
