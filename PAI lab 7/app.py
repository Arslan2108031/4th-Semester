from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    api_url = "https://api.thecatapi.com/v1/images/search?breed_ids=pers"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data:
            cat_image = data[0]["url"]
            breed_name = "Persian Cat"
        else:
            cat_image = None
            breed_name = "Not Found"
    else:
        cat_image = None
        breed_name = "API Error"
    return render_template("index.html", image=cat_image, breed=breed_name)

if __name__ == "__main__":
    app.run(debug=True)



