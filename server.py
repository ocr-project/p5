from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields
import pickle
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

api = Api(app, version='1.0', title='Ia API',
    description='A simple Api from machine learning model',
)

ns = api.namespace('questions', description='Questions operations')

classificationInput = api.schema_model('classificationInput', {
    "description": "Question",
    'type': 'string',
    "example": "C++ IDE for Linux? 	I want to expand my programming horizons to Linux.",
})

classificationOutput = api.schema_model('classificationOutput', {
    "description": "Liste des tags prédits",
    "type": "array",
    "example": ["c++", "linux"],
    "items": {
        "type": "string",
    }
})

@app.route("/hello")
def home():
    response = "Hello, World!"
    return jsonify(response)

@ns.route('/stack')
class StackOverflowQuestions(Resource):

    @ns.doc('get tags')
    @ns.expect(classificationInput)
    @ns.response(200, 'success', classificationOutput)
    def post(self):
        question = request.stream.read().decode("utf-8")
        return {
            "tags": ['tag1', 'tag2'],
            "question": question,
        }, 200    

if __name__ == '__main__':
    #print(predict('C++ IDE for Linux? 	I want to expand my programming horizons to Linux.'))
    app.run(debug=True)        