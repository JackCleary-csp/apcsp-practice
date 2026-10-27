"""Game Status: refactor render_status without changing its behavior."""

def clamp(value, min, max):
    if value < min:
        value = min
    elif value > max:
        value = max
    return value

def make_bar(shown_type, max, width):
    bar_filled = shown_type * 10 // max
    bar = "["
    for pos in range(width):
        if pos < bar_filled:
            bar = bar + "#"
        else:
            bar = bar + "-"
    bar = bar + "]"
    return bar


def format_time(seconds):
    minutes = seconds // 60
    remainder = seconds % 60
    text = str(minutes) + ":"
    if remainder < 10:
        text = text + "0"
    text = text + str(remainder)
    return text

def score_select(scores):
    total = 0
    highest = scores[0]
    strong_count = 0
    for score in scores:
        total += score
        if score > highest:
            score = highest
        if score >= 80:
            strong_count += 1
        if total < 100:
            level = "Rookie"
        elif level < 250:
            level = "Skilled"
        else:
            level = "Expert"
        return level, highest, strong_count, total

def render_status(name, health, energy, elapsed_seconds, best_seconds, scores):
    # Keep this function's name, parameters, and returned report.
    # Add your own helper functions above it.

    # Bound the two meters.
    shown_health = clamp(health, 0, 100)
    shown_energy = clamp(energy, 0, 60)


    # Build two bars. // keeps the whole-number part of the division.
    health_bar = make_bar(shown_health, 100, 10)
    energy_bar = make_bar(shown_energy, 60, 10)

    # Format two durations.
    
    elapsed_text = format_time(elapsed_seconds)
    best_text = format_time(best_seconds)


    # Summarize the recent scores.
    
    level, total, highest, strong_count = score_select(scores)

    # Return one report. \n separates its lines; there is no final \n.
    report = "PLAYER: " + name
    report = report + "\nHealth  " + health_bar + " " + str(shown_health) + "/100"
    report = report + "\nEnergy  " + energy_bar + " " + str(shown_energy) + "/60"
    report = report + "\nLevel:  " + level
    report = report + "\nTime:   " + elapsed_text
    report = report + "\nBest:   " + best_text
    report = report + "\nRecent: total=" + str(total)
    report = report + ", best=" + str(highest) + ", 80+=" + str(strong_count)
    return report


# Supplied demo. This guard keeps the demo from running when tests import the file.
if __name__ == "__main__":
    print(render_status("Nova", 75, 18, 125, 119, [40, 50, 90]))
    print()
    print(render_status("Orion", 110, -4, 61, 60, [80, 80, 90]))
