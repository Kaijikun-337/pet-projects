# A list of 3 messy responses from the API
api_responses = [
    # Case 1: Perfect data
    {
        "status": "ok",
        "room": {"id": "Math_101", "users": ["Alex", "Bob"]},
        "meta": {"version": "v2"}
    },
    # Case 2: No users list (Key missing)
    {
        "status": "ok",
        "room": {"id": "Eng_202"}, 
        "meta": None
    },
    # Case 3: Total failure (Room is None)
    {
        "status": "error",
        "room": None,
        "meta": {"version": "v1"}
    }
]

print("--- PROCESSING JITSI DATA ---")

for response in api_responses:
    room = response.get("room") or {}
    room_id = response.get("room") or "No room"
    users = room.get("users") or "0"
    meta = response.get("meta") or "v?"
        
    print("Room id:", room_id, "\n users:", users, "\n meta", meta)