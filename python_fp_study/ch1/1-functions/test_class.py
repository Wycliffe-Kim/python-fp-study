class TestClass:
    def set_value_with_side_effect(self, value: int):
        self.value = value

    def f_pure(self, value: int):
        return value * 2

    def f_not_pure(self):
        return self.value * 2
