from __future__ import annotations
"""
All of the actions are stored here. The decorator 
ActionRegistry.register() registers an action to the AcionRegistry.
In order for this to happen, the action needs to be imported!
"""
from re import Match
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from action_registry import ActionRegistry

if TYPE_CHECKING:
    import re


class BaseAction(ABC):

    @abstractmethod
    def __init__(self, match:re.Match) -> None:
        pass

    @abstractmethod
    def execute(self, line:str):
        pass


@ActionRegistry.register()
class UpdateSeat(BaseAction):
    pattern = r"^Seat (\d{1}): (.+) \((.+) in chips\)"

    def __init__(self, match:re.Match) -> None:
        self.seat_number = match[1]
        self.player = match[2]
        #self.stack = match[3]

    def execute(self):
        pass

    def __repr__(self):
        return f"[Action:UpdateSeat] Player: {self.player} - Seat: {self.seat_number}"
    
@ActionRegistry.register()
class PlaceAnte(BaseAction):
    pattern = r"^(.+): posts the ante (.+)"

    def __init__(self, match):
        self.player = match[1]
        self.amount = match[2]

    def execute(self):
        return super().execute()
    
    def __repr__(self):
        return f"[Action:PlaceAnte] Player: {self.player} Ante: {self.amount}"
    
@ActionRegistry.register()
class DealCards(BaseAction):
    pattern = r"^Dealt to (.+) \[(\w{2} \w{2})\]$"

    def __init__(self, match) -> None:
        self.player = match[1]
        self.cards = match[2]

    def execute(self):
        return super().execute()
    
    def __repr__(self):
        return f"[Action:DealCards] Player: {self.player} Cards: {self.cards}"
    
@ActionRegistry.register()
class Bet(BaseAction):
    pattern = r"(.+): bets (.+)"

    def __init__(self, match) -> None:
        self.player = match[1]
        self.amount = match[2]

    def execute(self):
        pass

    def __repr__(self) -> str:
        return f"[Action:Bet] Player: {self.player} Amount: {self.amount}"

@ActionRegistry.register()
class UncalledBet(BaseAction):
    pattern = r"^Uncalled bet \((.+)\) returned to (.+)"

    def __init__(self, match) -> None:
        self.player = match[2]
        self.amount = match[1]

    def execute(self):
        pass

    def __repr__(self) -> str:
        return f"[Action:UncalledBet] Returned to Player: {self.player} Amount: {self.amount}"
    
@ActionRegistry.register()
class Raise(BaseAction):
    pattern = r"^(.+): raises (.+) to (.+)"

    def __init__(self, match) -> None:
        self.player = match[1]
        self.amount_from = match[2]
        self.amount_to = match[3]

    def execute(self):
        return super().execute()
    
    def __repr__(self):
        return f"[Action:Raise] Player: {self.player} Amount: {self.amount_from} -> {self.amount_to}"

@ActionRegistry.register()
class Check(BaseAction):
    pattern = r"^(.+): checks"

    def __init__(self, match) -> None:
        self.player = match[1]

    def execute(self):
        pass

    def __repr__(self):
        return f"[Action:Check] Player: {self.player}"
    
@ActionRegistry.register()
class Call(BaseAction):
    pattern = r"^(.+): calls (.+)"

    def __init__(self, match) -> None:
        self.player = match[1]
        self.amount = match[2]

    def execute(self):
        return super().execute()
    
    def __repr__(self):
        return f"[Action:Call] Player: {self.player} Amount: {self.amount}"

@ActionRegistry.register()  
class Fold(BaseAction):
    pattern = r"^(.+): folds"

    def __init__(self, match) -> None:
        self.player = match[1]
    
    def execute(self):
        pass

    def __repr__(self):
        return f"[Action:Fold] Player: {self.player}"
    
@ActionRegistry.register()
class StageHoleCards(BaseAction):
    pattern = r"\*\*\* HOLE CARDS \*\*\*"

    def __init__(self, match) -> None:
        self.name = "HOLE CARDS"

    def execute(self):
        return super().execute()
    
    def __repr__(self) -> str:
        return f"[Action:ChangeStage] {self.name}"
    
@ActionRegistry.register()
class StageShowDown(BaseAction):
    pattern = r"\*\*\* SHOW DOWN \*\*\*"

    def __init__(self, match) -> None:
        self.name = "SHOW DOWN"

    def execute(self):
        return super().execute()
    
    def __repr__(self) -> str:
        return f"[Action:ChangeStage] {self.name}"
    
@ActionRegistry.register()
class StageSummary(BaseAction):
    pattern = r"\*\*\* SUMMARY \*\*\*" 

    def __init__(self, match) -> None:
        self.name = "SUMMARY"

    def execute(self):
        return super().execute()
    
    def __repr__(self) -> str:
        return f"[Action:ChangeStage] {self.name}"
    
@ActionRegistry.register()
class StageFlop(BaseAction):
    pattern = r"\*\*\* FLOP \*\*\* \[(\w{2} \w{2} \w{2})\]"

    def __init__(self, match) -> None:
        self.name = "FLOP"
        self.cards = match[1]

    def execute(self):
        return super().execute()
    
    def __repr__(self) -> str:
        return f"[Action:ChangeStage] {self.name} Cards: {self.cards}"
    
@ActionRegistry.register()
class StageTurn(BaseAction):
    pattern = r"\*\*\* TURN \*\*\* \[(\w{2} \w{2} \w{2})\] \[(\w{2})\]"

    def __init__(self, match) -> None:
        self.name = "TURN"
        self.cards = match[1] + " " + match[2]

    def execute(self):
        return super().execute()
    
    def __repr__(self) -> str:
        return f"[Action:ChangeStage] {self.name} Cards: {self.cards}"
    
@ActionRegistry.register()
class StageRiver(BaseAction):
    pattern = r"\*\*\* RIVER \*\*\* \[(\w{2} \w{2} \w{2} \w{2})\] \[(\w{2})\]"

    def __init__(self, match) -> None:
        self.name = "RIVER"
        self.cards = match[1] + " " + match[2]

    def execute(self):
        return super().execute()
    
    def __repr__(self) -> str:
        return f"[Action:ChangeStage] {self.name} Cards: {self.cards}"
    
@ActionRegistry.register()
class PlaceSB(BaseAction):
    pattern = r"^(.+): posts small blind (.+)"

    def __init__(self, match) -> None:
        self.player = match[1]
        self.amount = match[2]

    def execute(self):
        return super().execute()
    
    def __repr__(self):
        return f"[Action:PlaceSB] Player: {self.player} Amount: {self.amount}"
    
@ActionRegistry.register()
class PlaceBB(BaseAction):
    pattern = r"^(.+): posts big blind (.+)"

    def __init__(self, match) -> None:
        self.player = match[1]
        self.amount = match[2]

    def execute(self):
        return super().execute()
    
    def __repr__(self):
        return f"[Action:PlaceSB] Player: {self.player} Amount: {self.amount}"
    
@ActionRegistry.register()
class ShowCards(BaseAction):
    pattern = r"^(.+): shows \[(\w{2} \w{2})\]"

    def __init__(self, match) -> None:
        self.player = match[1]
        self.cards = match[2]

    def execute(self):
        return super().execute()
    
    def __repr__(self):
        return f"[Action:Show] Player: {self.player} Cards: {self.cards}"
    
@ActionRegistry.register()
class Collect(BaseAction):
    pattern = r"^(.+) collected (.*) from pot"

    def __init__(self, match) -> None:
        self.player = match[1]
        self.amount = match[2]

    def execute(self):
        return super().execute()
    
    def __repr__(self):
        return f"[Action:Collect] Player: {self.player} Amount: {self.amount}"
    
@ActionRegistry.register()
class Muck(BaseAction):
    pattern =  r"(.+): mucks hand"

    def __init__(self, match) -> None:
        self.player = match[1]

    def execute(self):
        return super().execute()
    
    def __repr__(self):
        return f"[Action:Muck] Player: {self.player}"
    
@ActionRegistry.register()
class DoesntShow(BaseAction):
    pattern = r"^(.+): doesn't show hand"

    def __init__(self, match) -> None: 
        self.player = match[1]

    def execute(self):
        return super().execute()
    
    def __repr__(self):
        return f"[Action:Doesn't show] Player: {self.player}"
    
@ActionRegistry.register()
class TotalPot(BaseAction):
    pattern = r"Total pot (.+) \| Rake (.)"

    def __init__(self, match) -> None:
        self.amount = match[1]
        self.rake = match[2]

    def execute(self):
        return super().execute()
    
    def __repr__(self):
        return f"[Action:TotalPot] Amount: {self.amount} Rake: {self.rake}"
    
@ActionRegistry.register()
class SummaryTotalPotSplit(BaseAction):
    #Total pot 1514 Main pot 272. Side pot 1242. | Rake 0
    pattern = r"Total pot (.+) Main pot (.+). Side pot (.+). | Rake (.+)"

    def __init__(self, match: Match) -> None:
        self.total_pot = match[1]
        self.main_pot = match[2]
        self.side_pot = match[3]
        self.rake = match[4]

    def execute(self, line: str):
        return super().execute(line)
    
    def __repr__(self) -> str:
        return f"[Summary: TotalPotSplit] Total Pot: {self.total_pot} Main Pot: {self.main_pot} Side Pot: {self.side_pot} Rake: {self.rake}"
    
@ActionRegistry.register()
class SummaryCollected(BaseAction):
    pattern = r"Seat \d: (.+) (\(\w*\))* *\(*\w* *\w*\)* *collected \((.+)\)"

    def __init__(self, match) -> None:
        self.player = match[1]
        self.amount = match[2]

    def execute(self):
        return super().execute()
    
    def __repr__(self):
        return f"[Summary: Collected] Player: {self.player} Amount: {self.amount}"
    
@ActionRegistry.register()
class SummaryCollectedSplitPot(BaseAction):
    pattern = r"(.+) collected (.+) from (\w+) pot"

    def __init__(self, match) -> None:
        self.player = match[1]
        self.amount = match[2]
        self.pot = match[3]

    def execute(self):
        return super().execute()
    
    def __repr__(self) -> str:
        return f"[Summary: Collected Split] Player:{self.player} Amount:{self.amount} Pot:{self.pot}"
    
@ActionRegistry.register()
class SummaryFolded(BaseAction):
    pattern = r"Seat \d: (.+) (\(\w*\))* *(\(\w* *\w*\))* *folded"

    def __init__(self, match) -> None:
        self.player = match[1]

    def execute(self):
        return super().execute()
    
    def __repr__(self):
        return f"[Summary: Folded] Player: {self.player}"
    
@ActionRegistry.register()
class SummaryShowedWon(BaseAction):
    pattern = r"^Seat \d: (.+) \(*.*\)* *showed \[(\w{2} \w{2})\] and won \((.+)\)"

    def __init__(self, match) -> None:
        self.player = match[1]
        self.cards = match[2]
        self.amount = match[3]

    def execute(self):
        return super().execute()
    
    def __repr__(self):
        return f"[Summary: Showed Won] Player: {self.player} Cards: {self.cards} Amount:{self.amount}"
    
@ActionRegistry.register()
class SummaryShowedLost(BaseAction):
    pattern = r"^Seat \d: (.+) \(*.*\)* *showed \[(\w{2} \w{2})\] and lost "

    def __init__(self, match) -> None:
        self.player = match[1]
        self.cards = match[2]

    def execute(self):
        return super().execute()
    
    def __repr__(self):
        return f"[Summary: Showed Lost] Player: {self.player} Cards: {self.cards}"

@ActionRegistry.register()
class SummaryMucked(BaseAction):
    #Seat 6: dalequeva823 mucked [Qh 9s]
    pattern = r"^Seat \d+: (.+) mucked (\[(.+)\])"

    def __init__(self, match: Match) -> None:
        self.player = match[1]
        self.hand = match[2]

    def execute(self, line: str):
        return super().execute(line)
    
    def __repr__(self) -> str:
        return f"[Summary: Mucked] Player: {self.player} Hand: {self.hand}"
    
@ActionRegistry.register()
class SummaryBoard(BaseAction):
    pattern = r"^Board \[(.+)\]"

    def __init__(self, match) -> None:
        self.board = match[1]

    def execute(self):
        return super().execute()
    
    def __repr__(self) -> str:
        return f"[Summary: Board] Cards: {self.board}"
    
@ActionRegistry.register()
class SummaryFinished(BaseAction):
    pattern = r"^(.+) finished the tournament"

    def __init__(self, match) -> None:
        self.player = match[1]
    
    def execute(self):
        return super().execute()
    
    def __repr__(self) -> str:
        return f"[Summary: Finished] Player: {self.player}"
    
@ActionRegistry.register()
class TournamentWin(BaseAction):
    pattern = r"^(.+) wins the tournament"

    def __init__(self, match) -> None:
        self.player = match[1]

    def execute(self):
        return super().execute()
    
    def __repr__(self) -> str:
        return f"[Final Winner] Player: {self.player}"
    
@ActionRegistry.register()
class TimeOut(BaseAction):
    pattern = r"^(.+) has timed out"

    def __init__(self, match) -> None:
       self.player = match[1]

    def execute(self):
        return super().execute()
    
    def __repr__(self) -> str:
        return f"[TimeOut] Player: {self.player}"
    
@ActionRegistry.register()
class SitOut(BaseAction):
    pattern = r"^(.+) is sitting out"

    def __init__(self, match) -> None:
       self.player = match[1]

    def execute(self):
        return super().execute()
    
    def __repr__(self) -> str:
        return f"[SitOut] Player: {self.player}"
    
@ActionRegistry.register()
class Returned(BaseAction):
    pattern = r"(.+) has returned"

    def __init__(self, match: Match) -> None:
        self.player = match[1]

    def execute(self, line: str):
        return super().execute(line)
    
    def __repr__(self) -> str:
        return f"[Returned] Player: {self.player}"

@ActionRegistry.register()
class Disconnected(BaseAction):
    pattern = r"^(.+) is disconnected"

    def __init__(self, match: Match) -> None:
        self.player = match[1]

    def execute(self, line: str):
        return super().execute(line)
    
    def __repr__(self) -> str:
        return f"[Disconnected] Player: {self.player}"
    
@ActionRegistry.register()
class Connected(BaseAction):
    pattern = r"^(.+) is connected"

    def __init__(self, match: Match) -> None:
        self.player = match[1]

    def execute(self, line: str):
        return super().execute(line)
    
    def __repr__(self) -> str:
        return f"[Connected] Player: {self.player}"
    
@ActionRegistry.register()
class UpdateTournament(BaseAction):
    #PokerStars Hand #204921198877: Tournament #2702072599
    pattern = r"^PokerStars Hand #(\d+): Tournament #(\d+), "

    def __init__(self, match: Match) -> None:
        self.hand_id = match[1]
        self.tournament_id = match[2]

    def execute(self, line: str):
        return super().execute(line)
    
    def __repr__(self) -> str:
        return f"\n[Update Tournament] Hand: {self.hand_id} Tournament: {self.tournament_id}"
    
@ActionRegistry.register()
class UpdateCashGame(BaseAction):
    #PokerStars Zoom Hand #204864602572:  Hold'em No Limit
    pattern = r"^PokerStars Zoom Hand #(\d+):  Hold'em No Limit"

    def __init__(self, match: Match) -> None:
        self.hand_id = match[1]

    def execute(self, line: str):
        return super().execute(line)
    
    def __repr__(self) -> str:
        return f"[Update Cash Game] Hand ID: {self.hand_id}"

@ActionRegistry.register()
class UpdateTable(BaseAction):
    pattern = r"^Table '(.+ *.*)' \d+-max Seat #(\d+) is the button"

    def __init__(self, match: Match) -> None:
        self.table_id = match[1]
        self.btn_seat = match[2]

    def execute(self, line: str):
        return super().execute(line)
    
    def __repr__(self) -> str:
        return f"[Update Tournament] Table ID: {self.table_id} Button-Seat: {self.btn_seat}"
    
@ActionRegistry.register()
class PlayAfterBtn(BaseAction):
    pattern = r"^(.+) will be allowed to play after the button"

    def __init__(self, match: Match) -> None:
        self.player = match[1]

    def execute(self, line: str):
        return super().execute(line)
    
    def __repr__(self) -> str:
        return f"[PlayAfterBtn] Player: {self.player}" 
    
@ActionRegistry.register()
class PlayerChat(BaseAction):
    pattern = r'^(.+) said, "(.+)"'

    def __init__(self, match: Match) -> None:
        self.player = match[1]
        self.chat = match[2]

    def execute(self, line: str):
        return super().execute(line)
    
    def __repr__(self) -> str:
        return f"[Chat] Player: {self.player} Content: {self.chat}"
    
@ActionRegistry.register()
class CashOut(BaseAction):
    pattern = r"^(.+) cashed out the hand for (.*)"

    def __init__(self, match: Match) -> None:
        self.player = match[1]
        self.amount = match[2]

    def execute(self, line: str):
        return super().execute(line)
    
    def __repr__(self) -> str:
        return f"[Cash Out] Player: {self.player} Amount: {self.amount}"