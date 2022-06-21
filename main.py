from flask import*
from mathi import mathi
import numpy as np
app=Flask(__name__)
app.register_blueprint(mathi)



app.run(debug=True,port="5002")

if __name__=='__main__':
	app.run()
