#!/usr/bin/env python3

import pytest

from classes.skier import Skier
from classes.event import Event
from classes.riding_team import RidingTeam
from classes.registration import Registration

class TestRegistrations:
    """Registration in registration.py"""

    def test_has_riding_team(self):
        """is initialized with a riding_tea,"""
        riding_team1 = RidingTeam("Bullseye", "Thomas")
        riding_team2 = RidingTeam("Cheese Puff", "Jen")
        event = Event(15000, "Steamboat Springs")
        event2 = Event(25000, "Leadville")
        skier = Skier("Farhan")

        registration_1 = Registration(riding_team1, skier, event)
        registration_2 = Registration(riding_team2, skier, event2)
        assert registration_1.riding_team == riding_team1
        assert registration_2.riding_team == riding_team2

    def test_has_skier(self):
        """is initialized with a skier"""
        riding_team1 = RidingTeam("Bullseye", "Thomas")
        riding_team2 = RidingTeam("Cheese Puff", "Jen")
        event = Event(15000, "Steamboat Springs")
        event2 = Event(25000, "Leadville")
        skier = Skier("Farhan")
        skier2 = Skier("Kip")

        registration_1 = Registration(riding_team1, skier, event)
        registration_2 = Registration(riding_team2, skier2, event2)
        assert registration_1.skier == skier
        assert registration_2.skier == skier2

    def test_has_event(self):
        """is initialized with an event"""
        riding_team1 = RidingTeam("Bullseye", "Thomas")
        riding_team2 = RidingTeam("Cheese Puff", "Jen")
        event = Event(15000, "Steamboat Springs")
        event2 = Event(25000, "Leadville")
        skier = Skier("Farhan")
        skier2 = Skier("Kip")

        registration_1 = Registration(riding_team1, skier, event)
        registration_2 = Registration(riding_team2, skier2, event2)
        assert registration_1.event == event
        assert registration_2.event == event2

    def test_riding_team_is_correct_type(self):
        """Registration has a riding_team of type RidingTeam"""
        riding_team1 = RidingTeam("Bullseye", "Thomas")
        riding_team2 = RidingTeam("Cheese Puff", "Jen")
        event = Event(15000, "Steamboat Springs")
        event2 = Event(25000, "Leadville")
        skier = Skier("Farhan")
        skier2 = Skier("Kip")

        registration_1 = Registration(riding_team1, skier, event)
        registration_2 = Registration(riding_team2, skier2, event2)
        assert type(registration_1.riding_team) == RidingTeam
        assert type(registration_2.riding_team) == RidingTeam
        
        with pytest.raises(Exception):
            registration = Registration("riding_team1", skier, event)

    def test_skier_is_correct_type(self):
        """Registration has a skier of type Skier"""
        riding_team1 = RidingTeam("Bullseye", "Thomas")
        riding_team2 = RidingTeam("Cheese Puff", "Jen")
        event = Event(15000, "Steamboat Springs")
        event2 = Event(25000, "Leadville")
        skier = Skier("Farhan")
        skier2 = Skier("Kip")

        registration_1 = Registration(riding_team1, skier, event)
        registration_2 = Registration(riding_team2, skier2, event2)
        assert type(registration_1.skier) == Skier
        assert type(registration_2.skier) == Skier
        
        with pytest.raises(Exception):
            registration = Registration(riding_team1, "skier", event)

    def test_event_is_correct_type(self):
        """Registration has an event of type Event"""
        riding_team1 = RidingTeam("Bullseye", "Thomas")
        riding_team2 = RidingTeam("Cheese Puff", "Jen")
        event = Event(15000, "Steamboat Springs")
        event2 = Event(25000, "Leadville")
        skier = Skier("Farhan")
        skier2 = Skier("Kip")

        registration_1 = Registration(riding_team1, skier, event)
        registration_2 = Registration(riding_team2, skier2, event2)
        assert type(registration_1.event) == Event
        assert type(registration_2.event) == Event
        
        with pytest.raises(Exception):
            registration = Registration(riding_team1, skier, "leadville")


    def test_get_all_registrations(self):
        """test Registration class all attribute"""
        Registration.all = []
        riding_team1 = RidingTeam("Bullseye", "Thomas")
        riding_team2 = RidingTeam("Cheese Puff", "Jen")
        event = Event(15000, "Steamboat Springs")
        event2 = Event(25000, "Leadville")
        skier = Skier("Farhan")
        skier2 = Skier("Kip")

        registration_1 = Registration(riding_team1, skier, event)
        registration_2 = Registration(riding_team2, skier2, event2)
        registration_3 = Registration(riding_team1, skier2, event2)
        registration_4 = Registration(riding_team2, skier, event)
        assert len(Registration.all) == 4
        assert registration_1 in Registration.all
        assert registration_2 in Registration.all
        assert registration_3 in Registration.all
        assert registration_4 in Registration.all
