from flask import Flask, render_template, session, redirect, url_for
print("aaaa")
from flask_session import Session
from tempfile import mkdtemp
print("bbb")



app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route("/")
def index():

    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"

    return render_template("game.html", game=session["board"], turn=session["turn"], winner = checkForWinner(session["board"]))

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    print(session["board"])
    session["board"][row][col] = session["turn"]
    if session["turn"] == "X":
        session["turn"] = "O"
    elif session["turn"] == "O":
        session["turn"] = "X"

    return redirect(url_for("index"))


def checkForWinner(board):
    # winner on row
    if (board[0][0] == board[0][1] == board[0][2] != None):
        return f'the winner is: {board[0][0]}'
    elif (board[1][0] == board[1][1] == board[1][2] != None):
        return f'the winner is: {board[1][0]}'
    elif (board[2][0] == board[2][1] == board[2][2] != None):
        return f'the winner is: {board[2][0]}'

    # winner on col
    elif (board[0][0] == board[1][0] == board[2][0] != None):
        return f'the winner is: {board[0][0]}' 
    elif (board[0][1] == board[1][1] == board[2][1] != None):
        return f'the winner is: {board[0][1]}'
    elif (board[0][2] == board[1][2] == board[2][2] != None):
        return f'the winner is: {board[0][2]}'
    
    # winner on diag
    elif (board[0][0] == board[1][1] == board[2][2] != None):
        return f'the winner is: {board[0][0]}' 
    elif (board[2][0] == board[1][1] == board[0][2] != None):
        return f'the winner is: {board[2][0]}'

    else:
        return 'Tic-Ta-Toe Game'


@app.route("/reset")
def reset():
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"
        return redirect(url_for("index"))






if __name__ == '__main__':
    app.run()