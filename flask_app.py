from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "<p>Hallo Declerck</p>"


if __name__ == '__main__':
    app.run(port=5000,debug=True)


#
# git checkout -b main      Switched to a new branch 'main'
# Er wordt een kopie gemaakt van de omgeving. Je kan nu met 2 omgevingen die de zelfde basis hebben verder werken.


#
#  Opstarten met   flask --app flask_app run
#
