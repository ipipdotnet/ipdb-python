import sys
import os
import ipdb
from flask import request
from flask import current_app


def main():
    current_app.logger.info("Received request")
    msg = "\n---HEADERS---\n%s\n---QUERY STRING---\n%s\n\n--BODY--\n%s\n-----\n" % (request.headers, request.query_string, request.get_data())
    current_app.logger.info("request parameter：",msg)
    db= ipdb.Reader(os.path.join(os.path.abspath(os.path.dirname(__file__)),'ipiptest.ipdb'))
    address = request.args.get('address')
    current_app.logger.info("address:",address)
    try:
        info=db.find_info(address)
        retinfo= 'sucess： %s, %s, %s, %s, %s, %s, %s, %s, %s 。' % (info.country_name, info.region_name, info.city_name, info.owner_domain, info.isp_domain, info.latitude,info.longitude, info.timezone, info.utc_offset)
        return retinfo
    except Exception as e:
        retinfo='faild：%s 。' %e
        return retinfo
