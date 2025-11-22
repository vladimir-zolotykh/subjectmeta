#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
import abc
from observer import Observer


class SubjectMeta(type):
    """Metaclass that automatically imbues any class using it with
    Observer Subject capabilities.

    """

    def __new__(mcs, name, bases, attrs):
        # Ensure the class has an _observers list.
        # We put it in attrs *before* calling type.__new__ so it's part of the class definition.
        if "_observers" not in attrs:
            attrs["_observers"] = []

        # Define the attach, detach, and notify methods for the class
        def attach_observer(cls_instance, observer):
            if not isinstance(observer, Observer):
                # Optional: Enforce that observers implement the Observer interface
                raise TypeError(
                    f"Observer must be an instance of Observer, got {type(observer)}"
                )
            if observer not in cls_instance._observers:
                cls_instance._observers.append(observer)
                print(
                    f"{observer.__class__.__name__} attached to "
                    f"{cls_instance.__class__.__name__}."
                )

        def detach_observer(cls_instance, observer):
            if observer in cls_instance._observers:
                cls_instance._observers.remove(observer)
                print(
                    f"{observer.__class__.__name__} detached from "
                    f"{cls_instance.__class__.__name__}."
                )

        def notify_observers(cls_instance, data=None):
            print(
                f"[{cls_instance.__class__.__name__}] Notifying "
                f"{len(cls_instance._observers)} observers with data: {data}"
            )
            for observer in cls_instance._observers:
                observer.update(cls_instance, data)

        # Add these methods to the class's attribute dictionary
        # We pass them as methods that will operate on the instance (self/cls_instance)
        attrs["attach"] = attach_observer
        attrs["detach"] = detach_observer
        attrs["notify"] = notify_observers

        # Now, create the class using the modified attrs
        return super().__new__(mcs, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        # Call the base type's __init__
        super().__init__(name, bases, attrs)
        # You could add further class-level initialization here if needed
        # print(f"Class '{name}' initialized with SubjectMeta.")
