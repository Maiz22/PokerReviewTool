from player import Player
from table import Table


def test_table_find_hero() -> None:
    player1 = Player("player1", stack=1450)
    player2 = Player("player2", stack=2000)
    hero = Player("Maiz", stack=1500, is_hero=True)
    player4 = Player("player4", stack=1000)
    list_of_players = [player1, player2, hero, player4]
    table = Table(total_seats=6, players=list_of_players, table_stack=None)
    assert table.find_hero() == 2

def test_table_position_players() -> None:
    player1 = Player("player1", stack=1450)
    player2 = Player("player2", stack=2000)
    hero = Player("Maiz", stack=1500, is_hero=True)
    player4 = Player("player4", stack=1000)
    list_of_players = [player1, player2, hero, player4]
    table = Table(total_seats=6, players=list_of_players, table_stack=None)
    table.position_players()
    assert [player.name for player in table.seats if player is not None] == ["Maiz", "player4", "player1", "player2"]

def test_table_position_dealer() -> None:
    player1 = Player("player1", stack=1450)
    player2 = Player("player2", stack=2000, is_dealer=True)
    hero = Player("Maiz", stack=1500, is_hero=True)
    player4 = Player("player4", stack=1000)
    list_of_players = [player1, player2, hero, player4]
    table = Table(total_seats=6, players=list_of_players, table_stack=None)
    table.position_players()
    assert table.dealer_position == 1