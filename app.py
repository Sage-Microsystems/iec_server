import os

from flask import Flask, json, request, jsonify
from flask_cors import CORS
from flask_script import Manager, Shell

import requests
import structlog
LOG = structlog.get_logger()

from config import config
from twilio import send_code, verify_code
from model import Voter

registered_voters = []

app = Flask(__name__)
config_name = os.getenv("APP_ENVIRONMENT") or "default"
app.config.from_object(config[config_name])
CORS(app)

def error_response(msg, err):
    return {
        "msg": msg,
        "error": str(err)
    }

@app.route("/verification_start", methods=['POST'])
def start_verification():
    try:
        payload = request.json
        phone_number = payload.get("phoneNumber", "")
        response = send_code(to=phone_number)
        LOG.info(
            "verification code sent successfully"
        )
        
        return jsonify(result=response.json())
    except Exception as e:
        msg = "verification code not sent"
        return jsonify(result=error_response(msg, e))

@app.route("/verification_check", methods=['POST'])
def check_verification():
    try:
        payload = request.json
        phone_number = payload.get("phoneNumber", "")
        verification_code = int(payload.get("verificationCode", "0000"))
        response = verify_code(to=phone_number, code=verification_code)
        LOG.info(
            "phone number verified successfully"
        )

        return jsonify(result=response.json())
    except Exception as e:
        msg = "verfication failed"
        return jsonify(result=error_response(msg, e))

@app.route("/voters", methods=['POST'])
def register_voter():
    try:
        payload = request.json
        voter = Voter(
            fullname=payload.get("fullname", ""),
            gender=payload.get("gender", ""),
            dob=payload.get("dob",""),
            national_id=payload.get("nationalId",""),
            reg_center=payload.get("regCenter",""),
            consitituency=payload.get("constituency",""),
            district=payload.get("district")
        )
        global registered_voters 
        registered_voters.append(voter)

        return jsonify(result=voter.to_json())
    except Exception as e:
        msg = "registration was unsuccessful"
        return jsonify(result=error_response(msg, e))

@app.route("/voters", methods=['GET'])
def get_voters():
    try:
        global registered_voters
        voters = [v.to_json() for v in registered_voters]
        return jsonify(result=voters)
    except Exception as e:
        msg = "failed fetching voters"
        return jsonify(result=error_response(msg, e))

def make_shell_context():
    return dict(
        app=app,
    )

manager = Manager(app)
manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == "__main__":
    manager.run()
