from flask import Flask
from flask import request

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
@app.route('/index')
def index():
    return """
           <html>
           <head>
             <link rel="stylesheet" href="styles.css">
           </head>
           <body>
             <h1>Welcome!</h1>
             <form action="/hello" method="GET">
               <label for="name">Enter your first name:</label>
               <input type="text" name="first_name"><br><br>
               <label for="name">Enter your last name:</label>
               <input type="text" name="last_name"><br><br>
               <input type="submit" value="Proceed to Women's Volleyball Game Times">
             <form>
           </body>
           </html>
            """

@app.route('/hello')
def hello():
    #Getting information via the query string portion of a URL
    print(f"request.url={request.url}")
    print(f"request.url={request.query_string}")
    print(f"request.url={request.args.get('first_name')}")
    print(f"request.url={request.args.get('last_name')}")

    games = ["September 21 (1PM)", "September 22 (2PM)", "October 4 (7AM)", "October 6 (11AM)", "October 18 (6PM)", "October 20 (1PM)", "October 23 (6PM)", "October 27 (1PM)", "November 8 (6PM)", "November 10 (1PM)", "November 20 (6PM)", "November 27 (1PM)"]
    response= f"""
           <html>
           <head>
           <link rel="stylesheet" href="styles.css">
           </head>
           <body>
           <h1>Hello, {request.args.get('first_name')} {request.args.get('last_name')}!</h1>

           What Women's games are you available to work?</br>"""

    for f in games:
      response += f"<a href='fruit/{f}'>{f.capitalize()}</a></br>"""

    response+=f"""
               </body>
               </html>
                """
    return response


@app.route('/games/<games_list>')
def games_list(game_time):
    #Getting information via the path portion of a URL
    games={
          "September 21 (1PM)"
          "September 22 (2PM)"
          "October 4 (7AM)"
          "October 6 (11AM)"
          "October 18 (6PM)"
          "October 20 (1PM)"
          "October 23 (6PM)"
          "October 27 (1PM)"
          "November 8 (6PM)"
          "November 10 (1PM)"
          "November 20 (6PM)"
          "November 27 (1PM)"
         }


    response = f"""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <title>My Webpage</title>
                    <link rel="stylesheet" href="../styles.css">
                </head>
                <body>
                <h1>Sign Up Sheet</h1>
                {tip}
                </body>
                </html>"""

    return response

app.run(debug=True)
