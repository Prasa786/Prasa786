import unittest
from datetime import datetime, timedelta


class Car:
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        raise NotImplementedError


class BatteryMixin:
    def needs_service(self):
        today = datetime.today().date()
        service_interval = timedelta(days=365 * 3)
        return (today - self.last_service_date) >= service_interval


class EngineMixin:
    def needs_service(self):
        mileage_interval = 30000
        mileage_since_last_service = self.current_mileage - self.last_service_mileage
        return mileage_since_last_service >= mileage_interval


class Calliope(Car, EngineMixin, BatteryMixin):
    pass


class Glissade(Car, EngineMixin, BatteryMixin):
    pass


class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date, 0, 0)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        return self.warning_light_is_on or super().needs_service()


class Rorschach(Car, EngineMixin, BatteryMixin):
    pass


class Thovex(Car, EngineMixin, BatteryMixin):
    pass


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today - timedelta(days=365 * 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today - timedelta(days=365)
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
import unittest
from datetime import datetime, timedelta


class Car:
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        raise NotImplementedError


class BatteryMixin:
    def needs_service(self):
        today = datetime.today().date()
        service_interval = timedelta(days=365 * 3)
        return (today - self.last_service_date) >= service_interval


class EngineMixin:
    def needs_service(self):
        mileage_interval = 30000
        mileage_since_last_service = self.current_mileage - self.last_service_mileage
        return mileage_since_last_service >= mileage_interval


class Calliope(Car, EngineMixin, BatteryMixin):
    pass


class Glissade(Car, EngineMixin, BatteryMixin):
    pass


class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date, 0, 0)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        return self.warning_light_is_on or super().needs_service()


class Rorschach(Car, EngineMixin, BatteryMixin):
    pass


class Thovex(Car, EngineMixin, BatteryMixin):
    pass


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today - timedelta(days=365 * 2)
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today - timedelta(days=365)
        current_mileage = 0
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = Calliope(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today - timedelta(days=365 * 33)
        current_mileage = 0
        last_service_mileage = 0

        car = Glissade(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today - timedelta(days=365)
        current_mileage = 0
        last_service_mileage = 0

￼Enter
