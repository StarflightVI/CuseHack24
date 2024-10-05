from flask import Flask, render_template

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Care Locator - Home</title>
        <link rel="stylesheet" href="static/styles.css">
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
                color: #333;
            }
            header {
                background-color: #4CAF50;
                color: white;
                padding: 10px 0;
                text-align: center;
            }
            h1 {
                margin: 0;
                font-size: 2.5em;
            }
            nav ul {
                display: flex;
                justify-content: center;
                padding: 0;
                margin: 20px 0;
                list-style: none;
            }
            nav ul li {
                margin: 0 15px;
            }
            nav ul li a {
                text-decoration: none;
                color: #4CAF50;
                font-size: 1.2em;
                font-weight: bold;
                padding: 10px 15px;
                border: 2px solid #4CAF50;
                border-radius: 5px;
                transition: background-color 0.3s, color 0.3s;
            }
            nav ul li a:hover {
                background-color: #4CAF50;
                color: white;
            }
            .content {
                text-align: center;
                margin: 50px 20px;
            }
            footer {
                background-color: #333;
                color: white;
                text-align: center;
                padding: 10px 0;
                position: absolute;
                bottom: 0;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to the Care Locator!</h1>
        </header>
        <div class="content">
            <p>Find hospitals, pharmacies, and emergency rooms near you.</p>
            <nav>
                <ul>
                    <li><a href="/hospitals">Hospitals</a></li>
                    <li><a href="/pharmacies">Pharmacies</a></li>
                    <li><a href="/emergency_rooms">Emergency Rooms</a></li>
                </ul>
            </nav>
        </div>
        <footer>
            <p>&copy; 2024 Care Locator. All rights reserved.</p>
        </footer>
    </body>
    </html>
    '''

@app.route('/hospitals')
def hospitals():
    return render_template('Hospitals.html')

@app.route('/pharmacies')
def pharmacies():
    return render_template('Pharmacies.html')

@app.route('/emergency_rooms')
def emergency_rooms():
    return render_template('Emergency_Rooms.html')

if __name__ == '__main__':
    app.run(debug=True)
