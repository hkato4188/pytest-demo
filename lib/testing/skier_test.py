#!/usr/bin/env python3

import pytest

from classes.skier import Skier
from classes.event import Event
from classes.riding_team import RidingTeam
from classes.registration import Registration



class TestSkier:
    """Skier in skier.py"""

    def test_has_name(self):
        """skier is initialized with name"""
        skier = Skier("Steve")
        assert skier.name == "Steve"

    def test_can_change_name(self):
        """skier name can be changed"""
        skier = Skier("Steve")
        skier.name = "Stove"
        assert skier.name == "Stove"

    def test_skier_name_is_str(self):
        """skier name is a string"""
        skier = Skier("Steve")
        assert isinstance(skier.name, str)

        with pytest.raises(Exception):
            skier.name = 1

    def test_skier_name_length(self):
        """skier name is between 1 and 15 characters"""
        skier = Skier("Steve")
        assert len(skier.name) == 5

        with pytest.raises(Exception):
            skier.name = "NameLongerThan15Characters"

        with pytest.raises(Exception):
            skier.name = ""

    def test_has_many_registrations(self):
        """skier has many registrations"""
        steamboat_springs = Event(15000, "Steamboat Springs")
        riding_team1 = RidingTeam("Bullseye", "Thomas")
        riding_team2 = RidingTeam("Dart", "Princeton")
        skier = Skier("Farhan")
        skier_2 = Skier("Tess")
        registration_1 = Registration(riding_team1, skier, steamboat_springs)
        registration_2 = Registration(riding_team2, skier, steamboat_springs)
        registration_3 = Registration(riding_team1, skier_2, steamboat_springs)

        assert len(skier.registrations()) == 2
        assert not registration_3 in skier.registrations()
        assert registration_1 in skier.registrations()
        assert registration_2 in skier.registrations()

    def test_registrations_of_type_registration(self):
        """skier registrations are of type Registration"""
        leadville = Event(4000, "Leadville")
        riding_team1 = RidingTeam("Flash", "Curtis")
        riding_team2 = RidingTeam("Lightning", "John")
        skier = Skier("Farhan")
        registration_1 = Registration(riding_team1, skier, leadville)
        registration_2 = Registration(riding_team2, skier, leadville)
        registration_3 = Registration(riding_team1, skier, leadville)

        assert isinstance(skier.registrations()[0], Registration)
        assert isinstance(skier.registrations()[1], Registration)
        assert isinstance(skier.registrations()[2], Registration)

    def test_has_many_events(self):
        """skier has many events."""
        event = Event(3400, "Canturbery Park")
        event_2 = Event(1500, "Bellevue")
        riding_team1 = RidingTeam("Tornado", "Teddy")
        skier = Skier("BreElle")
        registration_1 = Registration(riding_team1, skier, event)
        registration_2 = Registration(riding_team1, skier, event_2)

        assert event in skier.events()
        assert event_2 in skier.events()

    def test_has_unique_events(self):
        """skier has unique list of all the events they have registered to participate in."""
        event = Event(3400, "Canturbery Park")
        event_2 = Event(1500, "Bellevue")
        riding_team1 = RidingTeam("Tornado", "Teddy")
        riding_team2 = RidingTeam("Mustang", "Collin")
        skier = Skier("BreElle")
        registration_1 = Registration(riding_team1, skier, event)
        registration_2 = Registration(riding_team1, skier, event_2)
        registration_3 = Registration(riding_team2, skier, event)

        assert len(set(skier.events())) == len(skier.events())
        assert len(skier.events()) == 2

    def test_skier_create_registration(self):
        """test create_registration()"""
        event = Event(9000, "Canturbery Park")
        riding_team = RidingTeam("Bullet", "Doug")
        skier = Skier("Michael")
        skier.create_registration(riding_team, event)
        skier.create_registration(riding_team, event)

        assert len(skier.registrations()) == 2
        assert event in skier.events()
