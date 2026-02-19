def dividing_alerts_to_queues(alerts: list[dict]):
    urgent_queue = []
    normal_queue = []

    for alert in alerts:
        if (alert["weapons_count"] > 0 or
            alert["distance_from_fence_m"] <= 50 or
            alert["people_count"] >= 8 or
            alert["vehicle_type"] == "truck"
        ) or ((alert["people_count"] >= 4 and alert["distance_from_fence_m"] <= 150) or
              (alert["people_count"] >= 3 and alert["vehicle_type"] <= "jeep")):
            
            alert["priority"] = "URGENT"
            urgent_queue.append(alert)
        else:
            alert["priority"] = "NORMAL"
            normal_queue.append(alert)           
    return urgent_queue, normal_queue
