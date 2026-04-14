from flask import Flask
app = Flask(__name__)
import mysql.connector

connection = mysql.connector.connect(
            host='127.0.0.1',
            database='flight_game',
            user='Valtteri',
            password='Pallero1234'
        )

@app.route('/kenttä/<icao>')
def hae_kentta(icao):
    cursor = connection.cursor()
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao,))
    tulos = cursor.fetchone()

    if not tulos:
        return {"Error": f"Lentokenttää koodilla {icao} ei löytynyt."}


    return {
        "ICAO": icao,
        "Name": tulos[0],
        "Municipality": tulos[1]
    }
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)