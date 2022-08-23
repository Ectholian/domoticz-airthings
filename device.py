class AirthingsDevice:
    ""
    model = str
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
    model = "wave"
    co2 = False
    humidity = True
    mold = False
    pm25 = False
    pressure = False
    radon = True
    temp = True
    voc = False

class AirthingsWaveMini(AirthingsDevice):
    model = "wave-mini"
    co2 = False
    humidity = True
    mold = True
    pm25 = False
    pressure = False
    radon = False
    temp = True
    voc = True
    
class AirthingsWavePlus(AirthingsDevice):
    model = "wave-plus"
    co2 = True
    humidity = True
    mold = False
    pm25 = False
    pressure = True
    radon = True
    temp = True
    voc = True
    
class AirthingsWaveRadon(AirthingsDevice):
    model = "wave-radon"
    co2 = False
    humidity = True
    mold = False
    pm25 = False
    pressure = False
    radon = True
    temp = True
    voc = False
    
class AirthingsViewPlus(AirthingsDevice):
    model = "view-plus"
    co2 = True
    humidity = True
    mold = False
    pm25 = True
    pressure = True
    radon = True
    temp = True
    voc = True
    
class AirthingsViewPollution(AirthingsDevice):
    model = "view-pollution"
    co2 = False
    humidity = True
    mold = False
    pm25 = True
    pressure = False
    radon = False
    temp = True
    voc = False
    
class AirthingsViewRadon(AirthingsDevice):
    model = "view-radon"
    co2 = False
    humidity = True
    mold = False
    pm25 = False
    pressure = False
    radon = True
    temp = True
    voc = False

@unique
class domoticzType(IntEnum):
    TEMP = 80,
    HUMIDITY = 81,
    GENERAL = 243
    AIRQUALITY = 249

@unique
class domoticzSubtype(IntEnum):
    HUMIDITY = 1,
    AIRQUALIT =: 1,
    TEMP = 5,
    GENERAL_PRESSURE = 9,
    GENERAL_CUSTOM = 31

@unique
class Unit(IntEnum):
    """
    Device Unit numbers
    Define here your units numbers. These can be used to update your devices.
    Be sure the these have a unique number!
    """
    CO2 = 1
    HUMIDITY = 2
    MOLD = 3
    PM25 = 4
    PRESSURE = 5
    RADON = 6
    TEMP = 7
    VOC = 8
    
 UNITS = [
        # id, name, type, subtype, options, used
        [Unit.CO2, "Carbon Dioxide", domoticzType.AIRQUALITY, domoticzSubtype.AIRQUALITY, {}],
        [Unit.HUMIDITY, "Humidity", domoticType.HUMIDITY, domoticzSubtype.HUMIDITY, {}],
        [Unit.MOLD, "Mold Risk", domoticzType.GENERAL, domoticzSubtype.GENERAL_CUSTOM, {'Custom': '1;0-10'}],
        [Unit.PM25, "Particulate Matter 2.5", domoticzType.GENERAL, domoticzSubtype.GENERAL_CUSTOM, {'Custom': '1;ug/m3'}],
        [Unit.PRESSURE, "Air Pressure", domoticzType.GENERAL, domoticzSubtype.GENERAL_PRESSURE, {],
        [Unit.RADON, "Radon", domoticzType.GENERAL, domoticzSubtype.GENERAL_CUSTOM, {'Custom': '1;Bq/m3'}],
        [Unit.TEMP, "Temperature", domoticzType.TEMP, domoticzSubtype.TEMP, {}],
        [Unit.VOC, "Airborne Chemicals", domoticzType.GENERAL, domoticzSubtype.GENERAL_CUSTOM, {'Custom': '1;ppb'}]
