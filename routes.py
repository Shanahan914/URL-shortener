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
        if not db.session.query(Url).filter_by(short_url=short_url).first():
            return candidate 


# post -> create new shortCode
@app.route("/shorten", methods=["POST"])
def create_code():
    data = request.json
    short_url = generate_unique_short()
    new_url = Url(url=data['url'], shortcode = short_url)
    db.session.add(new_url)
    db.session.commit()
    item = db.get_or_404(shortCode = short_url)
    return jsonify({"id":item.id,"url": item.url, "shortCode": item.shortCode, "createdAt": item.created, "updated": item.updated}), 201


@app.route("/shorten/<short_url>", methods=["GET"])
def get_url(short_url):
    item = db.get_or_404(shortCode = short_url)
    return jsonify({"id":item.id,"url": item.url, "shortCode": item.shortCode, "createdAt": item.created, "updated": item.updated}), 200

@app.route("/shorten/<short_url>", methods=["PUT"])
def update_short(short_url):
    data = request.json
    item = db.get_or_404(shortCode = short_url)
    item.url = data.get('url', item.url)
    db.session.commit()
    item = db.get_or_404(shortCode = short_url)
    return jsonify({"id":item.id,"url": item.url, "shortCode": item.shortCode, "createdAt": item.created, "updated": item.updated}), 200
    

@app.route("/shorten/<short_url>", methods=["DELETE"])
def delete_short(short_url):
    item = db.get_or_404(shortCode = short_url)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "short url deleted"}), 204


@app.get("/shorten/<short_url>/stats")
def stats(short_url):
    item = db.get_or_404(shortCode = short_url)
    return jsonify({"id":item.id,"url": item.url, "shortCode": item.shortCode, "createdAt": item.created, "updated": item.updated, "accessCount": item.accessCount}), 200
