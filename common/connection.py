from inspect import trace
import traceback
from sqlalchemy import text
import logging
from config import db
from config import Config as config


def add_item(obj):
    try:
        db.session.add(obj)
        db.session.commit()
        return obj
    except Exception as err:
        # log.info("add_item", err)
        # db.session.rollback()
        # log.exception(traceback.print_exc())
        return None
    # finally:
    #     db.session.close()


def get_item(*args):
    try:
        result = db.session.query(*args)
        return result
    except Exception as err:
        # log.info("add_item", err)
        return None
    # finally:
    #     db.session.close()


def update_item(obj):
    try:
        db.session.commit()
        return obj
    except Exception as err:
        # db.session.rollback()
        # log.info("update_item", err)
        # print(traceback.print_exc())
        return None
    # finally:
    #     db.session.close()


def delete_item(obj):
    try:
        db.session.delete(obj)
        db.session.commit()
        return obj
    except Exception as err:
        # db.session.rollback()
        # log.info("delete_item", err)
        return None
    # finally:
    #     db.session.close()


def raw_select(sql):
    try:
        result_proxy = raw_execution(sql)
        result = []
        for row in result_proxy:
            row_as_dict = dict(row)
            date_ = row_as_dict.values()
            result.append(row_as_dict)
        result_proxy.close()
        return result
    except Exception as err:
        # logging.exception(traceback.print_exc())
        # print(traceback.print_exc())
        return []


def raw_execution(sql):
    try:
        result = db.engine.execute(text(sql).execution_options(autocommit=True))
        return result
    except Exception as err:
        # log.exception(traceback.print_exc())
        print(traceback.print_exc())
        return None


def get_count(sql):
    try:
        result = db.engine.execute(sql)
        one_row = result.fetchone()
        return one_row[0]
    except Exception as err:
        # log.info("raw_execution", str(err))
        return None



def raw_execution_replica(sql):
    try:
        result = config.READ_REPLICA_ENGINE.execute(text(sql).execution_options(autocommit=True))
        return result
    except Exception as err:
        # print(traceback.print_exc())
        return None


# def raw_select_read_replica(sql):
#     try:
#         result_proxy = raw_execution(sql)
#         result = []
#         for row in result_proxy:
#             row_as_dict = dict(row)
#             date_ = row_as_dict.values()
#             result.append(row_as_dict)
#         result_proxy.close()
#         return result
#     except Exception as err:
#         # logging.exception(traceback.print_exc())
#         return []
