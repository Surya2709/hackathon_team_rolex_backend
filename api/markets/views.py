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
from api.markets.models import Warehouses
from common.connection import  add_item, raw_select, update_item, delete_item
from common.response import success, failure
from flask import request
from api.markets.models import Market
from api.home.models import Category


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

        print(config.SQLALCHEMY_DATABASE_URI)
        market =  Market(name=name,area=area,city=city,state=state,latitude=latitude,longitude=longitude,
                        close_time = closeTime,open_time = openTime, is_open = isOpen )

        if add_item(market):
            return success("success",[])
        return failure("faliure")
    except:
        print(traceback.print_exc())
        return failure("failing")

@market_api.route('/getAllMarkets',methods=['GET'])
def getallMarkets():
    try:
        markets = Market.query.all()
        res = list()
        for market in  markets:
            temp= {}
            temp['name']  =  market.name
            temp['id'] = market.id
            temp['lat'] = market.latitude
            temp['lng'] = market.longitude
            res.append(temp)
        return success("success",res)

    except:
        print(traceback.print_exc())
        return failure("failing")


@market_api.route('/getAllCategory',methods=['GET'])
def getAllCategory():
    try:
        categories = Category.query.all()
        res = list()
        for category in  categories:
            temp= {}
            temp['name']  =  category.name
            temp['id'] = category.id      
            res.append(temp)
        return success("success",res)
    except:
        print(traceback.print_exc())
        return failure("failing")


