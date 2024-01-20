#!/usr/bin/python3
"""
Unittests for BaseModel class
"""

import unittest
import models
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import os


class Test_BaseModel(unittest.TestCase):
    """
    test casess for BaseModel class
    """

    def setUp(self):
        """
        set up the env before each test case
        """
        self.base_model = BaseModel()

    def tearDown(self):
        """
        clean up the test env after each test case if needed
        """
        pass

    def test_with_arguments(self):
        """
        test initialization with arguments
        """
        data = {
            'id': '123',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T00:00:00',
            'name': 'Test'
        }
        base_model = BaseModel(**data)

        self.assertEqual(base_model.id, '123')
        self.assertEqual(base_model.created_at,
                         datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(base_model.updated_at,
                         datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(base_model.name, 'Test')

    def test_without_arguments(self):
        """
        test initialization without arguments
        """
        base_model = BaseModel()

        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)
        self.assertEqual(base_model.created_at, base_model.updated_at)

    def test_args(self):
        """
        test unused args
        """
        basemodel = BaseModel(None)
        self.assertNotIn(None, basemodel.__dict__.values())

    def test_kwargs(self):
        """
        test kwargs
        """
        date = datetime.now()
        formatted = date.isoformat()
        b_m = BaseModel(id="123", created_at=formatted, updated_at=formatted)
        self.assertEqual(b_m.id, "123")
        self.assertEqual(b_m.created_at, date)
        self.assertEqual(b_m.updated_at, date)

    def test_kwargs_None(self):
        """
        test with kwargs set to None
        """
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_args_and_kwargs(self):
        """
        test with both args and kwargs
        """
        date = datetime.now()
        form = date.isoformat()
        base = BaseModel(id="123", created_at=form, updated_at=form)
        self.assertEqual(base.id, "123")
        self.assertEqual(base.created_at, date)
        self.assertEqual(base.updated_at, date)

    def test_id_str(self):
        """
        check if id data type
        """
        self.assertEqual(str, type(BaseModel().id))

    def test_id_unique(self):
        """
        test if id generated are unique
        """
        user1 = BaseModel()
        user2 = BaseModel()
        self.assertNotEqual(user1.id, user2.id)

    def test_created_at_datetime(self):
        """
        check if attribute is a datetime object
        """
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_created_at_timestamp(self):
        """
        check if the timestamp is different
        """
        user1 = BaseModel()
        sleep(0.05)
        user2 = BaseModel()
        self.assertLess(user1.created_at, user2.created_at)

    def test_updated_at_datetime(self):
        """
        check if attribute is a datetime object
        """
        self.assertEqual(datetime, type(BaseModel(). updated_at))

    def test_updated_at_timestamp(self):
        """
        checks if the timestamp is different
        """
        user1 = BaseModel()
        sleep(0.05)
        user2 = BaseModel()
        self.assertLess(user1.updated_at, user2.updated_at)

    def test_instance_storage(self):
        """
        check if storage and retrival were successful
        """
        self.assertIn(BaseModel(), models.storage.all().values())

    def test__str__(self):
        """
        test the string representation
        """
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.__str__(), base2.__str__())

    def test_save(self):
        """
        test the effective of timestamp updates
        """
        base = BaseModel()
        sleep(0.1)
        update = base.updated_at
        base.save()
        self.assertLess(update, base.updated_at)

    def test_two_saves(self):
        """
        tests the effectivity of diffrent timestamps updates
        """
        base = BaseModel()
        sleep(0.1)
        upadte1 = base.updated_at
        base.save()
        update2 = base.updated_at
        self.assertLess(upadte1, update2)
        sleep(0.1)
        base.save()
        self.assertLess(update2, base.updated_at)

    def test_save_updates_file(self):
        """
        tests that updates are updated and stored correctly
        """
        base = BaseModel()
        base.save()
        baseid = "BaseModel." + base.id
        with open("file.json", "r") as file:
            self.assertIn(baseid, file.read())

    def test_to_dict(self):
        """
        tests the expected output
        """
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertEqual(self.base_model.to_dict(), expected_dict)

    def test_to_dict_type(self):
        """
        verifys the class returns a dictionary
        """
        base = BaseModel()
        self.assertTrue(dict, type(base.to_dict()))

    def test_different_to_dict(self):
        """
        tests that the class produces 2 diff dict for diff instances
        """
        base1 = BaseModel()
        sleep(0.05)
        base2 = BaseModel()
        self.assertNotEqual(base1.to_dict(), base2.to_dict())

    def test_to_dict_has_correct_keys(self):
        """
        tests that the dict contains the right keys
        """
        base = BaseModel()
        self.assertIn("id", base.to_dict())
        self.assertIn("__class__", base.to_dict())
        self.assertIn("created_at", base.to_dict())
        self.assertIn("updated_at", base.to_dict())

    def test_to_dict_created_at_format(self):
        """
        checks the ISO formatted string
        """
        base = self.base_model.to_dict()
        created_at = base["created_at"]
        self.assertEqual(created_at, self.base_model.created_at.isoformat())

    def test_to_dict_updated_at_format(self):
        """
        checks the ISO formatted string
        """
        base = self.base_model.to_dict()
        updated_at = base["updated_at"]
        self.assertEqual(updated_at, self.base_model.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
