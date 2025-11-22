#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import abc
import logging


# 1. Observer Interface (using ABC for clarity, though not strictly
# required for Duck Typing)
class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self, subject, data):
        """
        Receives update from subject.
        :param subject: The subject that sent the notification.
        :param data: The data payload from the subject.
        """
        pass


# Concrete Observer implementations
class ConsoleLogger(Observer):
    def __init__(self, name="Logger"):
        self.name = name

    def update(self, subject, data):

        # logging.info(
        #     "[%s] received update from %s: %s",
        #     self.name,
        #     subject.__class__.__name__,
        #     data,
        # )

        print(
            f"[{self.name}] received update from {subject.__class__.__name__}: {data}"
        )


class EmailSender(Observer):
    def __init__(self, recipient):
        self.recipient = recipient

    def update(self, subject, data):
        print(
            f"[EmailSender] Sending email to {self.recipient} about {subject.__class__.__name__} update: {data}"
        )
