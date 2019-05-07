import sqlite3
from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/')
def print_items():

    conn = sqlite3.connect('analytics.db')

    cur_analytics = conn.cursor()
    cur_labs = conn.cursor()
    cur_docs = conn.cursor()
    cur_music = conn.cursor()

    cur_analytics = cur_analytics.execute("select * from monitor where type = 'analytics' order by 1 desc limit 5")
    cur_labs = cur_labs.execute("select * from monitor where type = 'labs' order by 1 desc limit 5")
    cur_docs = cur_docs.execute("select * from monitor where type = 'docs' order by 1 desc limit 5")
    cur_music = cur_music.execute("select * from monitor where type = 'music' order by 1 desc limit 5")

    return render_template(
                            'index.html',
                            list_a = cur_analytics.fetchall(),
                            list_b = cur_labs.fetchall(),
                            list_c = cur_docs.fetchall(),
                            list_d = cur_music.fetchall()
                           )
    conn.close()

if __name__ == "__main__":
    app.run(debug=True)




