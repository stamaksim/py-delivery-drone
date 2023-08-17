class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(self,
                 name: str,
                 weight: int | float,
                 coords: list[int] = None
                 ) -> None:
        self.name = name
        self.weight = weight
        if coords is None:
            coords = [0, 0]
        self.coords = coords or [0, 0]
        self.x = coords[0]
        self.y = coords[1]

    def go_forward(self, step: int = 1) -> list[int]:
        self.coords[1] += step
        return self.coords

    def go_back(self, step: int = 1) -> list[int]:
        self.coords[1] -= step
        return self.coords

    def go_right(self, step: int = 1) -> list[int]:
        self.coords[0] += step
        return self.coords

    def go_left(self, step: int = 1) -> list[int]:
        self.coords[0] -= step
        return self.coords

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(self,
                 name: str,
                 weight: int | float,
                 coords: list = None
                 ) -> None:
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords=coords)
        self.z = coords[2]

    def go_up(self, step: int = 1) -> list[int]:
        self.coords[2] += step
        return [self.coords[0], self.coords[1], self.z]

    def go_down(self, step: int = 1) -> list[int]:
        self.coords[2] -= step
        return [self.coords[0], self.coords[1], self.z]


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int | float,
        max_load_weight: int | float,
        current_load: int | float,
        coords: list = None,
    ) -> None:
        super().__init__(name, weight, coords=coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: int | float) -> Cargo:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo
            return self.current_load
        return None

    def unhook_load(self) -> None:
        self.current_load = None
        return self.current_load
