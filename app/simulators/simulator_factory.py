from app.simulators.travel_agent import TravelAgentSimulator


class SimulatorFactory:

    @staticmethod
    def get_simulator(agent: str):

        simulators = {
            "travel-agent": TravelAgentSimulator(),
        }

        simulator = simulators.get(agent)

        if simulator is None:
            raise ValueError(f"Unsupported agent: {agent}")

        return simulator