#!/usr/bin/env python
# -*-coding:utf-8 -*

from os import name as os_name
from pybsub import *

if __name__ == '__main__':
    class TestPub(Publisher):
        """A Publisher test."""
        def __init__(self):
            super(TestPub, self).__init__()

        def test(self, name, elitist = False):
            check = None
            if elitist:
                check = lambda s: s.priority > 0
            self.publish("Run " + str(name), check)

    class TestSub(Subscriber):
        """A Subscriber test."""
        def __init__(self, name, priority = 0):
            self.name = name
            self.priority = priority
            super(TestSub, self).__init__()

        def receive(self, message):
            print("[" + message + "] OHAI, I'm " + str(self.name) + "!")


    pub  = TestPub()
    sub1 = TestSub(1, 1)
    sub2 = TestSub(2)

    pub.test("0")

    pub.subscribe(sub1)
    pub.subscribe(sub2)
    pub.test("1")
    pub.test("1P", True)

    pub.unsubscribe(sub1)
    pub.test("2")

    if os_name == "posix":
        print("\nYou're doing it right.")
    else:
        input("\nAppuyez sur la touche 'Entrée' pour quitter\n")
