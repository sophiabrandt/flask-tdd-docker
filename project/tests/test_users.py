import json

from project.tests.utils import add_user, recreate_db


def test_add_user(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        "/users",
        data=json.dumps({"username": "michael", "email": "michael@testdriven.io"}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert "michael@testdriven.io was added!" in data["message"]
    assert "success" in data["status"]


def test_add_user_invalid_json(test_app, test_database):
    client = test_app.test_client()
    resp = client.post("/users", data=json.dumps({}), content_type="application/json",)
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Invalid payload." in data["message"]
    assert "fail" in data["status"]


def test_add_user_invalid_json_keys(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        "/users",
        data=json.dumps({"username": "john"}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Invalid payload." in data["message"]
    assert "fail" in data["status"]


def test_add_user_duplicate_email(test_app, test_database):
    client = test_app.test_client()
    client.post(
        "/users",
        data=json.dumps({"username": "john", "email": "john@johndoe.com"}),
        content_type="application/json",
    )
    resp = client.post(
        "/users",
        data=json.dumps({"username": "john", "email": "john@johndoe.com"}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Sorry. That user already exists." in data["message"]
    assert "fail" in data["status"]


def test_single_user(test_app, test_database):
    user = add_user("alison", "alison@test.com")
    client = test_app.test_client()
    resp = client.get(f"/users/{user.id}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert "alison" in data["data"]["username"]
    assert "alison@test.com" in data["data"]["email"]
    assert "success" in data["status"]


def test_single_user_no_id(test_app, test_database):
    client = test_app.test_client()
    resp = client.get("/users/blub")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
    assert "User does not exist." in data["message"]
    assert "fail" in data["status"]


def test_single_user_incorrect_id(test_app, test_database):
    client = test_app.test_client()
    resp = client.get("/users/999")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
    assert "User does not exist." in data["message"]
    assert "fail" in data["status"]


def test_all_users(test_app, test_database):
    recreate_db()
    add_user("john", "john@doe.com")
    add_user("mike", "mike@email.com")
    client = test_app.test_client()
    resp = client.get("/users")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert len(data["data"]["users"]) == 2
    assert "john" in data["data"]["users"][0]["username"]
    assert "mike" in data["data"]["users"][1]["username"]
    assert "john@doe.com" in data["data"]["users"][0]["email"]
    assert "mike@email.com" in data["data"]["users"][1]["email"]
    assert "success" in data["status"]
