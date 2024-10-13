import logging
import unittest
import Runner



logging.basicConfig(
                    level=logging.INFO,
                    filemode="w",
                    filename="runner_tests.log",
                    encoding="utf-8",
                    format="%(asctime)s | %(levelname)s | %(message)s"
                    )
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только числом, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')
    def run(self):
        self.distance += self.speed * 2
    def walk(self):
        self.distance += self.speed
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name
class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)
    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers
# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            run1 = Runner("Vasja", speed=-5)
            i = 1
            while i <= 10:
                run1.walk()
                i += 1
            self.assertEqual(run1.distance, 50)
            logging.info('"test_walk" выполнен успешно')

        except ValueError as a:
            logging.warning("Неверная скорость для Runner: %s", a, exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            run2 = Runner(name=10, speed="Alex")
            j = 1
            while j <= 10:
                run2.run()
                j += 1
            self.assertEqual(run2.distance, 100)
            logging.info('"test_run" выполнен успешно')

        except TypeError as a:
            logging.warning("Неверный тип данных для объекта Runner: %s", a, exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run3 = Runner("Nik")
        run4 = Runner("Den")
        l = 1
        while l <= 10:
            run3.run()
            run4.walk()
            l += 1
        self.assertNotEqual(run3.distance, run4.distance)

if __name__ == "__main__":

    unittest.main()