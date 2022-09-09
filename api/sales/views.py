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

sales_api = Blueprint('sales', __name__, url_postfix='sales')



@sales_api.route('/productSalesDetail', methods=['GET'])
def productSalesDetail():
    res = {
        "product_name": "Wheat",
        "avg_sale_price_lower": "155.",
        "avg_sale_price_upper": "155.",
        "last_sold_price": "167.50",
        "selling_data": [
            {
                "seller_name": "Surya",
                "quantity": "238273789",
                "price": ""
            },
            {
                "seller_name": "Surya",
                "quantity": "238273789",
                "price": ""
            },
            {
                "seller_name": "Surya",
                "quantity": "238273789",
                "price": ""
            }
        ]

    }
    return success('SUCCESS',res)



  

