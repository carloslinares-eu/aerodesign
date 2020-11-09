import os, math, openpyxl

def scan_mission_file():
    return 0


class Mission():
    def __init__ (self,id_,name,mission_type,mission_range,payload):
        self.id_ = id_
        self.name = name
        self.mission_type = mission_type
        self.range = mission_range
        self.payload = payload
        self.segments = []

    def add_mission_segment(self,mission_segment):
        self.segments.append(mission_segment)


class MissionSegment():
    def __init__ (self, id_, name, aero_setup):
        self.id_ = id_
        self.name = name
        self.aero_setup = aero_setup

    def load_aircraft_data(self, aircraft_type):
        self.tsfc = aircraft_type.tsfc
        if self.aero_setup == "dirty":
            self.lift2drag = aircraft_type.dirty_lift2drag
        elif self.aero_setup == "clean":
            self.lift2drag = aircraft_type.clean_lift2drag
        else:
            self.lift2drag = aircraft_type.clean_lift2drag
            print("Unknown aero_setup. Using clean_lift2drag for segment "+ self.id_ +"_" + self.name)
    
    def payload_drop(self, payload):
        self.weight_delta = -payload

class Cruise(MissionSegment):
    
    def __init__(self, id_, name, aero_setup, speed, lenght):
        MissionSegment.__init__(self, id_, name, aero_setup)
        self.lenght = lenght
        self.speed = speed

    def breguet(self):
            self.weight_fraction = math.exp(-self.tsfc * self.lenght / self.speed  * pow(self.lift2drag,-1))


class Gradient(MissionSegment):

    def __init__(self, id_, name, aero_setup, speed, climb_gradient, initial_altitude, final_altitude):
        MissionSegment.__init__(self, id_, name, aero_setup)
        self.climb_gradient = climb_gradient
        self.initial_altitude = initial_altitude
        self.final_altitude = final_altitude
        self.speed = speed
        self.lenght = abs(final_altitude - initial_altitude) / (climb_gradient / 100)
        self.gamma = math.atan(climb_gradient) / 180 * math.pi

    def breguet(self):
        self.weight_fraction = math.exp(-self.tsfc * self.lenght / self.speed  * (pow(self.lift2drag,-1) + self.gamma))


class Loitering(MissionSegment):

    def __init__(self, id_, name, aero_setup, endurance):
        MissionSegment.__init__(self, id_, name, aero_setup)
        self.endurance = endurance

    def breguet(self):
        self.weight_fraction  = math.exp(-self.tsfc * self.endurance / self.lift2drag)


class Estimated(MissionSegment):

    def __init__(self, id_, name, aero_setup, estimated_weight_fraction):
        MissionSegment.__init__(self, id_, name, aero_setup)
        self.estimated_weight_fraction = estimated_weight_fraction


class Combat(MissionSegment):

    def __init__(self, id_, name, aero_setup, combat_time):
        MissionSegment.__init__(self, id_, name, aero_setup)
        self.combat_time  = combat_time
    
    def breguet(self):
        self.weight_fraction  = math.exp(-self.tsfc * self.combat_time / self.lift2drag)
