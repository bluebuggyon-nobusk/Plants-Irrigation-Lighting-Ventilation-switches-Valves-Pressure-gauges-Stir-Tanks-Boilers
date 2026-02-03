# Plants-Irrigation-Lighting-Ventilation-switches-Valves-Pressure-gauges-Stir-Tanks-Boilers


Python Greenhouse Controller # project 1
Python-driven irrigation and environment control core for a multi-bay greenhouse system.

Designed to be ready for connection to Wi‑Fi hardware and mobile apps (Android / iOS) in future versions.


This project currently focuses on the logic layer only. Hardware drivers and phone apps would talk to this controller over an API or network connection.

##########################################################################################################################

# Project 1 – Greenhouse Switches: 5 Bay Controller

Python-driven irrigation and environment control core for a **5-bay greenhouse system**.

Each bay can have its own:
- watering schedule  
- lighting schedule  
- ventilation schedule (fans + vents)  
- roof window schedule  

This project focuses on the **controller logic**. In a real installation, this code would connect to Wi‑Fi hardware (relays, smart plugs, motor controllers) and be managed from a mobile or web application.

---

## How It Works

At the center is the `GreenhouseController` class:

- Creates and manages 5 `BayConfig` objects (one per bay).
- Stores independent schedules for each bay:
  - `watering_schedule`
  - `lighting_schedule`
  - `ventilation_schedule`
  - `roof_window_schedule`
- Provides methods to:
  - set schedules for a given bay  
  - clear all schedules for a bay  
  - print a human-readable summary of each bay or all bays

Supporting models:

- `Schedule`  
  Simple time window with `start_time` and `end_time` stored as `"HH:MM"` strings, plus a `describe()` helper.

- `BayConfig`  
  Configuration for a single bay, with optional `Schedule` objects for each system (watering, lighting, ventilation, roof windows).

When you run:

```bash
python greenhouse_controller.py


######################################################################################################
