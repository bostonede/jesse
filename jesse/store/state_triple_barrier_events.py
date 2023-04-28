from dataclasses import dataclass
from collections import deque

from jesse.enums import trade_types


@dataclass
class TripleBarrierEvent:
    signal_timestamp: float = None
    side: trade_types = None
    profit_take_price: float = None
    stop_loss_price: float = None
    expiration_limit_time: float = None
    label: int = None
    executed_at: float = None


class TripleBarrierEventsState:
    def __init__(self) -> None:
        # used in simulation only
        self.to_execute: deque[TripleBarrierEvent] = deque()
        self.executed: deque[TripleBarrierEvent] = deque()

        self.profit_take_count = 0
        self.stop_loss_count = 0
        self.no_sign_count = 0

    def show_stats(self) -> dict:
        total_executed = len(self.executed)

        return {
            "total_executed": total_executed,
            "profit_take_count": self.profit_take_count,
            "stop_loss_count": self.stop_loss_count,
            "no_sign_count": self.no_sign_count,
        }
