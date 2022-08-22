class AirthingsDevice:
    ""
    model: str
    co2 = bool
    humidity = bool
    mold = bool
    pm25 = bool
    pressure = bool
    radon = bool
    temp = bool
    voc = bool
    
    @staticmethod
    def get(model):
        if model == "wave":
            return AirthingsWave()
        elif model == "wave-mini":
            return AirthingsWaveMini()
        elif model == "wave-plus":
            return AirthingsWavePlus()
        elif model == "wave-radon":
            return AirthingsWaveRadon()
        elif model == "view-plus":
            return AirthingsViewPlus()
        elif model == "view-pollution":
            return AirthingsViewPollution()
        elif model == "view-radon":
            return AirthingsViewRadon()
        else:
            raise Exception("Unsupported device " + model)
  
class AirthingsWave(AirthingsDevice):
    model: "wave"
    co2 = False
    humidity = True
    mold = False
    pm25 = False
    pressure = False
    radon = True
    temp = True
    voc = False

class AirthingsWaveMini(AirthingsDevice):
    model: "wave-mini"
    co2 = False
    humidity = True
    mold = True
    pm25 = False
    pressure = False
    radon = False
    temp = True
    voc = True
    
class AirthingsWavePlus(AirthingsDevice):
    model: "wave-plus"
    co2 = True
    humidity = True
    mold = False
    pm25 = False
    pressure = True
    radon = True
    temp = True
    voc = True
    
class AirthingsWaveRadon(AirthingsDevice):
    model: "wave-radon"
    co2 = False
    humidity = True
    mold = False
    pm25 = False
    pressure = False
    radon = True
    temp = True
    voc = False
    
class AirthingsViewPlus(AirthingsDevice):
    model: "view-plus"
    co2 = True
    humidity = True
    mold = False
    pm25 = True
    pressure = True
    radon = True
    temp = True
    voc = True
    
class AirthingsViewPollution(AirthingsDevice):
    model: "view-pollution"
    co2 = False
    humidity = True
    mold = False
    pm25 = True
    pressure = False
    radon = False
    temp = True
    voc = False
    
class AirthingsViewRadon(AirthingsDevice):
    model: "view-radon"
    co2 = False
    humidity = True
    mold = False
    pm25 = False
    pressure = False
    radon = True
    temp = True
    voc = False

print(AirthingsDevice.get("wave").model)
