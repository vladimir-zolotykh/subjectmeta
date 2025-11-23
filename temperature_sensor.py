#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import logging

logging.basicConfig(level=logging.DEBUG)


class Observer:
    def update(self, *args, **kwargs):
        pass


class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)


class TemperatureSensor(Subject):
    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, val):
        self._temperature = val
        self.notify(self.temperature)


class Logger(Observer):
    def update(self, *args, **kwargs):
        logging.info("Temperature: %s" % args[0])


class Display(Observer):
    def update(self, *args, **kwargs):
        print(f"Temperature: {args[0]}")


if __name__ == "__main__":
    sensor = TemperatureSensor()
    sensor.attach(Logger())
    sensor.attach(Display())
    sensor.temperature = 11
    sensor.temperature = 17
