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

home_api = Blueprint('home', __name__, url_postfix='home')


@home_api.route('/getOverViewData', methods=['GET'])
def getOverViewData():


    res = {

        "head_card" : {

        "market_id":"euyie4djeidjoedie-0343434",
        "total_sales" : 10000,
        "total_expenses" : 100,
        "total_products" : 100,
        "todays_sales" :100 ,

        }


        }

    return res