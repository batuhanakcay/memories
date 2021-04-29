import flask
import arrow
import memories

@memories.app.route('/')
def show_index():
    connection = memories.model.get_db()

    friends = connection.execute(
        "SELECT * "
        "FROM friends "
        "ORDER BY name "
    ).fetchall()

    connections = connection.execute(
        "SELECT DISTINCT connection "
        "FROM friends "
        "ORDER BY connection "
    ).fetchall()
    connections_list = []
    for con in connections:
        connections_list.append(con["connection"])

    states = connection.execute(
        "SELECT DISTINCT name "
        "FROM states "
        "ORDER BY name "
    ).fetchall()
    states_list = []
    for state in states:
        states_list.append(state["name"])

    hobbies = connection.execute(
        "SELECT DISTINCT name "
        "FROM hobbies "
        "ORDER BY name "
    ).fetchall()
    hobbies_list = []
    for hobby in hobbies:
        hobbies_list.append(hobby["name"])
    
    context = {"friends": friends, "connections": connections_list,
     "states": states_list, "hobbies": hobbies_list}
    return flask.render_template("index.html", **context)