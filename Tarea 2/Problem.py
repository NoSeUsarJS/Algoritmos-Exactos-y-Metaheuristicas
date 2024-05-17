from typing import List

class DataNode:
    def __init__(self, m: int, n: int, installation_cost: List[int], clinic_demand_places: List[List[int]]):
        self.m = m
        self.n = n
        self.installation_cost = installation_cost
        self.clinic_demand_places = clinic_demand_places

    @staticmethod
    def ReadData(data_path: str) -> 'DataNode':
        with open(data_path, "r") as file:
            m = int(file.readline())
            n = int(file.readline())
            
            installation_cost = []
            elements_appended = 0

            while elements_appended < n:
                line = file.readline().strip()
                if line:
                    installation_cost_line = [int(cost) for cost in line.split() if cost.strip()]
                    installation_cost.extend(installation_cost_line)
                    elements_appended += len(installation_cost_line)
            
            clinic_demand_places = []
            for _ in range(m):
                number_of_places = int(file.readline())
                sector = []

                places_appended = 0
                while places_appended < number_of_places:
                    line = file.readline().strip()
                    if line:
                        clinic_demand_places_line = [int(place) for place in line.split() if place.strip()]
                        sector.extend(clinic_demand_places_line)
                        places_appended += len(clinic_demand_places_line)

                clinic_demand_places.append(sector)

            return DataNode(m, n, installation_cost, clinic_demand_places)

#data_node = DataNode.read_data("data/C1.txt")

# Ahora puedes acceder a los datos como atributos de la instancia data_node
#print(data_node.m)
#print(data_node.n)
#print(data_node.installation_cost)
#print(data_node.clinic_demand_places)
