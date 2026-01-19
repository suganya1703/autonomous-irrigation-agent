
# Autonomous Irrigation AI Agent

class IrrigationAgent:
    def decide(self, soil, rain, time):

        if rain == "yes":
            return "Pump OFF | Reason: Rain detected"

        if time == "afternoon":
            return "Pump OFF | Reason: Afternoon - water loss high"

        if soil <= 20:
            return "Pump ON | Reason: Soil very dry"

        elif soil <= 40:
            return "Pump ON | Reason: Moderate soil moisture"

        else:
            return "Pump OFF | Reason: Soil moisture sufficient"


agent = IrrigationAgent()

soil = int(input("Enter soil moisture (0-100): "))
rain = input("Is it raining? (yes/no): ").lower()
time = input("Time (morning/afternoon/evening): ").lower()

print(agent.decide(soil, rain, time))
