#custom  func to deleted array of related caches
import json
import traceback
import logging
from config import log


def delete_related_keys(keys,redis_client):
    """
    deleted related keys in redis and returns the  count
    """
    try:
            
        redis_res = redis_client.keys()
        for key in keys:
            for res in redis_res:
                key_name = res.decode('utf-8')
                if key in key_name:
                    # log.info("deleted ",key_name)
                    redis_client.delete(key_name)
        return True
    except:
        logging.exception(traceback.print_exc())


def delete_order_related_keys(keys_name, user_id, outlet_id, order_type_cache, redis_client):
    """
    deleted order related keys in redis and returns the  count
    """
    try:
        keys = keys_name+'_'+str(user_id)+'_'+str(outlet_id)+'_'+str(order_type_cache).strip()
        #log.info(("keys",keys))
        redis_client.delete(keys)
        return True
    except:
        logging.exception(traceback.print_exc())


def delete_all_keys(redis_client):
    redis_client.execute_command('FLUSHDB ASYNC')
    return True

def get_all_redis_caches(redis_client):
    try:
        redis_res = redis_client.keys()
        redis_server_info = redis_client.execute_command('INFO')['redis_version']
        # log.info(redis_server_info)
        result= []
        
        for res in redis_res:
            obj = {}
            key_name = res.decode('utf-8')
            obj[key_name]=json.loads(redis_client.get(key_name))
            result.append(obj)
        # log.info(result)
        return result,redis_server_info
    except:
        logging.exception(traceback.print_exc())


def get_all_redis_caches_list(redis_client):
    try:

        redis_res = redis_client.keys()
        result= []
        for res in redis_res:
            key_name = res.decode('utf-8')
            result.append(key_name)
        # log.info(result)
        return result
    except:
        logging.exception(traceback.print_exc())