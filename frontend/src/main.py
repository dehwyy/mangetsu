from flask import Flask, render_template, redirect, request
from api.request_builder import RequestBuilder
from api.shikimori import ShikimoriOrderBy

app = Flask(__name__)

def main():

  app.run(port=7788, host='127.0.0.1')


class Routes:
  @app.route("/")
  def index():
    return render_template("index.html")

  @app.route("/animes")
  def animes():
    query = request.args.get("search")
    query = query if query else ""
    animes = RequestBuilder().shikimori().with_query(query).with_order_by(ShikimoriOrderBy.Rank).with_limit(10).finish().animes()

    return render_template("animes.html", animes=animes, query=query)

  @app.route('/users')
  def users():
    # perform api request
    users = [
      {"username": "dehwyy", "picture": "https://sun9-77.userapi.com/impg/HJquvixJDUoQ1Z78ZHfU_kr-w9Lf0yamaP-DCQ/VDPE0j1FlhU.jpg?size=900x1600&quality=95&sign=f5ed202bcf80d5002f0c89bcfd79d523&type=album"},
      {"username": "Waypo1nt", "picture": "https://avatars.githubusercontent.com/u/103949460?s=400&u=a0c696f5c8881967fcab5516e90bf04d4fd423a4&v=4"}
    ]
    return render_template("users.html", users=users)

  @app.route("/user/<username>")
  def user(username: str):
    # perfrom api request
    return render_template("user.html", username=username)

  @app.route("/api/oauth2/github")
  def github():
    return redirect("/")


if __name__ == '__main__':
  main()
