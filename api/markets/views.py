from doctest import REPORT_UDIFF
from random import lognormvariate, randint
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
from api.home.models import Category, Product
from api.products.models import ProductMarketMapping


market_api = Blueprint('market', __name__, url_postfix='market')



@market_api.route('/getNearbyMarket', methods=['POST'])
def getNearbyMarket():
    try:
        payload = request.get_json()

        lat = payload['lat']
        long = payload['lng']
        product_id = payload['product_id']


        from math import radians
        lat1 = radians(lat)
        lon1 = radians(long)

        distance = '(6371.01 * (2 * atan2(sqrt((power(sin((radians(latitude::float) - ' + str(lat1) + ') / 2),2) + cos(' + str(lat1) + ') * cos(radians(latitude::float)) * power(sin((radians(longitude::float) - ' + str(lon1) + ') / 2),2))), sqrt(1 - (power(sin((radians(latitude::float) - ' + str(lat1) + ') / 2),2) + cos(' + str(lat1) + ') * cos(radians(latitude::float)) * power(sin((radians(longitude::float) - ' + str(lon1) + ') / 2),2))))))'
        time = '((' + distance + '/ 20) * 60)'

    
        outlet_query = "SELECT *," + distance + " as distance," + time + " as time from market where deleted_at IS " \
                                                                                "Null ORDER BY distance ASC LIMIT 4" 
        print(outlet_query)
        results = raw_select(outlet_query)

        out =[]
        graph = [
        {
            "time" : "8:00",
            "avg_price" : randint(40,70)
        },
        {
            "time" : "9:00",
            "avg_price" : randint(40,70),
        }, {
            "time" : "10:00",
            "avg_price" : randint(40,70),
        }, {
            "time" : "11:00",
            "avg_price" :  randint(40,70),
        }, {
            "time" : "12:00",
            "avg_price" :  randint(40,70),
        }, {
            "time" : "1:00",
            "avg_price" :  randint(40,70),
        }, {
            "time" : "2:00",
            "avg_price" :  randint(40,70),
        }, {
            "time" : "3:00",
            "avg_price" :  randint(40,70),
        }, {
            "date_time" : "4:00",
            "avg_price" :  randint(40,70),
        },  {
            "time" : "5:00",
            "avg_price" :  randint(40,70),
        }, {
            "time" : "6:00",
            "avg_price" : randint(40,70),
        }, {
            "time" : "7:00",
            "avg_price" : randint(40,70),
        }, {
            "time" : "8:00",
            "avg_price" :  randint(40,70),
        }
        ]

        productName =  ""
        productId = ""
        productData = Product.query.filter_by(id=product_id ).first()
        if productData:
            productName =  productData.name
            productId = productData.id

        if len(results)>0:
            for result in results:
                temp = {}
                temp['market_name'] = result['name']
                temp['market_id'] = result['id']
                temp['lat']  = result['latitude']
                temp['lng'] = result['longitude']
                temp['distance'] = result['distance']
                temp['opening_time'] = result['open_time']
                temp['is_open'] = result['is_open']
                temp['prediction'] = graph
                temp['product_name'] = productName
                temp['product_id'] =  productId
                out.append(temp)
        return success("success", out)
    except:
        print(traceback.print_exc())
        return failure("failed")


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
    
        warehouse =  Warehouses(name = name, area = area, city = city, 
        state = state, longitude = longitude, latitude = latitude, open_time = open_time,
         close_time = close_time, is_open = is_open)

        if add_item(warehouse):
            return success("success",[])
        return failure("faliure")

    except:
        print(traceback.print_exc())
        return failure("failing")



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





