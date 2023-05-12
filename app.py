from flask import Flask, render_template
import json

app = Flask(__name__)

s='{"nowonair_list":{"g1":{"previous":{"id":"2023051118707","event_id":"18707","start_time":"2023-05-11T16:10:00+09:00","end_time":"2023-05-11T16:15:00+09:00","area":{"id":"130","name":"東京"},"service":{"id":"g1","name":"ＮＨＫ総合１","logo_s":{"url":"//www.nhk.or.jp/common/img/media/gtv-100x50.png","width":"100","height":"50"},"logo_m":{"url":"//www.nhk.or.jp/common/img/media/gtv-200x100.png","width":"200","height":"100"},"logo_l":{"url":"//www.nhk.or.jp/common/img/media/gtv-200x200.png","width":"200","height":"200"}},"title":"きょうの料理ビギナーズ （５）ご飯のおとも カレー鶏そぼろ","subtitle":"つくりおきができる便利な「ご飯のおとも」は、ひとりごはんの強い味方です。カレー風味が食欲をそそる「カレー鶏そぼろ」、トロッとした「塩こぶなめたけ」を紹介します","genres":["0205","1015"]},"present":{"id":"2023051121675","event_id":"21675","start_time":"2023-05-11T16:15:00+09:00","end_time":"2023-05-11T17:00:00+09:00","area":{"id":"130","name":"東京"},"service":{"id":"g1","name":"ＮＨＫ総合１","logo_s":{"url":"//www.nhk.or.jp/common/img/media/gtv-100x50.png","width":"100","height":"50"},"logo_m":{"url":"//www.nhk.or.jp/common/img/media/gtv-200x100.png","width":"200","height":"100"},"logo_l":{"url":"//www.nhk.or.jp/common/img/media/gtv-200x200.png","width":"200","height":"200"}},"title":"あしたが変わるトリセツショー 正しい保湿術！冬の乾燥に負けないかゆみ撃退法","subtitle":"乾燥肌によるかゆみにお悩みのあなたへ、ＭＣ石原さとみが“正しい保湿術”をお届け！皮膚科医推薦！お肌に浸透し水分量をアップさせる保湿剤の塗り方「３Ｔ塗り」とは？","genres":["0515","0203","0205"]},"following":{"id":"2023051118710","event_id":"18710","start_time":"2023-05-11T17:00:00+09:00","end_time":"2023-05-11T18:00:00+09:00","area":{"id":"130","name":"東京"},"service":{"id":"g1","name":"ＮＨＫ総合１","logo_s":{"url":"//www.nhk.or.jp/common/img/media/gtv-100x50.png","width":"100","height":"50"},"logo_m":{"url":"//www.nhk.or.jp/common/img/media/gtv-200x100.png","width":"200","height":"100"},"logo_l":{"url":"//www.nhk.or.jp/common/img/media/gtv-200x200.png","width":"200","height":"200"}},"title":"ニュースＬＩＶＥ！ゆう５時「相撲部」があります","subtitle":"▽令和初「春の園遊会」車いすテニス国枝慎吾さんら招待 ▽大谷翔平選手の「ホームランかぶと」すべて手作業の工房 ▽大相撲夏場所へ「北青鵬」に注目 ＃君の声","genres":["0000","0202","0205"]}}}}'
#print(s)
deta = json.loads(s)
print(deta["nowonair_list"]["g1"]["previous"])
@app.route("/")
def index():
    #return render_template('index.html', x = 20)
    return render_template('index.html',time="開始時刻",title="タイトル")
@app.route("/style.css")
def html():
    return render_template("style.css")

if __name__ == "__main__":
    app.run()