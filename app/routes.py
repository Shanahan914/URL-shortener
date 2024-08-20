from flask import Blueprint, jsonify, request
from .models import Url
from .extensions import db
import secrets
import string

main = Blueprint('main', __name__)


def generate_short(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))


def generate_unique_short():
    while True:
        candidate = generate_short()
        if not db.session.query(Url).filter_by(shortCode=generate_short()).first():
            return candidate 


# post -> create new shortCode
@main.route("/shorten", methods=["POST"])
def create_code():
    data = request.json     
    short_url = generate_unique_short()
    new_url = Url(url=data['url'], shortCode = short_url)
    db.session.add(new_url)
    db.session.commit()
    item = Url.query.filter(Url.shortCode == short_url).first_or_404()
    return jsonify({"id":item.id,"url": item.url, "shortCode": item.shortCode, "createdAt": item.created, "updated": item.updated}), 201


@main.route("/shorten/<short_url>", methods=["GET"])
def get_url(short_url):
    item = Url.query.filter(Url.shortCode == short_url).first_or_404()
    return jsonify({"id":item.id,"url": item.url, "shortCode": item.shortCode, "createdAt": item.created, "updated": item.updated}), 200


@main.route("/shorten/<short_url>", methods=["PUT"])
def update_short(short_url):
    data = request.json
    item = Url.query.filter(Url.shortCode == short_url).first_or_404()
    item.url = data.get('url', item.url)
    db.session.commit()
    item = Url.query.filter(Url.shortCode == short_url).first_or_404()
    return jsonify({"id":item.id,"url": item.url, "shortCode": item.shortCode, "createdAt": item.created, "updated": item.updated}), 200
    

@main.route("/shorten/<short_url>", methods=["DELETE"])
def delete_short(short_url):
    item = Url.query.filter(Url.shortCode == short_url).first_or_404()
    db.session.delete(item)
    db.session.commit()
    return 204   


@main.get("/shorten/<short_url>/stats")
def stats(short_url):
    item = Url.query.filter(Url.shortCode == short_url).first_or_404()
    return jsonify({"id":item.id,"url": item.url, "shortCode": item.shortCode, "createdAt": item.created, "updated": item.updated, "accessCount": item.accessCount}), 200
