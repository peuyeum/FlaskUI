import serial
from lib import cilok,config
from flask import render_template
from flask import Flask,abort,Response
app = Flask(__name__)


def event_tap():
	ser = serial.Serial(config.port, config.baudrate)
	while True:
		data=ser.readline().rstrip('\n')
		data=data.strip()
		yield data
		if data[:1]=="[":
			print "\a"
			trimdata = data.replace(" ","")
			thedata = cilok.urlEncode16(trimdata)
			uri = config.keyuri+'%input%ktp%'+trimdata
			thedata = cilok.urlEncode16(uri)
			yield thedata

@app.route("/tap")
def scan():
	newresponse = Response(event_tap(), mimetype="text/event-stream")
	newresponse.headers.add('Access-Control-Allow-Origin', '*')
	newresponse.headers.add('Cache-Control', 'no-cache')
	return newresponse

@app.route("/")
def index():
	#return "Welcome to Indonesia Electronic KTP Middleware"
	name="ganteng"
	return render_template('index.peuyeum', name=name)

	
@app.route("/<gurih>")
def get(gurih):
	if gurih != cilok.urlDecode16(gurih):
		return "Hash Cilok %s" % cilok.urlDecode16(gurih)
	else:
		abort(401)

