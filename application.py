from datetime import datetime
from requests import Response
from common.response import failure
from common.utils.validator import validateTokens
from factoy import create_app
from config import Config as config
from flask_cors import CORS
from flask import request
from app_whitelist import WHITELISTED


app = create_app()
CORS(app)

@app.before_request
def applicationBeforeRequest():
    """
    MiddleWare
    """
    accessToken = request.environ.get("HTTP_AUTHORIZATION",None)
    requestPath = request.environ.get("PATH_INFO")
    requestUri = request.environ.get("REQUEST_URI")

    
    # print(request)
    # print("********")
    # print(request.environ)
    requestMethod = request.environ.get("REQUEST_METHOD")
    if requestMethod =="OPTIONS":
        return

    if requestPath == "/" or requestPath == "":
        return "welcome"
    overallPath = requestPath.split('/')[-1]
    #for path with args
    subPath = requestPath.split('/')[-2]
    print(overallPath)
    print(subPath)

    if accessToken == 'eyJ0eXAiOiJKV1QiLCPRASHanthGVudGl0eSI6IlRFTVAzODEzODE4MjIxNjI2NjY3OTI1IiwiZXreddyfGiHsHJniGqehU5cUPx':
        return 


    if not (overallPath in WHITELISTED or subPath in WHITELISTED):
        if accessToken:
            isTokenValid,isUserValid, tokenExpired = validateTokens(accessToken)
            if not(isTokenValid and isUserValid) and not tokenExpired: 
                return failure("Invalid Token",status_code=401)
            if tokenExpired:
                return failure("Token Expired", status_code=403)
        else:
            return failure("Token Missing", status_code=403)

@app.after_request
def afterRequest(response):
    """responseModule open for logging"""
    return response

@app.route('/')
def home():
    return 'welcome'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=config.PORT,debug=True)
