from gzip import READ
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

product_api = Blueprint('product', __name__, url_postfix='product')


@product_api.route('/topSellingProductPredictionGraph', methods=['GET'])
def topSellingProductPredictionGraph():

    graph = [
      {
        "time" : "8:00",
        "avg_price" : "40"
      },
       {
        "time" : "9:00",
        "avg_price" : "42",
      }, {
        "time" : "10:00",
        "avg_price" : "45",
      }, {
        "time" : "11:00",
        "avg_price" : "44",
      }, {
        "time" : "12:00",
        "avg_price" : "41",
      }, {
        "time" : "1:00",
        "avg_price" : "38",
      }, {
        "time" : "2:00",
        "avg_price" : "39",
      }, {
        "time" : "3:00",
        "avg_price" : "43",
      }, {
        "date_time" : "4:00",
        "avg_price" : "48",
      },  {
        "time" : "5:00",
        "avg_price" : "50",
      }, {
        "time" : "6:00",
        "avg_price" : "43",
      }, {
        "time" : "7:00",
        "avg_price" : "42",
      }, {
        "time" : "8:00",
        "avg_price" : "47",
      }
      ]


    res = {
    "prodcut_name" : "Wheat",
    "market_id" : "skdj9932-0wl-3o2=w=3-",
    "market_name" : "chickpet",
    "data" : graph
    
     }

    return success("Success", res)



@product_api.route('/getTopSellingProducts', methods=['GET'])
def getTopSellingProducts():

    res = {
        "columns" : [
        {
            "title": "sample",
            "dataIndex": "img",
            "key": "img",
            "width": "100px"
        },
        {
            "title": "Product Name",
            "dataIndex": "name",
            "key": "name"
        },
        {
            "title": "Category",
            "dataIndex": "category",
            "key": "category"
        },
        {
            "title": "Sub Category",
            "dataIndex": "subcategory",
            "key": "subcategory"
        },
        {
            "title": "Price",
            "dataIndex": "price",
            "key": "price"
        },
        {
            "title": "Sold",
            "dataIndex": "sold",
            "key": "sold"
        }
        ],
        "data": [
        {
            "img": "https://stylesatlife.com/wp-content/uploads/2018/05/cabbage-benefits.jpg.webp",
            "name": "Cabbage",
            "category": "Vegetable",
            "subcategory": "Green Vegetable",
            "price": "$0.5",
            "sold": "$1.3"
        },
        {
            "img": "https://5.imimg.com/data5/AK/RA/MY-68428614/apple-250x250.jpg",
            "name": "Apple",
            "category": "Fruit",
            "subcategory": "",
            "price": "$1.8",
            "sold": "$2.1"
        },
        {
            "img": "https://cdn.shopify.com/s/files/1/0592/9884/0756/products/Bangalorebluegrapes_9a4f5dc4-c11f-4bb7-802a-834bd86652c6_300x.jpg?v=1653647503",
            "name": "Grapes",
            "category": "Fruit",
            "subcategory": "Black",
            "price": "$2.2",
            "sold": "$2.3"
            }
            ]
        }
    return success("success", res)
