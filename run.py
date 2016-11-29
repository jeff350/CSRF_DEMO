#!/usr/bin/env python
from app import app
from flask_debug import Debug
Debug(app)
app.run(host='0.0.0.0', debug=True)
