from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

# Test 1 : Creation d'un nouveau dresseur + vérification de la création
def test_create_trainer(mocker):
    """
        Creation d'un trainer
    """
    mocker.patch(
        "app.actions.create_trainer",
        return_value= {
        "name": "Tom",
        "birthdate": "1990-11-04",
        "id": 1,
        "inventory": [],
        "pokemons": []
        }
    )
    response = client.post("/trainers/", json={"name": "Tom", "birthdate": "1990-11-04"})
    assert response.status_code == 200
    assert response.json() == {"name": "Tom", "birthdate": "1990-11-04", "id": 1, "inventory": [], "pokemons": []}


