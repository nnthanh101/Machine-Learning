def reward_function(params):
    '''
    Optimized version of the reward function that:
    1. Prioritizes staying close to the center line.
    2. Ensures the agent stays within the track borders.
    3. Considers speed for an overall performance boost.
    '''
    
    # Extract relevant parameters: 
    # whether all wheels are on track, distance from center, track width, and speed
    all_wheels_on_track  = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width          = params['track_width']
    speed                = params['speed']
    
    # Initialize the reward with a low default value to discourage off-track driving
    reward = 1e-3
    
    # Define a marker at 10% of the track width for center-line driving
    marker_center = 0.1 * track_width
    
    # 1. Prioritize center-line driving by assigning the highest reward for being close to the center
    if distance_from_center <= marker_center:
        reward = 1.0

    # 2. If all wheels are on track and the car is within half the track width from the center,
    #    Assign a moderate reward, 
    elif all_wheels_on_track and distance_from_center <= (0.5 * track_width):
        reward = 0.5

    # 3. Incorporate speed into the reward. 
    #    The faster the car, the higher the reward, up to a maximum speed of 3.5 m/s
    speed_factor = speed / 3.5
    reward *= speed_factor

    # Return the reward as a float value, 
    # ensuring it's at least 1e-3 to provide some feedback for undesirable actions
    return float(max(reward, 1e-3))
