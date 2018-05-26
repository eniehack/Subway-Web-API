import falcon
import json
from tinydb import TinyDB, Query

#変数dbにjsonの場所を指定
db = TinyDB('db.json')
table = db.table('subway')

Data = Query()
msg =[]
items = {}
#i = 0


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
                # 1つのデータをディクショナリ化してリストに入れる
                for row in get_data:
                    msg.append({
                        'name': row['name'],
                        'name_en': row['name_en'],
                        'type':  row['type'],
                        'price_regular': row['price_regular'],
                        'price_footlong': row['price_footlong'],
                        'dressing': row['dressing'],
                        'calorie': row['calorie'],
                        'protein': row['protein'],
                        'lipid': row['lipid'],
                        'carbohydrate':  row['carbohydrate'],
                        'sodium':  row['sodium'],
                        'saltEquivalent':  row['saltEquivalent'],
                        'detail': row['detail'],
                        'image_url': row['image_url'],
                    })

                i = 0

                for les in msg:
                    items[i] = les
                    i = i + 1

                # JSON形式でレスポンス
                resp.body = json.dumps(items)
                resp.status = falcon.HTTP_200

            else:
                # nameパラメータのみに値が存在するとき
                # データをDBから取得
                get_data = table.search(Data.name == name)
                # for文を使ってひとつづつデータをJSON形式に整形
                for row in get_data:
                    msg.append({
                        'name': row['name'],
                        'name_en': row['name_en'],
                        'type':  row['type'],
                        'price_regular': row['price_regular'],
                        'price_footlong': row['price_footlong'],
                        'dressing': row['dressing'],
                        'calorie': row['calorie'],
                        'protein': row['protein'],
                        'lipid': row['lipid'],
                        'carbohydrate':  row['carbohydrate'],
                        'sodium':  row['sodium'],
                        'saltEquivalent':  row['saltEquivalent'],
                        'detail': row['detail'],
                        'image_url': row['image_url'],
                    })

                i = 0

                for les in msg:
                    items[i] = les
                    i = i + 1

                # JSON形式でレスポンス
                resp.body = json.dumps(items)
                resp.status = falcon.HTTP_200

        else:
            if types:
                # typeパラメータのみに値が存在するとき
                # データをDBから取得
                get_data = table.search(Data.type == types)
                # for文を使ってひとつづつデータをJSON形式に整形
                for row in get_data:
                    print(row['name'])
                    msg.append({
                        'name': row['name'],
                        'name_en': row['name_en'],
                        'type':  row['type'],
                        'price_regular': row['price_regular'],
                        'price_footlong': row['price_footlong'],
                        'dressing': row['dressing'],
                        'calorie': row['calorie'],
                        'protein': row['protein'],
                        'lipid': row['lipid'],
                        'carbohydrate':  row['carbohydrate'],
                        'sodium':  row['sodium'],
                        'saltEquivalent':  row['saltEquivalent'],
                        'detail': row['detail'],
                        'image_url': row['image_url'],
                    })

                i = 0

                # リストmsg
                for les in msg:
                    items[i] = les
                    i = i + 1

                # JSON形式でレスポンス
                resp.body = json.dumps(items)

            else:
                # パラメータが指定されていない場合、全てのエントリを返す
                # データをDBから取得
                get_data = table.all()
                # for文を使ってひとつづつデータをJSON形式に整形
            for row in get_data:
                msg.append({
                    'name': row['name'],
                    'name_en': row['name_en'],
                    'type':  row['type'],
                    'price_regular': row['price_regular'],
                    'price_footlong': row['price_footlong'],
                    'dressing': row['dressing'],
                    'calorie': row['calorie'],
                    'protein': row['protein'],
                    'lipid': row['lipid'],
                    'carbohydrate':  row['carbohydrate'],
                    'sodium':  row['sodium'],
                    'saltEquivalent':  row['saltEquivalent'],
                    'detail': row['detail'],
                    'image_url': row['image_url'],
                })

            i = 0

            for les in msg:
                items[i] = les
                i = i + 1

                # JSON形式でレスポンス
            resp.body = json.dumps(items)
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