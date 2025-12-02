class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp 
        self.kwh = kwh              

class Building:
    def __init__(self, name):
        self.name = name
        self.readings = []  

    def add_reading(self, reading):
        self.readings.append(reading)

    # Calculate total energy consumption
    def total_consumption(self):
        return sum(r.kwh for r in self.readings)

    # Generate report
    def report(self):
        total = self.total_consumption()
        max_kwh = max(r.kwh for r in self.readings)
        min_kwh = min(r.kwh for r in self.readings)
        return f"{self.name}: Total={total}, Max={max_kwh}, Min={min_kwh}"

class BuildingManager:
    def __init__(self):
        self.buildings = {}  

    
    def add_building(self, building):
        self.buildings[building.name] = building

    # summary of total consumption per building
    def summary(self):
        return {b.name: b.total_consumption() for b in self.buildings.values()}

if __name__ == "__main__":
    b1 = Building("BuildingA")
    b1.add_reading(MeterReading("2025-01-01 00:00", 120))
    b1.add_reading(MeterReading("2025-01-01 01:00", 130))

    b2 = Building("BuildingB")
    b2.add_reading(MeterReading("2025-01-01 00:00", 200))

    manager = BuildingManager()
    manager.add_building(b1)
    manager.add_building(b2)

    print(b1.report())
    print(b2.report())
    print(manager.summary())
