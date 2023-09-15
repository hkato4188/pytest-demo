#!/usr/bin/env python3

import pytest

from classes.skier import Skier
from classes.event import Event
from classes.riding_team import RidingTeam
from classes.registration import Registration



class TestRidingTeam:
    """RidingTeam in riding_team.py"""

    def test_has_horse_name(self):
        """riding_team is initialized with a horse_name"""
        riding_team = RidingTeam("Bullseye", "Farhan")
        assert riding_team.horse_name == "Bullseye"

    def test_can_change_name(self):
        """riding_team horse_name can be changed"""
        riding_team = RidingTeam("Bullseye", "Farhan")
        riding_team.horse_name = "Bullet"
        assert riding_team.horse_name == "Bullet"

    def test_riding_team_horse_name_is_str(self):
        """riding_team horse_name is a string"""
        riding_team = RidingTeam("Bullseye", "Farhan")
        assert isinstance(riding_team.horse_name, str)

        with pytest.raises(Exception):
            riding_team.horse_name = 1

    def test_riding_team_horse_name_length(self):
        """riding_team horse_name is between 1 and 15 characters"""
        riding_team = RidingTeam("Bullseye", "Farhan")
        assert len(riding_team.horse_name) == 8

        with pytest.raises(Exception):
            riding_team.horse_name = "NameLongerThan15Characters"

        with pytest.raises(Exception):
            riding_team.horse_name = ""

    def test_has_rider_name(self):
        """riding_team is initialized with a rider_name"""
        riding_team = RidingTeam("Bullseye", "Farhan")
        assert riding_team.rider_name == "Farhan"

    def test_can_change_name(self):
        """riding_team rider_name can be changed"""
        riding_team = RidingTeam("Bullseye", "Farhan")
        riding_team.rider_name = "Hiro"
        assert riding_team.rider_name == "Hiro"

    def test_riding_team_rider_name_is_str(self):
        """riding_team rider_name is a string"""
        riding_team = RidingTeam("Bullseye", "Farhan")
        assert isinstance(riding_team.rider_name, str)

        with pytest.raises(Exception):
            riding_team.rider_name = 1

    def test_riding_team_rider_name_length(self):
        """riding_team rider_name is between 1 and 15 characters"""
        riding_team = RidingTeam("Bullseye", "Farhan")
        assert len(riding_team.rider_name) == 6

        with pytest.raises(Exception):
            riding_team.rider_name = "NameLongerThan15Characters"

        with pytest.raises(Exception):
            riding_team.rider_name = ""

    def test_has_many_registrations(self):
        """riding_team has many registrations"""
        steamboat_springs = Event(15000, "Steamboat Springs")
        riding_team1 = RidingTeam("Bullseye", "Thomas")
        riding_team2 = RidingTeam("Dart", "Princeton")
        skier = Skier("Farhan")
        skier_2 = Skier("Tess")
        registration_1 = Registration(riding_team1, skier, steamboat_springs)
        registration_2 = Registration(riding_team2, skier, steamboat_springs)
        registration_3 = Registration(riding_team1, skier_2, steamboat_springs)

        assert len(riding_team1.registrations()) == 2
        assert registration_2 in riding_team2.registrations()
        assert registration_3 in riding_team1.registrations()
        assert registration_1 in riding_team1.registrations()

    def test_registrations_of_type_registration(self):
        """riding_team registrations are of type Registration"""
        leadville = Event(4000, "Leadville")
        riding_team1 = RidingTeam("Flash", "Curtis")
        skier_1 = Skier("Farhan")
        skier_2 = Skier("Hiro")
        skier_3 = Skier("Tess")
        registration_1 = Registration(riding_team1, skier_1, leadville)
        registration_2 = Registration(riding_team1, skier_2, leadville)
        registration_3 = Registration(riding_team1, skier_3, leadville)

        assert isinstance(riding_team1.registrations()[0], Registration)
        assert isinstance(riding_team1.registrations()[1], Registration)
        assert isinstance(riding_team1.registrations()[2], Registration)

    def test_has_many_events(self):
        """riding_team has many events."""
        event = Event(3400, "Canturbery Park")
        event_2 = Event(1500, "Bellevue")
        riding_team1 = RidingTeam("Tornado", "Teddy")
        skier = Skier("BreElle")
        registration_1 = Registration(riding_team1, skier, event)
        registration_2 = Registration(riding_team1, skier, event_2)

        assert event in riding_team1.events()
        assert event_2 in riding_team1.events()

    
    def test_riding_team_create_registration(self):
        """test create_registration()"""
        event = Event(9000, "Canturbery Park")
        riding_team = RidingTeam("Bullet", "Doug")
        skier = Skier("Michael")
        
        riding_team.create_registration(skier, event)
        riding_team.create_registration(skier, event)

        assert len(riding_team.registrations()) == 2
        assert event in riding_team.events()