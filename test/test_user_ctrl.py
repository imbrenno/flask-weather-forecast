import pytest
import json
from faker import Faker
from main.database.models.user_model import Users

fake = Faker()


def test_create_user(client):
    data = {"username": fake.user_name(), "email": fake.email()}
    response = client.post(
        "/user/create", data=json.dumps(data), content_type="application/json"
    )
    assert response.status_code == 200
    response_data = response.get_json()
    assert response_data["message"] == "User added successfully"
    client.delete(f"/user/delete/{data['username']}")


def test_get_users(client):
    response = client.get("/user/list")
    assert response.status_code == 200
    response_data = response.get_json()
    assert "users" in response_data


def test_update_user(client):
    username = "existing_user"
    data = {"username": username, "email": fake.email()}
    Users(username=username, email="test@example.com").save()

    response = client.put(
        f"/user/update/{username}",
        data=json.dumps(data),
        content_type="application/json",
    )
    assert response.status_code == 200 or response.status_code == 404
    if response.status_code == 200:
        response_data = response.get_json()
        assert response_data[0]["message"] == "User update successfully"
        assert response_data[1]["username"] == data["username"]
        assert response_data[1]["email"] == data["email"]
    client.delete(f"/user/delete/{data['username']}")


def test_delete_user(client):
    username = "user_to_delete"
    Users(username=username, email="test@example.com").save()
    response = client.delete(f"/user/delete/{username}")
    assert response.status_code == 200 or response.status_code == 404
    if response.status_code == 200:
        response_data = response.get_json()
        assert response_data[0]["message"] == "User delected successfully"
