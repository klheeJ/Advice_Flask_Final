from flask import Blueprint,request, jsonify, render_template
from models import db, Advice_Collection, advice_schema, advices_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/advice', methods = ['POST'])
def create_advice():
    advice = request.json['advice']
    advice_ID = request.json['advice_ID']


    advice_ = Advice_Collection(advice, advice_ID)

    db.session.add(advice_)
    db.session.commit()

    response = advices_schema.dump(advice_)
    return jsonify(response)

@api.route('/advice', methods = ['GET'])
def get_advice():
    advices = Advice_Collection.query.all()
    response = advices_schema.dump(advices)
    return jsonify(response)

@api.route('/advice/<id>', methods = ['GET'])
def get_single_advice(id):
    advice_ = Advice_Collection.query.get(id)
    response = advices_schema.dump(advice_)
    return jsonify(response)

@api.route('/advice/<id>', methods = ['POST', 'PUT'])
def update_advice(id):
    advice_ = Advice_Collection.query.get(id)
    advice_.advice_ID = request.json['advice_ID']
    advice_.advice = request.json['advice']

    db.session.commit()
    response = advice_schema.dump(advice_)
    return jsonify(response)

@api.route('/advice/<id>', methods = ['DELETE'])
def delete_advice(id):
    advice_ = Advice_Collection.query.get(id)
    db.session.delete(advice_)
    db.session.commit()
    response = advice_schema.dump(advice_)
    return jsonify(response)