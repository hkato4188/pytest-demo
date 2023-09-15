#!/usr/bin/env python3

import pytest

from classes.skier import Skier
from classes.event import Event
from classes.riding_team import RidingTeam
from classes.registration import Registration

class TestEvent:
    """Event in event.py"""

    def test_has_capacity(self):
        """Event is initialized with a capacity"""
        leadville = Event(1500, "Leadville")
        assert leadville.capacity == 1500

    def test_capacity_is_string(self):
        """Event is initialized with a capacity of type int"""
        leadville = Event(1500, "Leadville")
        assert isinstance(leadville.capacity, int)

    def test_capacity_setter(self):
        """Cannot change the capacity of the event"""
        leadville = Event(1500, "Leadville")

        with pytest.raises(Exception):
            leadville.capacity = 2400

    def test_has_location(self):
        """Event is initialized with a location"""
        leadville = Event(1500, "Leadville")
        assert leadville.location == "Leadville"

    def test_location_is_string(self):
        """Event is initialized with a location of type str"""
        leadville = Event(1500, "Leadville")
        assert isinstance(leadville.location, str)

    def test_location_setter(self):
        """Cannot change the location of the event"""
        leadville = Event(1500, "Leadville")

        with pytest.raises(Exception):
            leadville.location = "Plumbum"

    def test_has_many_registrations(self):
        """Event has many registrations"""
        steamboat_springs = Event(15000, "Steamboat Springs")
        leadville = Event(1500, "Leadville")
        riding_team1 = RidingTeam("Bullseye", "Thomas")
        riding_team2 = RidingTeam("Dart", "Princeton")
        skier = Skier("Farhan")
        skier_2 = Skier("Tess")
        registration_1 = Registration(riding_team1, skier, steamboat_springs)
        registration_2 = Registration(riding_team2, skier, steamboat_springs)
        registration_3 = Registration(riding_team1, skier_2, steamboat_springs)
        registration_4 = Registration(riding_team1, skier_2, leadville)

        assert len(steamboat_springs.registrations()) == 3
        assert registration_1 in steamboat_springs.registrations()
        assert registration_2 in steamboat_springs.registrations()
        assert registration_3 in steamboat_springs.registrations()
        assert not registration_4 in steamboat_springs.registrations()

    def test_registrations_of_type_registration(self):
        """event registrations are of type Registration"""
        leadville = Event(4000, "Leadville")
        riding_team1 = RidingTeam("Flash", "Curtis")
        riding_team2 = RidingTeam("Lightning", "John")
        skier = Skier("Farhan")
        registration_1 = Registration(riding_team1, skier, leadville)
        registration_2 = Registration(riding_team2, skier, leadville)
        registration_3 = Registration(riding_team1, skier, leadville)

        assert isinstance(leadville.registrations()[0], Registration)
        assert isinstance(leadville.registrations()[1], Registration)
        assert isinstance(leadville.registrations()[2], Registration)

    def test_has_many_skiers(self):
        """Event has many skiers."""
        steamboat_springs = Event(15000, "Steamboat Springs")
        riding_team1 = RidingTeam("Bullseye", "Thomas")
        riding_team2 = RidingTeam("Dart", "Princeton")
        skier = Skier("Farhan")
        skier_2 = Skier("Tess")
        skier_3 = Skier("Curtis")
        skier_4 = Skier("John")
        registration_1 = Registration(riding_team1, skier, steamboat_springs)
        registration_2 = Registration(riding_team2, skier_3, steamboat_springs)
        registration_3 = Registration(riding_team1, skier_2, steamboat_springs)
        registration_4 = Registration(riding_team1, skier_4, steamboat_springs)


        assert skier in steamboat_springs.skiers()
        assert skier_2 in steamboat_springs.skiers()
        assert skier_3 in steamboat_springs.skiers()
        assert skier_4 in steamboat_springs.skiers()

    def test_has_unique_skiers(self):
        """skier has unique list of all the events they have registered to participate in."""
        event = Event(15000, "Steamboat Springs")
        riding_team1 = RidingTeam("Bullseye", "Thomas")
        riding_team2 = RidingTeam("Dart", "Princeton")
        skier = Skier("Farhan")
        skier_2 = Skier("Tess")
        skier_3 = Skier("Curtis")
        skier_4 = Skier("John")
        registration_1 = Registration(riding_team1, skier, event)
        registration_2 = Registration(riding_team2, skier_3, event)
        registration_3 = Registration(riding_team1, skier_2, event)
        registration_4 = Registration(riding_team1, skier_4, event)
        registration_4 = Registration(riding_team2, skier_4, event)
        
        assert len(set(event.skiers())) == len(event.skiers())
        assert len(event.skiers()) == 4

    def test_has_many_riding_teams(self):
        """Event has many riding_teams."""
        steamboat_springs = Event(15000, "Steamboat Springs")
        riding_team1 = RidingTeam("Bullseye", "Thomas")
        riding_team2 = RidingTeam("Dart", "Princeton")
        riding_team3 = RidingTeam("Blue", "Tess")
        riding_team4 = RidingTeam("Ms. Pam", "Hiro")
        skier = Skier("Farhan")
        skier_2 = Skier("Teddy")
        skier_3 = Skier("Curtis")
        skier_4 = Skier("John")
        registration_1 = Registration(riding_team1, skier, steamboat_springs)
        registration_2 = Registration(riding_team2, skier_2, steamboat_springs)
        registration_3 = Registration(riding_team3, skier_3, steamboat_springs)
        registration_4 = Registration(riding_team4, skier_4, steamboat_springs)


        assert riding_team1 in steamboat_springs.riding_teams()
        assert riding_team2 in steamboat_springs.riding_teams()
        assert riding_team3 in steamboat_springs.riding_teams()
        assert riding_team4 in steamboat_springs.riding_teams()

    def test_get_number_of_skiers(self):
        """test num_skiers()"""
        steamboat_springs = Event(15000, "Steamboat Springs")
        riding_team1 = RidingTeam("Bullseye", "Thomas")
        riding_team2 = RidingTeam("Dart", "Princeton")
        riding_team3 = RidingTeam("Blue", "Tess")
        riding_team4 = RidingTeam("Ms. Pam", "Hiro")
        skier = Skier("Farhan")
        skier_2 = Skier("Teddy")
        skier_3 = Skier("Curtis")
        skier_4 = Skier("John")
        registration_1 = Registration(riding_team1, skier, steamboat_springs)
        registration_2 = Registration(riding_team2, skier_2, steamboat_springs)
        registration_3 = Registration(riding_team3, skier_3, steamboat_springs)
        registration_4 = Registration(riding_team4, skier_4, steamboat_springs)

        assert steamboat_springs.num_skiers() == 4

    