class Voter(object):
    def __init__(self, fullname, gender, dob, national_id, reg_center, consitituency, district):
        self.fullname = fullname
        self.gender = gender
        self.dob = dob 
        self.national_id = national_id
        self.reg_center = reg_center
        self.constituency = consitituency
        self.district = district

    def to_json(self):
        return {
            "fullname": self.fullname,
            "gender": self.gender,
            "dob": self.dob,
            "national_id": self.national_id,
            "reg_center": self.reg_center,
            "constituency": self.constituency,
            "district": self.district
        }
        