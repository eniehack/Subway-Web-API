import falcon
import json
from tinydb import TinyDB, Query

#変数dbにjsonの場所を指定
db = TinyDB('db.json')
table = db.table('subway')


class Search(Object):

    def on_get(self, req, resp):

        # パラメータを取得
        name = req.get_param('name')
        type = req.get_param('type')

        # nameパラメータに値が入っているのかを確認
        if name:
            if type:
                # name,typeパラメータ共に値が存在するとき
                # データをDBから取得
                # for文を使ってひとつづつデータをJSON形式に整形

            else:
                # nameパラメータのみに値が存在するとき
                # データをDBから取得
                # for文を使ってひとつづつデータをJSON形式に整形

        else:
            if type:
                # typeパラメータのみに値が存在するとき
                # データをDBから取得
                # for文を使ってひとつづつデータをJSON形式に整形

            else:
                # パラメータが指定されていない場合、全てのエントリを返す
                # データをDBから取得
                get_data = table.all()
                # for文を使ってひとつづつデータをJSON形式に整形

        # JSON形式でレスポンス
        #resp.body = json.dumps(msg)


class Random(Object):

    def on_get(self, req, resp):

        # 乱数を生成
        # 生成すた乱数番号のメニューのデータをDBから取得
        # for文を使ってひとつづつデータをJSON形式に整形

        # JSON形式でレスポンス
        #resp.body = json.dumps(msg)

app = falcon.API()
app.add_route("/search", Search())
app.add_route("/random", Random())

#table.insert({'name': , 'type': , 'regular_price': , 'long_price': , 'calorie': , 'protein': , 'lipid': , 'carbohydrate'; , 'sodium'; , 'saltEquivalent': , 'description': , 'imageURL': . 'recommend_dressing': })