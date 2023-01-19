from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

import tushare as ts

app = Flask(__name__)
api = Api(app)
CORS(app,resources=r'/*')


def get_stock_list():
    pro = ts.pro_api()
    # 查询当前所有正常上市交易的股票列表
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    return data.to_json(orient="records", force_ascii=False)


class GetStockList(Resource):
    @staticmethod
    def get():
        return get_stock_list()


api.add_resource(GetStockList, '/api/list')
