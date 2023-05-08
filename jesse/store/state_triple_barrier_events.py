from dataclasses import dataclass, asdict, field
from collections import deque

import jesse.helpers as jh
from jesse.enums import trade_types


@dataclass
class TripleBarrierEvent:
    signal_timestamp: float = None
    side: trade_types = None
    profit_taking_rate: float = None
    profit_taking_price: float = None
    stop_loss_rate: float = None
    stop_loss_price: float = None
    expiration_limit_time: float = None
    label: int = None
    executed_at: float = None
    note: dict = field(default_factory=dict)

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        info = asdict(self)
        info["signal_datetime"] = jh.timestamp_to_time(self.signal_timestamp) if self.signal_timestamp else None
        info["expiration_limit_datetime"] = jh.timestamp_to_time(self.expiration_limit_time) if self.expiration_limit_time else None
        info["executed_at_datetime"] = jh.timestamp_to_time(self.executed_at) if self.executed_at else None
        return str(info)

class TripleBarrierEventsState:
    def __init__(self) -> None:
        # used in simulation only
        self.to_execute: deque[TripleBarrierEvent] = deque()
        self.executed: deque[TripleBarrierEvent] = deque()

        self.profit_taking_count = 0
        self.stop_loss_count = 0
        self.no_sign_count = 0

    def show_stats(self) -> dict:
        total_executed = len(self.executed)

        return {
            "total_executed": total_executed,
            "profit_taking_count": self.profit_taking_count,
            "stop_loss_count": self.stop_loss_count,
            "no_sign_count": self.no_sign_count,            
            "profit_taking_ratio": self.profit_taking_count / total_executed if total_executed != 0 else 0,
            "stop_loss_ratio": self.stop_loss_count / total_executed if total_executed != 0 else 0,
            "no_sign_ratio": self.no_sign_count / total_executed if total_executed != 0 else 0,
        }
