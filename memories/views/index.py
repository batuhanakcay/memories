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

    context = {"friends": friends, "connections": connections_list}
    return flask.render_template("index.html", **context)