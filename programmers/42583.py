def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    truck_index = 0
    while True:
        bridge.pop(0)
        answer += 1
        if truck_index == len(truck_weights):
            break
        if sum(bridge) + truck_weights[truck_index] <= weight:
            bridge.append(truck_weights[truck_index])
            truck_index += 1
        else:
            bridge.append(0)
    while sum(bridge) > 0:
        bridge.pop(0)
        answer += 1
        
    return answer