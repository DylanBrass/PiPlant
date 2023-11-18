from functools import wraps

import jwt
from flask import request, current_app, abort
import models
import Database.db_fetch_functions as db_fetch_functions

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Bearer" in request.cookies:
            token = request.cookies["Bearer"]
        if not token:
            return {
                "message": "Bearer Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = db_fetch_functions.get_by_id(data["user_id"])
            if current_user is None:
                return {
                    "message": "Invalid Authentication token!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401
            if not current_user["active"]:
                abort(403)
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500
        current_user[2] = None
        return f(current_user, *args, **kwargs)

    return decorated
