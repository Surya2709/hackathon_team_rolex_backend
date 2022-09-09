import re
from config import Config as config
import jwt
import traceback
from common.connection import raw_select

def is_mobile_no(mobile_no):
    try:
        if re.match(r'[6789]\d{9}$', mobile_no):
            return True
        else:
            return False
    except Exception as err:
        return False


def is_email_id(email_id):
    try:
        if re.match(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', email_id, re.I):
            return True
        else:
            return False
    except Exception as err:
        return False


def is_valid_password(password):
    try:
        password = str(password)

        # todo rule to be added
        if not password:
            return False
        else:
            return True
    except Exception as err:
        return False

# def googleAuthCheckVal(id):
#     content = {}
#     content["user_id"] = id
#     url = str(config.APP_BASE_URL) + 'api/v1/user/verifyApiUser'
#     headers = {
#         "Content-Type": "application/json",
#     }
#     data = {"positions": [0, 6, 7, 29]}
#     # log.info(content)
#     r = requests.post(url, json=content, headers=headers)
#     # log.info("google auth check response")
#     res = r.json()
#     #log.info(res)
#     # log.info(res)
#     if res["error"] == 0:
#         return res["content"]["status"]
#     else:
#         return 0


def validateTokens(token):
        try:
            payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
            # print(payload)
            is_authorised = authenticatedUser(payload['identity'])
            return True, is_authorised , False
        except Exception as err:
            # print("unauth user falling here")
            return False, None, True

def authenticatedUser(user_id):
    if 'TEMP' in  user_id:
        validate_query = f"select id from temp_user where user_id='{user_id}'"
        return True if raw_select(validate_query) else False
    validate_query = f"select id from user_data where id='{user_id}'"
    return True if raw_select(validate_query) else False
        
