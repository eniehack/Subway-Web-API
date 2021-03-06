import os
import json
import falcon
from tinydb import TinyDB, Query

#変数dbにjsonの場所を指定
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PLACE = os.path.join(BASE_DIR, 'db.json')
db = TinyDB(DB_PLACE)
table = db.table('subway')

Data = Query()
msg =[]
items = {}


class Search():
    '''パラメータを取得し、その条件を満たしたデータだけを返す'''
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

            else:
                # nameパラメータのみに値が存在するとき
                # データをDBから取得
                get_data = table.search(Data.name == name)

        else:
            if types:
                # typeパラメータのみに値が存在するとき
                # データをDBから取得
                get_data = table.search(Data.type == types)

            else:
                # パラメータが指定されていない場合、全てのエントリを返す
                # データをDBから取得
                get_data = table.all()

        # for文を使ってひとつづつデータをJSON形式に整形
        # 条件に合うデータ(商品)の数だけ、データをディクショナリ化。そのディクショナリをリストmsgに入れる
        i = 0

        for row in get_data:
            # 作成されたリストの項だけレスポンス用ディクショナリitemsに挿入し続ける
            items[i] = row
            i = i + 1

        # JSON形式でレスポンス
        resp.body = json.dumps(items)

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