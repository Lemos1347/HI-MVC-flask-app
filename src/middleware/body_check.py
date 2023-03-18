from flask import request
from jsonschema import validate, ValidationError
from functools import wraps

def validate_body(schema):
    def wraper(f):
        @wraps(f)
        def validate_body_function(*args, **kwargs):
            try:
                validate(request.json, schema)
                return f(*args, **kwargs)
            except ValidationError as e:
                return {"error": str(e.message)}, 400
        return validate_body_function
    return wraper

