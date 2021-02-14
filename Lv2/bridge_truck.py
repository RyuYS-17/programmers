def get_truck_on_bridge(on_bridge, truck_weights, weight, second, on_bridge_time):
    if(truck_weights):
        next_truck = truck_weights[0]
        if (next_truck+sum(on_bridge) <= weight):
            next_truck = truck_weights.pop(0)
            on_bridge.append(next_truck)
            on_bridge_time.append(second)

def arrive_truck(on_bridge, arrival, second, bridge_length, on_bridge_time):
    if (on_bridge):
        if (second - on_bridge_time[0]) == bridge_length:
            on_bridge_time.pop(0)
            arrival.append(on_bridge.pop(0))

def solution(bridge_length, weight, truck_weights):
    on_bridge = []; on_bridge_time = []; arrival = []; second = 0
    total_truck = len(truck_weights)
    while(len(arrival) < total_truck):
        second += 1
        arrive_truck(on_bridge, arrival, second, bridge_length, on_bridge_time)
        get_truck_on_bridge(on_bridge, truck_weights, weight, second, on_bridge_time)
    return second

if __name__ == "__main__":
    bridge_length = 2
    weight = 10
    truck_weights = [7,4,5,6]
    assert solution(bridge_length, weight, truck_weights) == 8
