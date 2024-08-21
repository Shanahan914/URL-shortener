import secrets
import string
from flask import Blueprint, jsonify, request
from .models import Url
from .extensions import db


main = Blueprint('main', __name__)


def generate_short(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))


def generate_unique_short():
    while True:
        candidate = generate_short()
        if not db.session.query(Url).filter_by(shortCode=candidate).first():
            return candidate 
        
def get_url_item(short_code):
    return Url.query.filter(Url.shortCode == short_code).first_or_404()
        

def url_to_json(item):
    return {
        "id": item.id,
        "url": item.url,
        "shortCode": item.shortCode,
        "createdAt": item.created,
        "updated": item.updated
    }


@main.route("/shorten", methods=["POST"])
def create_code():
    data = request.json  
    if 'url' not in data:
        return jsonify ({"message": "you must provide a 'url' field"}), 400   
    
    short_code = generate_unique_short()
    new_url = Url(url=data['url'], shortCode = short_code)
    db.session.add(new_url)
    db.session.commit()
    item = get_url_item(short_code)
    return jsonify(url_to_json(item)), 201


@main.route("/shorten/<short_code>", methods=["GET"])
def get_url(short_code):
    item = get_url_item(short_code)
    item.accessCount = item.accessCount + 1
    db.session.commit()
    return jsonify(url_to_json(item)), 200


@main.route("/shorten/<short_code>", methods=["PUT"])
def update_short(short_code):
    data = request.json
    item = get_url_item(short_code)
    item.url = data.get('url', item.url)
    db.session.commit()
    item = get_url_item(short_code)
    return jsonify(url_to_json(item)), 200
    

@main.route("/shorten/<short_code>", methods=["DELETE"])
def delete_short(short_code):
    item = get_url_item(short_code)
    db.session.delete(item)
    db.session.commit()
    return '', 204   


@main.get("/shorten/<short_code>/stats")
def stats(short_code):
    item = get_url_item(short_code)
    return jsonify(url_to_json(item) |{"accessCount" : item.accessCount}), 200
