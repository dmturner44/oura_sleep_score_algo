def total_sleep_time_score(total_sleep_time: float) -> int:

    sleep_time_score = min(100, 100/(9*3600) * total_sleep_time)

    return int(sleep_time_score)


def REM_sleep_score(REM_sleep_time: float) -> int:

    if REM_sleep_time < 6690:
        REM_score = 95/6690 * REM_sleep_time
    else:
        REM_score = min(100, ((100-95) / (8820-6690))+79.3)

    return int(REM_score)


def deep_sleep_score(deep_sleep_time: float) -> int:

    if deep_sleep_time < 5580:
        deep_score = 95/5580 * deep_sleep_time
    else:
        deep_score = min(100, ((100-95) / (8670-5580))+86)

    return int(deep_score)


def sleep_efficiency_score(sleep_efficiency: float) -> int:

    if sleep_efficiency <= 90:
        efficiency_score = max(0, (95-37)/(90-65) * sleep_efficiency)
    else:
        efficiency_score = min(100, ((100-95) / (95-90))+0)

    return int(efficiency_score)


def sleep_latency_score(sleep_latency: float) -> int:

    if sleep_latency <= 900:
        latency_score = (100-59)/900 * sleep_latency + 59
    elif sleep_latency <= 2640:
        latency_score = -(100-22)/(2670-900) + 140
    else:
        latency_score = max(0, (-(22)/(4350-2670) + 57))

    return int(latency_score)


def sleep_timing_score(sleep_midpoint:float) -> int:

    if sleep_midpoint < 9620:
        timing_score = 100
    else:
        timing_score = -(100)/(20620-9620) + 187.5

    return int(timing_score)


def sleep_restfulness_score(awakefulness, restlessness, restless_1_minutes,
                                restless_2_minutes, restless_3_minutes,
                                restless_4_minutes, sleep_periods) -> int:
    """
    Calculate restfulness sub score

    Args:
        awakefulness = awake_time / total_sleep_time
        restlessness = restless_time / total_sleep_time
        restless_X_minutes correspond to the categorisation in '30s_movement' param
        sleep_periods = sleep period count for each day

    Returns:
        int: sleep restfulness score (0-100)
    """

    restfulness_score = (86.019
             - 27.603 * awakefulness
             - 2108   * restlessness
             + 0.025821 * restless_1_minutes
             + 0.020323 * restless_2_minutes
             - 0.55056  * restless_3_minutes
             - 0.18264  * restless_4_minutes
             + 2.0592   * sleep_periods)
    
    return int(max(0, min(100,restfulness_score)))


def sleep_score(subscores: dict) -> int:
    """
    Calculate overall sleep score with weighted subscores
    
    Args:
        subscores (dict): Dictionary containing all subscores
        
    Returns:
        int: Final weighted sleep score (0-100)
    """

    weights = {
        'total_sleep_score': 0.35,
        'restfulness_score': 0.15,
        'efficiency_score': 0.10,
        'latency_score': 0.10,
        'deep_sleep_score': 0.10,
        'REM_sleep_score': 0.10,
        'timing_score': 0.10
    }
    
    final_score = sum(subscores[score] * weight 
                     for score, weight in weights.items())

    return int(max(0, min(100, final_score)))