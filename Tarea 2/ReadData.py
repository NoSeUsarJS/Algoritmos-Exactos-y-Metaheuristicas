from typing import List

def read_data(data_path: str) -> dict:
    with open(data_path, "r") as file:
        m: int = int(file.readline())
        n: int = int(file.readline())
        installation_cost: List[int] = []
        clinic_demand_places: List[List[int]] = []

        elements_appended: int = 0

        while elements_appended < n:
            line: str = file.readline()
            installation_cost_line: List[int] = [int(cost) for cost in line.replace("\n", "").split(" ") if cost.strip()]
            elements_appended += len(installation_cost_line)
            installation_cost += installation_cost_line
        
        for i in range(m):
            number_of_places: int = int(file.readline())
            places_appended: int = 0
            sector: List[int] = []

            while places_appended != number_of_places:
                line: str = file.readline()
                clinic_demand_places_line: List[int] = [int(place) for place in line.replace("\n", "").split(" ") if place.strip()]
                places_appended += len(clinic_demand_places_line)
                sector += clinic_demand_places_line

            clinic_demand_places.append(sector)

        return {
            "m": m,
            "n": n,
            "installation_cost": installation_cost,
            "clinic_demand_places": clinic_demand_places
        }