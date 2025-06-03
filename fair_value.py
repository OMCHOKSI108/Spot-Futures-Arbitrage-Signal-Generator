def calculate_fair_value(spot, rf, x, d):
    return spot * (1 + (rf * x / 365)) - d