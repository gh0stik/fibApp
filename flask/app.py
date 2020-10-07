import os, redis
from flask import Flask, render_template, request, redirect, url_for, make_response
from db_functions import get_all_values, insert_new_index, create_table
from dotenv import load_dotenv
load_dotenv()

redisHost = os.environ.get("REDIS_HOST")
redisPost = os.environ.get("REDIS_PORT")

r = redis.Redis(host=redisHost, port=redisPost, db=0)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/values/all", methods=["GET"])
def get_all():
    return "{}".format(get_all_values())


@app.route("/values/current", methods=["GET"])
def get_current():
    current = r.pubsub()
    current.subscribe("index")
    try:
        return current.get_message()
    except:
        return None


@app.route("/values", methods=["POST"])
def post_value():
    value = request.form.get("value")
    r.publish('index', value)
    create_table()
    insert_new_index(int(value))
    return render_template('index.html', answer=int(r.hget("index", value)))

if __name__ == "__main__":
    app.run()
