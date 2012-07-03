#!/usr/bin/env python
# -*-coding:utf-8 -*

class Publisher(object):
    """Keep a list of subscribers.
    Use 'subscribe' method to add a subscriber
    Use 'unsubscribe' method to remove a subscriber
    Use 'publish' method to broadcast a message to a specified or every subscribers."""

    def __init__(self):
        self.subscribers = []
        super(Publisher, self).__init__()

    def subscribe(self, subscriber):
        """subscriber: an object that inherits from Subscriber and receives the message in its 'receive' method."""
        if not isinstance(subscriber, Subscriber):
            raise TypeError("The given subscriber (" + str(subscriber) + ") must inherit from Subscriber.")
        if subscriber in self.subscribers:
            raise ValueError("This subscriber is already in the subscribers list: " + str(subscriber))
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        """subscriber: the one to remove."""
        if not isinstance(subscriber, Subscriber):
            raise TypeError("The given subscriber (" + str(subscriber) + ") must inherit from Subscriber.")
        if subscriber not in self.subscribers:
            raise ValueError("This subscriber is not in the subscribers list: " + str(subscriber))
        self.subscribers.remove(subscriber)

    def publish(self, message, check = None):
        """message: the message to broadcast (given to 'receive')
        check: a callback that return True if the given object must receive the message, False elsewhere."""

        if check is None:
            check = lambda s: True
        else:
            if not callable(check):
                raise ValueError("'check' must be a callable object since it is a callback function.")

        for subscriber in self.subscribers:
            if not isinstance(subscriber, Subscriber):
                raise TypeError("The subscriber (" + str(subscriber) + ") must inherit from Subscriber.")
            if check(subscriber):
                subscriber.receive(message)


class Subscriber(object):
    """Expose a 'receive' method in order to receive some Publisher's messages."""
    def __init__(self):
        super(Subscriber, self).__init__()

    def receive(self, message):
        """Must be implemented by the extending class."""
        raise NotImplementedError("This Subscriber object must override the 'receive' method.")

