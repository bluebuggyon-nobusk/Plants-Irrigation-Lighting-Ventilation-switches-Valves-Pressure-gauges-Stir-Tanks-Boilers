# Project 1 

# Green house simulator #

"""
greenhouse_controller.py

Core logic for a Python-driven irrigation and environment control system.

- 5 bays
- Each bay controls:
    - watering schedule
    - lighting schedule
    - ventilation (fans + vents)
    - roof windows

This is a simulation-friendly controller core. Real hardware or a mobile app
would talk to this layer via APIs or device drivers.
"""

## Begin Coding here ## remember spaces and Tabs are not equals. 

from dataclasses import dataclass


@dataclass
class Schedule:
    """Simple schedule model: start_time and end_time as 'HH:MM' strings."""
    start_time: str
    end_time: str

    def describe(self) -> str:
        return f"{self.start_time} → {self.end_time}"


@dataclass
class BayConfig:
    """Configuration for a single bay in the system."""
    bay_id: int

    watering_schedule: Schedule | None = None
    lighting_schedule: Schedule | None = None
    ventilation_schedule: Schedule | None = None
    roof_window_schedule: Schedule | None = None

    def describe(self) -> str:
        def sched_to_text(name: str, sched: Schedule | None) -> str:
            if sched is None:
                return f"{name}: OFF"
            return f"{name}: {sched.describe()}"

        return (
            f"Bay {self.bay_id} configuration:\n"
            f"  {sched_to_text('Watering', self.watering_schedule)}\n"
            f"  {sched_to_text('Lighting', self.lighting_schedule)}\n"
            f"  {sched_to_text('Ventilation', self.ventilation_schedule)}\n"
            f"  {sched_to_text('Roof windows', self.roof_window_schedule)}"
        )


class GreenhouseController:
    """
    Central controller for a multi-bay irrigation and environment system.

    In a real implementation, this class would:
    - talk to hardware drivers (relays, smart plugs, motor controllers)
    - expose an API for a mobile app (Wi-Fi / HTTP / MQTT, etc.)
    - log events and errors
    """

    def __init__(self, bay_count: int = 5) -> None:
        self.bays: dict[int, BayConfig] = {}
        for bay_id in range(1, bay_count + 1):
            self.bays[bay_id] = BayConfig(bay_id=bay_id)

    # --- Schedule configuration methods ---

    def set_watering_schedule(self, bay_id: int, start_time: str, end_time: str) -> None:
        self._validate_bay_id(bay_id)
        self.bays[bay_id].watering_schedule = Schedule(start_time, end_time)

    def set_lighting_schedule(self, bay_id: int, start_time: str, end_time: str) -> None:
        self._validate_bay_id(bay_id)
        self.bays[bay_id].lighting_schedule = Schedule(start_time, end_time)

    def set_ventilation_schedule(self, bay_id: int, start_time: str, end_time: str) -> None:
        self._validate_bay_id(bay_id)
        self.bays[bay_id].ventilation_schedule = Schedule(start_time, end_time)

    def set_roof_window_schedule(self, bay_id: int, start_time: str, end_time: str) -> None:
        self._validate_bay_id(bay_id)
        self.bays[bay_id].roof_window_schedule = Schedule(start_time, end_time)

    def clear_all_schedules(self, bay_id: int) -> None:
        self._validate_bay_id(bay_id)
        bay = self.bays[bay_id]
        bay.watering_schedule = None
        bay.lighting_schedule = None
        bay.ventilation_schedule = None
        bay.roof_window_schedule = None

    # --- Simulation / inspection methods ---

    def describe_bay(self, bay_id: int) -> str:
        self._validate_bay_id(bay_id)
        return self.bays[bay_id].describe()

    def describe_all_bays(self) -> str:
        lines: list[str] = []
        for bay_id in sorted(self.bays.keys()):
            lines.append(self.bays[bay_id].describe())
            lines.append("")  # blank line between bays
        return "\n".join(lines).strip()

    # --- Internal helpers ---

    def _validate_bay_id(self, bay_id: int) -> None:
        if bay_id not in self.bays:
            raise ValueError(f"Invalid bay_id={bay_id}. Must be between 1 and {len(self.bays)}.")


if __name__ == "__main__":
    # Example usage / demo:
    controller = GreenhouseController(bay_count=5)

    # Configure bay 1
    controller.set_watering_schedule(bay_id=1, start_time="06:00", end_time="06:30")
    controller.set_lighting_schedule(bay_id=1, start_time="05:30", end_time="19:30")
    controller.set_ventilation_schedule(bay_id=1, start_time="10:00", end_time="16:00")
    controller.set_roof_window_schedule(bay_id=1, start_time="09:00", end_time="15:00")

    # Configure bay 2 with different settings
    controller.set_watering_schedule(bay_id=2, start_time="07:00", end_time="07:20")
    controller.set_lighting_schedule(bay_id=2, start_time="06:00", end_time="20:00")

    # Print a summary (this is what you’d show on a dashboard or send to a mobile app)
    print("Current greenhouse configuration:\n")
    print(controller.describe_all_bays())


# once you execute this function - all switches are off 
# It prints EAch bay, and each Bay in Function. 
#. Water - lighting - Vent - Roof windows 
