#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request
import random

blueprint = Blueprint('base', __name__, template_folder='templates')

barometerData = [str(x) + " inHg" for x in range(28, 32)]
gpsData = ["30.444899, -84.299797", "30.444890, -84.299771", "30.444890, -84.299722", "30.444881, -84.299666", "30.444890, -84.299722", "30.444862, -84.299592", "30.444870, -84.299518", "30.444915, -84.299455", "30.444945, -84.299423", "30.444890, -84.299722", "30.445021, -84.299296", "30.445037, -84.299254", "30.445023, -84.299214", "30.445013, -84.299183", "30.445022, -84.299223", "30.445011, -84.299178", "30.444890, -84.299722", "30.445003, -84.299179", "30.445013, -84.299222", "30.444996, -84.299187", "30.445004, -84.299232", "30.444933, -84.299261", "30.444906, -84.299269", "30.444801, -84.299296", "30.444744, -84.299301", "30.444655, -84.299289", "30.444528, -84.298967", "30.444423, -84.298691", "30.444373, -84.298522", "30.444321, -84.298411", "30.444890, -84.299722", "30.444495, -84.298918", "30.444576, -84.299140", "30.444731, -84.299265", "30.444937, -84.299194", "30.445026, -84.299179", "30.445117, -84.299432", "30.445164, -84.299647", "30.445187, -84.299801", "30.445233, -84.299933", "30.445286, -84.300088", "30.445284, -84.300183", "30.445197, -84.300293", "30.445078, -84.300177", "30.445009, -84.299936", "30.444928, -84.299762"]
temperatureData = [str(x) + "˚ F" for x in range(75, 77)]
windData = [str(speed) + " MPH " + direction for speed in range(1, 4) for direction in ["North", "West"]] + ["0 MPH"]

@blueprint.route('/')
def index():
    return render_template('index.html')

@blueprint.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')

###

@blueprint.route('/temperature')
def temperature():
	spot = int(request.args.get('n'))
	return temperatureData[random.randint(0, len(temperatureData) - 1)]

@blueprint.route('/gps')
def gps():
	spot = int(request.args.get('n'))
	if spot < 0:
		spot *= -1
	if spot > len(gpsData) - 1:
		spot = spot % (len(gpsData) - 1)
	return gpsData[spot]

@blueprint.route('/barometer')
def barometer():
	return barometerData[random.randint(0, len(barometerData) - 1)]

@blueprint.route('/wind')
def wind():
	return windData[random.randint(0, len(windData) - 1)]