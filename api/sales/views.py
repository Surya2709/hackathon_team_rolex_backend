from audioop import add
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
from api.sales.models import Sales


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



@sales_api.route('/addProductSalesDetails', methods=['POST'])
def addProductSalesDetails():

    try:
        
        payload = request.get_json()
        marketId =  payload['market_id']
        productId = payload['product_id']
        userId = payload['user_id']
        quantity = payload['quantity']
        purchase_vlaue = payload['purchase_value']
        salesDetail =  Sales()
        salesDetail.market_id = marketId
        salesDetail.product_id = productId
        salesDetail.quantity =  quantity
        salesDetail.user_id = userId
        salesDetail.purchase_value = purchase_vlaue
        if add_item(salesDetail):
            return success("success",[])
        return failure("failure")
    except:
        return failure("failure")




@sales_api.route('/predict', methods=['GET'])
def predict():
    from ml.main import predict

    results = predict()
    json_res = results.to_dict()
    print(json_res)


    # print(res.head())


    {
      "date_time" : "01/12/2022 00:00:00",
      "avg_price" : "120",
      "orders" : "24",
    },

    return success("success",[])

    