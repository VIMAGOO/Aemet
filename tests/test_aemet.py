import aemet 

def test_get_city():
    data = aemet.get_daily("08017")[0]
    assert data["provincia"] == "Barcelona"