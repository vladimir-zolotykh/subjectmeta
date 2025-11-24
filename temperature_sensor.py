#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class Observer(ABC):
    @abstractmethod
    def update(self, *args, **kwargs) -> None:
        pass


class Subject:
    def __init__(self) -> None:
        self.observers: list[Observer] = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)


class TemperatureSensor(Subject):
    @property
    def temperature(self) -> float:
        return self._temperature

    @temperature.setter
    def temperature(self, val: float):
        self._temperature = val
        self.notify(self.temperature)


class Logger(Observer):
    def update(self, *args, **kwargs):
        logger.info("Temperature: %s" % args[0])


class Display(Observer):
    def update(self, *args, **kwargs):
        print(f"Temperature: {args[0]}")


if __name__ == "__main__":
    sensor = TemperatureSensor()
    sensor.attach(Logger())
    sensor.attach(Display())
    sensor.temperature = 11
    sensor.temperature = 17
