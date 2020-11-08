class AircraftType():

    def __init__(self, name, role, empty_weight, max_to_weight, clean_lift2drag, dirty_lift2drag, tsfc):
        self.name = name
        self.role = role
        self.empty_weight = empty_weight
        self.max_to_weight = max_to_weight
        self.clean_lift2drag = clean_lift2drag
        self.dirty_lift2drag = dirty_lift2drag
        self.tsfc = tsfc

#class Aicraft(AircraftType):

    #def __init__(self,weight):