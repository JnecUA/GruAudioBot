class AbstractHandler:
    def __init__(self, dp) -> None:
        self.dp = dp
        self.wrap()

    def wrap(self) -> None:
        pass