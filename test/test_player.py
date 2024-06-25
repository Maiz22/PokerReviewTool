from player import Player

def test_player() -> None:
    player1 = Player(name="Maiz", stack=1500)
    assert player1.stack == 1500