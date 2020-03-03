from flask import Flask,request,jsonify

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/balance', methods=['POST'])
def home():
    if request.method == 'POST':
        req = request.get_json()
        persons = req['persons']
        contributions = req['contributions']
        balance = {}
        balance['balance'] = getBalance(persons,contributions)
        return jsonify(balance)

def getBalance(persons,contributions):
    numPersons = len(persons)
    foodItems = {}
    balance = {}
    for person in persons:
        personContribution = contributions[person]
        for contribution in personContribution:
            if contribution in foodItems:
                foodItems[contribution] = personContribution[contribution] + foodItems[contribution]
            else:
                foodItems[contribution] = personContribution[contribution]
    for person in persons:
        personContribution = contributions[person]
        personBalance={}
        for contribution in personContribution:
            personBalance[contribution]=int(personContribution[contribution] - (foodItems[contribution]/numPersons))
        balance[person] = personBalance
    return balance
app.run()
