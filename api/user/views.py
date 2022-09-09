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

user_api = Blueprint('user', __name__, url_postfix='user')


@user_api.route('/refreshToken', methods=['GET'])
def refreshToken():
    try:
        refresh_token = request.headers['refreshToken']
        # refresh_token = payload["refresh_token"]
        print(refresh_token)
        try:
            payload = jwt.decode(refresh_token, config.SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
        except jwt.ExpiredSignatureError:
            return failure('Authentication timeout', 419)
        except jwt.DecodeError:
            print(traceback.print_exc())
            return failure('Unauthorized', 401)
        except jwt.InvalidTokenError:
            print(traceback.print_exc())
            return failure('Unauthorized', 401)
        user_id = payload['identity']
        if user_id.startswith('TEMP'):
            user_query = TempUser.query.filter_by(user_id=user_id)
        else:
            user_query = User.query.filter_by(id=payload['identity'])
        result = query_list_to_dict(user_query)
        if len(result) > 0:
            payload = payload['identity']
            identity = {'identity': payload, "exp": get_auth_exp(config.JWT_TOKEN_TIME_OUT_IN_MINUTES)}
            token = jwt.encode(identity, config.SECRET_KEY, config.JWT_ALGORITHM)
            tk = token.decode("utf-8")

            refres_identity = {'identity': payload, "exp": get_auth_exp(config.JWT_REFRESH_TOKEN_TIME_OUT_IN_MINUTES)}
            refres_token = jwt.encode(refres_identity, config.SECRET_KEY, config.JWT_ALGORITHM)
            refres_tk = refres_token.decode("utf-8")
            token = {'token': str(tk), 'refresh_token':str(refres_tk)}
            return success('success', token)
        else:
            print("hre")
            return failure('Unauthorized', 401)
    except Exception as err:
        print(traceback.print_exc())
        return failure('Unauthorized', 401)





@user_api.route('/createUserToken', methods=['GET'])
def createUserToken():
    try:
        user_id = request.headers["userId"]
        if user_id == "0":
            uuid = uuid1()
            import time
            ts = int(time.time())
            user_id = "TEMP" + str(uuid) + str(ts)
            userData = TempUser()
            userData.user_id = user_id
            add_item(userData)
        token = createToken(user_id)
        if len(token) > 0:
            return success("Success", token)
        else:
            return failure("Generating token failed",200)
    except Exception as err:
        print(traceback.print_exc())
        return failure('Unauthorized', 401)



@user_api.route('/signUp',methods=['POST'])
def signup():

    try:

        payload = request.get_json()
        email = payload.get('email',None)
        password = payload.get('password',None)
        country_code = payload.get('country_code',None)
        if email and password and country_code:
            is_user_already_exists = User.query.filter_by(email=email).first()
            if not is_user_already_exists:
                user = User(email= email, password=password, country_code = country_code)
                if add_item(user):
                    token = createToken(str(user.id))
                    return success("success",token)
                else:
                    return failure("unable add data")       
            else:
                return failure("Email Already Exists ! ")
        else:
            return failure("missing values in payload")

    except Exception as err:
        print(traceback.print_exc())
        return "fail"



@user_api.route('/login',methods=['POST'])
def signin():

    try:

        payload =  request.get_json()
        email =  payload.get("username",None)
        password = payload.get("password",None)
        if email and password:
            is_valid_email = User.query.filter_by(email=email).first()
            if is_valid_email:
                if is_valid_email.password == password:
                    token = createToken(str(is_valid_email.id))
                    return success("success",token)
                else:
                    return failure("Invalid password")
            else:
                return failure("Invalid email")
        return failure("Invalid payload")
        
    except Exception as err:
        # print(traceback.print_exc())
        return failure(str(err))



@user_api.route('/addProfile',methods=['POST'])
def addProfile():

    try:
        user_id = request.headers.get("userId",None)
        payload = request.get_json()
        if user_id:
            user = User.query.filter_by(id=user_id).first()
            if user:
                first_name = payload.get("first_name",None)
                last_name = payload.get("last_name",None)
                middle_name = payload.get("middle_name",None)
                dob = payload.get("dob",None)
                gender = payload.get("gender",None)
                street_no = payload.get("street_no",None)
                city = payload.get("city",None)
                postal_code = payload.get("postal_code",None)
                country = payload.get("country",None)
                national_number = payload.get("national_number",None)

                if first_name:
                    user.first_name = first_name
                if last_name:
                    user.last_name = last_name
                if middle_name:
                    user.middle_name =  middle_name
                if dob:
                    user.dob = dob
                if gender:
                    user.gender = gender

                if not update_item(user):
                    return failure("unable add the user profile data")
                address =  Address.query.filter_by(user_id= user.id).first()
                if not address:
                    address =  Address()
                    address.user_id = user_id
                    if street_no:
                        address.street = street_no
                    if city:
                        address.city = city
                    if postal_code:
                        address.pincode = postal_code
                    if country:
                        address.country = country
                    if national_number:
                        address.national_number = national_number
                    if not add_item(address):
                        return failure("unable add the user profile data")
                else:
                    if street_no:
                        address.street = street_no
                    if city:
                        address.city = city
                    if postal_code:
                        address.pincode = postal_code
                    if country:
                        address.country = country
                    if national_number:
                        address.national_number = national_number
                    if not update_item(address):
                        return failure("unable add the user profile data")    
                return success("success",[])
        return failure("User not found")
    except Exception as err:
        return failure(str(err))

@user_api.route('/profile')
def getProfile():

    try:
        user_id =  request.headers.get("userId",None)

        if user_id:
            user = User.query.filter_by(id= user_id).first()
            if user:
                res = {}

                res['first_name'] =user.first_name
                res['middle_name'] = user.middle_name
                res['last_name_name'] = user.last_name
                res['dob'] = user.dob
                res['gender'] = user.gender
                res['country_code'] = user.country_code
                res['is_email_verified'] =  True if user.email_verified else False
                res['is_survey_taken'] = True if user.is_survey_taken else False
                res['address'] = {}

                address = Address.query.filter_by(user_id=user_id).first()
                if address:
                    res['address']['city'] = address.city
                    res['address']['street_no'] = address.street
                    res['address']['postal_code'] = address.pincode
                    res['address']['country'] = address.country
                    res['address']['national_number'] = address.national_number
                    
                return success("success",res)
        return failure("Invalid User")
    except Exception as err:
        return failure(str(err))
