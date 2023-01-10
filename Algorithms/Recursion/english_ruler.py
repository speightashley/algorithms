def draw_line(tick_length, tick_label=""):
    """Draw one line with given tick length"""
    line = "-" * tick_length

    if tick_label:
        line += " " + tick_label
    print(line)


def draw_interval(center_length):
    """Draw tick interval based upon a crental tick length"""
    if center_length > 0:  # Stop when length gets to 0
        draw_interval(center_length - 1)  # Recursivley draw top ticks
        draw_line(center_length)  # Draw centre tick
        draw_interval(center_length - 1)  # Recursivley draw bottom ticks


def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length"""
    draw_line(major_length, "0")  # Draw inch 0 line
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)  # Draw interior ticks for inch
        draw_line(major_length, str(j))  # draw inch j line and label


draw_ruler(10, 3)
