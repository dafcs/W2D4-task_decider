import unittest
from src.task_decider import *
from src.task import Task

class TestDecider(unittest.TestCase):

    

    def test_task_decider_1(self):
        self.result = get_preferred_option("Wash Dishes","Cook Dinner")
        self.assertEqual("Wash Dishes", self.result)
    def test_task_decider_2(self):
        self.result = get_preferred_option("Wash Clothes","Cook Dinner")
        self.assertEqual("Wash Clothes", self.result)
    def test_task_decider_3(self):
        self.result = get_preferred_option("Wash Dishes","Clean Windows")
        self.assertEqual("Clean Windows", self.result)
    def test_task_decider_4(self):
        self.result = get_preferred_option("Clean Windows","Do Ironing")
        self.assertEqual("Clean Windows", self.result)
    def test_task_decider_5(self):
        self.result = get_preferred_option("Do Ironing","Cook Dinner")
        self.assertEqual("Cook Dinner", self.result)
    def test_task_decider_fail(self):
        self.assertEqual("you having a laugh", get_preferred_option("Wash Dishes","Wash Dishes"))
