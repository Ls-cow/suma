from flask import Flask, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    result=None
    if request.method == "POST":
        number1 = request.form.get("number1")
        number2 = request.form.get("number2")
        # Si els camps estan buits, torna un missatge per evitar errors
        if (not number1 or not number1.isnumeric()) or (not number2 or not number2.isnumeric()):
            result= "Tots els camps han de contenir números vàlids!"
        else:
            result = int(number1) + int(number2)
    
    # Aquesta resposta s'envia si la petició no és POST
    return f'''
   <!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulari Suma</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}

        .form-container {{
            background-color: #fff;
            padding: 20px 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            text-align: center;
        }}

        h1 {{
            color: #333;
            margin-bottom: 20px;
        }}

        label {{
            display: block;
            margin-bottom: 5px;
            color: #555;
        }}

        .numbers {{
            width: calc(100% - 20px);
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }}

        #btn-suma{{
            background-color: #4caf50;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }}

        #btn-suma:hover {{
            background-color: #45a049;
        }}

        .footer {{
            margin-top: 10px;
            font-size: 12px;
            color: #888;
        }}
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Suma Selenium</h1>
        <form method="post">
            <label for="number1">Número 1:</label>
            <input type="text" id="number1" name="number1" class="numbers" placeholder="Introdueix el primer número">

            <label for="number2">Número 2:</label>
            <input type="text" id="number2" name="number2" class="numbers" placeholder="Introdueix el segon número">

            <input type="submit" id="btn-suma" value="Calcular">          
        </form> 
        {'<div class="result"><strong>Resultat:</strong> <input type="text" class="numbers" name="resultat" readonly value="' + str(result) + '"/></div>' if result is not None else ''}

    </div>
</body>
</html>

    '''

if __name__ == "__main__":
    app.run(debug=True)

