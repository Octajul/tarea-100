# value for the differential between the two sensors.
# you can change this value to make it more or less sensitive.
diff = 100
basic.show_icon(IconNames.ASLEEP)
input.button_is_pressed(Button.A)
input.button_is_pressed(Button.B)
gigglebot.stop()
gigglebot.set_speed(gigglebotWhichMotor.BOTH, 50)
while True:
    if input.button_is_pressed(Button.A):
        basic.show_icon(IconNames.HEART)
        while True:
            basic.show_icon(IconNames.HAPPY)
            right=gigglebot.light_read_sensor(gigglebotWhichTurnDirection.RIGHT)
            left=gigglebot.light_read_sensor(gigglebotWhichTurnDirection.LEFT)
            if right > left+diff:
                gigglebot.turn(gigglebotWhichTurnDirection.RIGHT)
            elif left > right+diff:
                gigglebot.turn(gigglebotWhichTurnDirection.LEFT)
            else:
                gigglebot.drive_straight(gigglebotWhichDriveDirection.FORWARD)
            if input.button_is_pressed(Button.B):
                gigglebot.stop()
                basic.show_icon(IconNames.ASLEEP)
                break
