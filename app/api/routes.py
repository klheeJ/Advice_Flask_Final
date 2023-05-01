from flask import Blueprint,request, jsonify, render_template
from models import db, Advice, advice_schema, advices_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/advice', methods = ['POST'])
def create_advice():
    advice = request.json['advice']


    advice_ = Advice(advice)

    db.session.add(advice_)
    db.session.commit()
    return jsonify(201)
    # response = advices_schema.dump(advice_)


@api.route('/advice', methods = ['GET'])
def get_advice():
    advices = Advice.query.all()
    response = advices_schema.dump(advices)
    return jsonify(response)


@api.route('/advice/<id>', methods = ['GET'])
def get_single_advice(id):
    advice_ = Advice.query.get(id)
    response = advices_schema.dump(advice_)
    return jsonify(response)


@api.route('/advice/<id>', methods = ['PUT'])
def update_advice(id):
    advice_ = Advice.query.get(id)
    advice_.advice = request.json['advice']

    db.session.commit()
    response = advice_schema.dump(advice_)
    return jsonify(response)

@api.route('/advice/<id>', methods = ['DELETE'])
def delete_advice(id):
    advice_ = Advice.query.get(id)
    db.session.delete(advice_)
    db.session.commit()
    response = advice_schema.dump(advice_)
    return jsonify(response)