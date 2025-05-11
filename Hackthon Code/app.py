from flask import Flask, render_template, request

app = Flask(__name__)

# Emission factors (kg CO2 per unit)
EMISSION_FACTORS = {
    "electricity": 0.5,       # per kWh
    "gas": 2.0,               # per therm
    "oil": 3.0,               # per liter
    "car": 0.2,               # per km
    "bus": 0.1,               # per km
    "train": 0.05,            # per km
    "plane": 0.25,            # per km
    "meat": 2.5,              # per serving
    "vegetables": 0.5,        # per serving
    "processed_food": 1.5     # per serving
}

@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/Tracker')
def Tracker():
    return render_template('Tracker.html')

@app.route('/About_us')
def About_us():
    return render_template('About_us.html')

@app.route('/AboutCarbonFootprint')
def AboutC():
    return render_template('AboutCarbonFootprint.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Home Energy
    electricity = float(request.form['electricity'])
    gas = float(request.form['gas'])
    oil = float(request.form['oil'])
    
    # Transportation
    car_mileage = float(request.form['car_mileage'])
    bus_mileage = float(request.form['bus_mileage'])
    train_mileage = float(request.form['train_mileage'])
    plane_mileage = float(request.form['plane_mileage'])
    
    # Food
    meat = float(request.form['meat'])
    vegetables = float(request.form['vegetables'])
    processed_food = float(request.form['processed_food'])
    
    # Calculations
    home_energy = (electricity * EMISSION_FACTORS['electricity'] +
                  gas * EMISSION_FACTORS['gas'] +
                  oil * EMISSION_FACTORS['oil'])
    
    transportation = (car_mileage * EMISSION_FACTORS['car'] +
                     bus_mileage * EMISSION_FACTORS['bus'] +
                     train_mileage * EMISSION_FACTORS['train'] +
                     plane_mileage * EMISSION_FACTORS['plane'])
    
    food = (meat * EMISSION_FACTORS['meat'] +
           vegetables * EMISSION_FACTORS['vegetables'] +
           processed_food * EMISSION_FACTORS['processed_food'])
    
    total_footprint = home_energy + transportation + food
    
    # Determine eco-friendliness
    if total_footprint < 6000:
        rating = "Excellent"
        message = "Your carbon footprint is lower than average!"
    elif total_footprint < 12000:
        rating = "Good"
        message = "Your carbon footprint is about average."
    else:
        rating = "Needs Improvement"
        message = "Your carbon footprint is higher than average. Consider reducing energy use."
    
    return render_template('result.html', 
                         home_energy=round(home_energy, 2),
                         transportation=round(transportation, 2),
                         food=round(food, 2),
                         total_footprint=round(total_footprint, 2),
                         rating=rating,
                         message=message)

if __name__ == '__main__':
    app.run(debug=True)