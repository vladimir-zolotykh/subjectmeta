#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
# 2. Subject Implementation using the Metaclass
from subjectmeta import SubjectMeta
from observer import ConsoleLogger, EmailSender


class DataProcessor(metaclass=SubjectMeta):
    """
    A class that processes data and notifies observers when its state changes.
    It automatically has attach, detach, and notify methods due to SubjectMeta.
    """

    def __init__(self, name="DefaultProcessor"):
        self.name = name
        self._data = {}  # Internal state that changes

    def add_data_point(self, key, value):
        print(f"\n[{self.name}] Adding new data: {key}={value}")
        old_value = self._data.get(key)
        self._data[key] = value
        # Notify observers about the change
        self.notify(
            {"action": "add", "key": key, "old_value": old_value, "new_value": value}
        )

    def remove_data_point(self, key):
        if key in self._data:
            print(f"\n[{self.name}] Removing data point: {key}")
            value = self._data.pop(key)
            self.notify({"action": "remove", "key": key, "removed_value": value})
        else:
            print(f"\n[{self.name}] Key '{key}' not found, nothing to remove.")


# 3. Demonstrate Usage
if __name__ == "__main__":
    processor = DataProcessor("FinancialProcessor")

    logger1 = ConsoleLogger("ActivityLogger")
    logger2 = ConsoleLogger("DebugLogger")
    email_alert = EmailSender("admin@example.com")

    # Attach observers
    processor.attach(logger1)
    processor.attach(logger2)
    processor.attach(email_alert)

    # Simulate state changes
    processor.add_data_point("revenue", 1000)
    processor.add_data_point("expenses", 300)

    # Detach one observer
    processor.detach(logger2)

    processor.add_data_point("profit", 700)
    processor.remove_data_point("expenses")

    # Trying to attach a non-observer (will raise TypeError if enforced)
    # try:
    #     processor.attach("not an observer")
    # except TypeError as e:
    #     print(f"\nERROR: {e}")
