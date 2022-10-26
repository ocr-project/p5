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

def loadModel():
    modelBert1 = SentenceTransformer('flax-sentence-embeddings/stackoverflow_mpnet-base', device='cuda')
    def predict(question):
        encoded = modelBert1.encode(question)
        binaryTags = model['classifier'].predict([encoded])
        tags = []
        for col, value in enumerate(binaryTags[0]):
            if value == 1:
                tags.append(model['tags'][col])
        return tags

    with open('./model.pickle', 'rb') as handle:
        model = pickle.load(handle)

    return predict

predict = loadModel()

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
        tags = predict(question)
        app.logger.info('%s', tags)
        return {
            "tags": tags,
            "question": question,
        }, 200    

if __name__ == '__main__':
    #print(predict('C++ IDE for Linux? 	I want to expand my programming horizons to Linux.'))
    app.run(debug=True)        