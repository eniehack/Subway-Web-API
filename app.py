import falcon
import json
from tinydb import TinyDB, Query

#変数dbにjsonの場所を指定
db = TinyDB('db.json')
table = db.table('subway')

Data = Query()
msg ={}


class Search():

    def on_get(self, req, resp):

        # パラメータを取得
        name = req.get_param('name')
        types = req.get_param('type')

        # nameパラメータに値が入っているのかを確認
        if name:
            if types:
                # name,typeパラメータ共に値が存在するとき
                # データをDBから取得
                get_data = table.search((Data.name == name) & (Data.type == types))
                # for文を使ってひとつづつデータをJSON形式に整形
                for row in get_data:
                    msg['name'] = row['name']
                    msg['name_en'] = row['name_en']
                    msg['type'] = row['type']
                    msg['price_regular']= row['price_regular']
                    msg['price_footlong'] = row['price_footlong']
                    if row['dressing']:
                        msg['dressing'] = row['dressing']
                    msg['calorie'] = row['calorie']
                    msg['protein'] = row['protein']
                    msg['lipid'] = row['lipid']
                    msg['carbohydrate'] = row['carbohydrate']
                    msg['sodium'] = row['sodium']
                    msg['saltEquivalent'] = row['saltEquivalent']
                    msg['detail'] = row['detail']
                    msg['image_url'] = row['image_url']
                    # JSON形式でレスポンス
                    resp.body = json.dumps(msg)
                    resp.status = falcon.HTTP_200

            else:
                # nameパラメータのみに値が存在するとき
                # データをDBから取得
                get_data = table.search(Data.name == name)
                # for文を使ってひとつづつデータをJSON形式に整形
                for row in get_data:
                    msg['name'] = row['name']
                    msg['name_en'] = row['name_en']
                    msg['type'] = row['type']
                    msg['price_regular']= row['price_regular']
                    msg['price_footlong'] = row['price_footlong']
                    if row['dressing']:
                        msg['dressing'] = row['dressing']
                    msg['calorie'] = row['calorie']
                    msg['protein'] = row['protein']
                    msg['lipid'] = row['lipid']
                    msg['carbohydrate'] = row['carbohydrate']
                    msg['sodium'] = row['sodium']
                    msg['saltEquivalent'] = row['saltEquivalent']
                    msg['detail'] = row['detail']
                    msg['image_url'] = row['image_url']
                    # JSON形式でレスポンス
                    resp.body = json.dumps(msg)
                    resp.status = falcon.HTTP_200

        else:
            if types:
                # typeパラメータのみに値が存在するとき
                # データをDBから取得
                get_data = table.search(Data.type == types)
                # for文を使ってひとつづつデータをJSON形式に整形
                for row in get_data:
                    msg['name'] = row['name']
                    msg['name_en'] = row['name_en']
                    msg['type'] = row['type']
                    msg['price_regular']= row['price_regular']
                    msg['price_footlong'] = row['price_footlong']
                    if row['dressing']:
                        msg['dressing'] = row['dressing']
                    msg['calorie'] = row['calorie']
                    msg['protein'] = row['protein']
                    msg['lipid'] = row['lipid']
                    msg['carbohydrate'] = row['carbohydrate']
                    msg['sodium'] = row['sodium']
                    msg['saltEquivalent'] = row['saltEquivalent']
                    msg['detail'] = row['detail']
                    msg['image_url'] = row['image_url']
                    # JSON形式でレスポンス
                    resp.body = json.dumps(msg)
                    resp.status = falcon.HTTP_200

            else:
                # パラメータが指定されていない場合、全てのエントリを返す
                # データをDBから取得
                get_data = table.all()
                # for文を使ってひとつづつデータをJSON形式に整形
                for row in get_data:
                    msg['name'] = row['name']
                    msg['name_en'] = row['name_en']
                    msg['type'] = row['type']
                    msg['price_regular']= row['price_regular']
                    msg['price_footlong'] = row['price_footlong']
                    if row['dressing']:
                        msg['dressing'] = row['dressing']
                    msg['calorie'] = row['calorie']
                    msg['protein'] = row['protein']
                    msg['lipid'] = row['lipid']
                    msg['carbohydrate'] = row['carbohydrate']
                    msg['sodium'] = row['sodium']
                    msg['saltEquivalent'] = row['saltEquivalent']
                    msg['detail'] = row['detail']
                    msg['image_url'] = row['image_url']

                    # JSON形式でレスポンス
                    resp.body = json.dumps(msg)
                    resp.status = falcon.HTTP_200

'''
class Random(Object):

    def on_get(self, req, resp):

        # 乱数を生成
        # 生成すた乱数番号のメニューのデータをDBから取得
        # for文を使ってひとつづつデータをJSON形式に整形

        # JSON形式でレスポンス
        resp.body = json.dumps(msg)
'''
app = falcon.API()
app.add_route("/search", Search())
# app.add_route("/random", Random())

if __name__ == "__main__":
    from wsgiref import simple_server

    httpd = simple_server.make_server("127.0.0.1", 8008, app)
    httpd.serve_forever()