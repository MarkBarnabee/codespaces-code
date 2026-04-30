from codde import Point
from codde import makeData


ex_player = Point("f", [2, 3])
makeData(Point._instances)


def test_coddename():
    assert ex_player.name == "f"

def test_coddepoints():
    assert ex_player.points == [2, 3]

def test_coddemake():
    assert makeData(Point._instances) == {"f": [2, 3]}
