

def test_home(test_client):
    response = test_client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "welcome to service center API"
    }

def test_register(test_client):
    response = test_client.post(
        "/register",
        json={
            "username": "testuser",
            "email": "ahmed_test@example.com",
            "password": "12345678",
            "role": "user"
        }
    )

    assert response.status_code == 200

def test_login(test_client):
    test_client.post(
        "/register",
        json={
            "username": "testuser",
            "email": "ahmed_test@example.com",
            "password": "12345678",
            "role": "user"
        }
    )

    response = test_client.post(
        "/login",
        json={
            "email": "ahmed_test@example.com",
            "password": "12345678"
    

        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_create_customer(test_client):
    
    test_client.post(
        "/register",
        json={
            "username": "testuser",
            "email": "ahmed_test@example.com",
            "password": "12345678",
            "role": "user"
        }
    )

    login = test_client.post(
        "/login",
        json={
            "email": "ahmed_test@example.com",
            "password": "12345678"
        }
    )

    token = login.json()["access_token"]

    response = test_client.post(
        "/customer",
        headers={
            "Authorization": f"Bearer {token}"
    },
        json={
            "name": "Ahmed",
            "phone": "01012345678",
            "address": "Cairo"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Ahmed"
    assert data["phone"] == "01012345678"
    assert data["address"] == "Cairo"    