from doctest import REPORT_UDIFF
from random import lognormvariate
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
from api.markets.models import Market


market_api = Blueprint('market', __name__, url_postfix='market')



@market_api.route('/getNearbyMarket', methods=['POST'])
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



@market_api.route('/addMarket',methods=['POST'])
def addMarket():


    try:
        payload = request.get_json()
        name =  payload.get('name',None)
        area = payload.get('area',None)
        city = payload.get('city',None)
        latitude = payload.get('latitude',None)
        longitude = payload.get('longitude',None)
        closeTime = payload.get('closeTime',None)
        openTime = payload.get('open_time',None)
        isOpen = payload.get('is_open',None)
        state = payload.get('state',None)

        market =  Market(name=name,area=area,city=city,state=state,latitude=latitude,longitude=longitude,
                        close_time = closeTime,open_time = openTime, is_open = isOpen )

        if add_item(market):
            return success("success",[])
        return failure("faliure")
    except:
        print(traceback.print_exc())
        return failure("failing")