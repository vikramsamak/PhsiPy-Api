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
        "FORCE": {
            "tags": ["NLM Endpoints"],
            "summary": "Force Calculation",
            "description": "Calculate the force exerted on an object given mass and acceleration.",
        },
        "MOMENTUM": {
            "tags": ["NLM Endpoints"],
            "summary": "Momentum Calculation",
            "description": "Compute the momentum of an object given its mass and velocity.",
        },
        "RECOIL_VELOCITY": {
            "tags": ["NLM Endpoints"],
            "summary": "Recoil Velocity Calculation",
            "description": "Determine the recoil velocity of an object after a collision or explosion, given the masses and velocities of the objects involved.",
        },
    },
}
