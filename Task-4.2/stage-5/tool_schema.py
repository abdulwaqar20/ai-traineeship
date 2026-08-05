TOOLS = [
    {
        "type":"function",
        "function":{
            "name":"calculator",
            "description":
            "Calculate mathematical expressions",
            "parameters":{
                "type":"object",
                "properties":{
                    "expression":{
                        "type":"string"
                    }
                },
                "required":[
                    "expression"
                ]
            }
        }
    },

    {
        "type":"function",
        "function":{
            "name":"get_current_time",
            "description":
            "Get current time of a location",
            "parameters":{
                "type":"object",
                "properties":{
                    "timezone":{
                        "type":"string"
                    }
                },
                "required":[
                    "timezone"
                ]
            }
        }
    }
]