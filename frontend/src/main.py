from flask import Flask, render_template

app = Flask(__name__)

def main():

  app.run(port=7788, host='127.0.0.1')


class Routes:
  @app.route("/")
  def index():
    return render_template("index.html")


if __name__ == '__main__':
  main()
