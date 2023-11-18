import json
from functools import wraps

import jwt
from flask import request, current_app, abort, jsonify
import Database.db_fetch_functions as db_fetch_functions


def secured_endpoint(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "Bearer" not in request.cookies:
            return jsonify(
                message="Bearer Token is missing!",
                error="Unauthorized"
            ), 401
        
        token = request.cookies["Bearer"]
        print(token)
        if not token:
            return jsonify(
                message="Bearer Token is missing!",
                error="Unauthorized"
            ), 401

        print("token is not none")
        try:
            data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            print(data)
            current_user = db_fetch_functions.get_by_id(data["user_id"])
            print(current_user)
            if current_user is None:
                return jsonify(
                    message="Invalid Authentication token!",
                    error="Unauthorized"
                ), 401


        except Exception as e:
            return jsonify(
                message="Unknown error occurred!",
                error=e
            ), 422
        return f(*args, **kwargs)

    return decorated
