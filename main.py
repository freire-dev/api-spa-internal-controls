from flask import Flask, jsonify, make_response, request
from flask_cors import CORS, cross_origin

Controls = [
    {
        'code': 'CTECH.1',
        'name': 'Control Name 1',
        'description': 'Control Desc 1',
        'goal': "Control Goal 1",
        'frequency': "Quarterly",
        'risk': "High",
        'controlOwner': "Control owner name 1",
        'effective': 'Efetivo'
    },
    {
        'code': 'CTECH.2',
        'name': 'Control Name 2',
        'description': 'Control Desc 2',
        'goal': "Control Goal 2",
        'frequency': "Quarterly",
        'risk': "High",
        'controlOwner': "Control owner name 2",
        'effective': 'Inefetivo'
    },
    {
        'code': 'CTECH.3',
        'name': 'Control Name 3',
        'description': 'Control Desc 3',
        'goal': "Control Goal 3",
        'frequency': "Quarterly",
        'risk': "High",
        'controlOwner': "Control owner name 3",
        'effective': 'Efetivo'
    },
    {
        'code': 'CBSEC.1',
        'name': 'Control Name 4',
        'description': 'Control Desc 4',
        'goal': "Control Goal 4",
        'frequency': "Quarterly",
        'risk': "High",
        'controlOwner': "Control owner name 4",
        'effective': 'Efetivo'
    },
    {
        'code': 'CBSEC.2',
        'name': 'Control Name 5',
        'description': 'Control Desc 5',
        'goal': "Control Goal 5",
        'frequency': "Quarterly",
        'risk': "High",
        'controlOwner': "Control owner name 5",
        'effective': 'Inefetivo'
    },
    {
        'code': 'CBSEC.3',
        'name': 'Control Name 6',
        'description': 'Control Desc 6',
        'goal': "Control Goal 6",
        'frequency': "Quarterly",
        'risk': "High",
        'controlOwner': "Control owner name 6",
        'effective': 'Efetivo'
    },
]

app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JSON_SORT_KEYS'] = False


@app.route('/', methods=['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def getAPI():
    return make_response(
        jsonify(Controls)
    )


@app.route('/', methods=['DELETE'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def delAPI():
    delControl = request.json
    index = Controls.index(delControl)
    Controls.pop(index)
    return make_response(
        jsonify(controlDel=delControl)
    )


@app.route('/', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def postAPI():
    addControl = request.json
    Controls.append(addControl)
    return make_response(
        jsonify(newControl=addControl)
    )


@app.route('/', methods=['PUT'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def updateAPI():
    updateControl = request.json
    index = Controls.index(updateControl['toDelete'])
    Controls[index] = updateControl['toAdd']

    return make_response(
        jsonify(controlUpdate=updateControl['toAdd'])
    )


app.run(host='0.0.0.0')