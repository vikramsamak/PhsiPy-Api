from Dictionaries import NlmDictionary


def get_force(req):
    return {"defintion": NlmDictionary.NlmDict["force"]}


def get_momentum(req):
    return {"defintion": NlmDictionary.NlmDict["momentum"]}


def get_recoil_velocity(req):
    return {"defintion": NlmDictionary.NlmDict["recoil_velocity"]}
