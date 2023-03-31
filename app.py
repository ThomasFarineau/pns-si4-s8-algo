from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/move', methods=['POST'])
def move():
    b = request.args.get('b')
    if b is None:
        return jsonify({'error': 'Paramètre b manquant'}), 400
    # TODO: effectuer les opérations nécessaires avec le paramètre b
    result = {'message': 'Opération effectuée avec succès'}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)