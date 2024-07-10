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
    "SUBAUTOMATIC": {
        "MASS_ENERGY_EQUIVALENCE": {
            "tags": ["Subautomatic Endpoints"],
            "summary": "Calculate mass-energy equivalence",
            "description": "This endpoint calculates the mass-energy equivalence using Einstein's E=mc² formula.",
        },
        "BINDING_ENERGY": {
            "tags": ["Subautomatic Endpoints"],
            "summary": "Calculate nuclear binding energy",
            "description": "This endpoint calculates the binding energy of a nucleus given the mass defect.",
        },
        "DE_BROGILE_WAVELENGTH": {
            "tags": ["Subautomatic Endpoints"],
            "summary": "Calculate De Broglie wavelength",
            "description": "This endpoint calculates the De Broglie wavelength of a particle given its momentum.",
        },
        "BOHR_RADIUS": {
            "tags": ["Subautomatic Endpoints"],
            "summary": "Calculate Bohr radius",
            "description": "This endpoint calculates the Bohr radius of the hydrogen atom.",
        },
        "ENERGY_LEVEL_HYDROGEN": {
            "tags": ["Subautomatic Endpoints"],
            "summary": "Calculate energy level of hydrogen atom",
            "description": "This endpoint calculates the energy levels of the hydrogen atom using the Rydberg formula.",
        },
        "RADIOACTIVE_DECAY": {
            "tags": ["Subautomatic Endpoints"],
            "summary": "Calculate radioactive decay",
            "description": "This endpoint calculates the remaining quantity of a radioactive substance after a given period using its decay constant.",
        },
        "HALF_LIFE": {
            "tags": ["Subautomatic Endpoints"],
            "summary": "Calculate half-life",
            "description": "This endpoint calculates the half-life of a radioactive substance given its decay constant.",
        },
    },
    "NLM": {
        "FORCE": {
            "tags": ["NLM Endpoints"],
            "summary": "Calculate Force",
            "description": "Calculate the force exerted on an object given mass and acceleration.",
        },
        "MOMENTUM": {
            "tags": ["NLM Endpoints"],
            "summary": "Calculate Momentum",
            "description": "Compute the momentum of an object given its mass and velocity.",
        },
        "RECOIL_VELOCITY": {
            "tags": ["NLM Endpoints"],
            "summary": "Calculate Recoil Velocity",
            "description": "Determine the recoil velocity of an object after a collision or explosion, given the masses and velocities of the objects involved.",
        },
    },
}
