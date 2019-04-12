world_map = {
    'MASTER_BEDROOM': {
        'NAME': "Joseph room",
        'DESCRIPTION': "This is the room you start in. ",
        'PATHS': {
            'NORTH': "KITCHEN"
        }
    },
    'KITCHEN': {
        'NAME': "The kitchen",
        'DESCRIPTION': "This is the kitchen here is where I eat.",
        'PATHS': {
            'EAST': "MASTER_ROOM"
        }
    },
    'EXIT_DOOR': {
        'NAME': "Exit door",
        'DESCRIPTION': "There is and exit door here I can go outside.",
        'PATHS': {
            'SOUTH': "LIVING_ROOM"
        }
    },
    'Living_Room':{
        'NAME': "Living Room",
        'DESCRIPTION': "I'm in the living room.",
        'PATHS': {
            'WEST': "EXIT_DOOR"
        }
    },
    'Restroom':{
        'NAME': "RESTROOM",
        'DESCRIPTION': "I'm in the restroom now",
        'PATHS': {
            'NORTH': "LIVING_Room"
        }
    },
}