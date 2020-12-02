let right: number;
let left: number;
//  value for the differential between the two sensors.
//  you can change this value to make it more or less sensitive.
let diff = 100
basic.showIcon(IconNames.Asleep)
input.buttonIsPressed(Button.A)
input.buttonIsPressed(Button.B)
gigglebot.stop()
gigglebot.setSpeed(gigglebotWhichMotor.Both, 50)
while (true) {
    if (input.buttonIsPressed(Button.A)) {
        basic.showIcon(IconNames.Heart)
        while (true) {
            basic.showIcon(IconNames.Happy)
            right = gigglebot.lightReadSensor(gigglebotWhichTurnDirection.Right)
            left = gigglebot.lightReadSensor(gigglebotWhichTurnDirection.Left)
            if (right > left + diff) {
                gigglebot.turn(gigglebotWhichTurnDirection.Right)
            } else if (left > right + diff) {
                gigglebot.turn(gigglebotWhichTurnDirection.Left)
            } else {
                gigglebot.driveStraight(gigglebotWhichDriveDirection.Forward)
            }
            
            if (input.buttonIsPressed(Button.B)) {
                gigglebot.stop()
                basic.showIcon(IconNames.Asleep)
                break
            }
            
        }
    }
    
}
