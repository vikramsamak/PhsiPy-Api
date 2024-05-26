TAGS = {
    "SUBAUTOMATIC": "Subautomatic Endpoints",
    "NLM": "NLM Enpoints",
}

ROUTE_PARAMS = {
    "ELECTRICITY": {
        "FORCE_ELECTROSTATICS": {
            "tags": ["Electricity Endpoints"],
            "summary": "Calculate electrostatic force",
            "description": "This endpoint calculates the electrostatic force between two charges.",
        },
        "RESISTANCE": {
            "tags": ["Electricity Endpoints"],
            "summary": "Calculate electrical resistance",
            "description": "This endpoint calculates the electrical resistance given voltage and current.",
        },
        "CURRENT": {
            "tags": ["Electricity Endpoints"],
            "summary": "Calculate electric current",
            "description": "This endpoint calculates the electric current given voltage and resistance.",
        },
        "VOLTAGE": {
            "tags": ["Electricity Endpoints"],
            "summary": "Calculate electric voltage",
            "description": "This endpoint calculates the electric voltage given current and resistance.",
        },
        "POWER": {
            "tags": ["Electricity Endpoints"],
            "summary": "Calculate electric power",
            "description": "This endpoint calculates the electric power given voltage and current.",
        },
    },
    "SUBAUTOMATIC": {},
    "NLM": {
        "FORCE": {"tags": ["NLM Enpoints"]},
        "MOMENTUM": {"tags": ["NLM Enpoints"]},
        "RECOIL_VELOCITY": {"tags": ["NLM Enpoints"]},
    },
}
