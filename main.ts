function car_back() {
    mecanumRobot.Motor(LR.Upper_left, MD.Back, 75)
    mecanumRobot.Motor(LR.Lower_left, MD.Back, 75)
    mecanumRobot.Motor(LR.Upper_right, MD.Back, 75)
    mecanumRobot.Motor(LR.Lower_right, MD.Back, 75)
}

function car_left() {
    mecanumRobot.Motor(LR.Upper_left, MD.Back, 75)
    mecanumRobot.Motor(LR.Lower_left, MD.Back, 75)
    mecanumRobot.Motor(LR.Upper_right, MD.Forward, 75)
    mecanumRobot.Motor(LR.Lower_right, MD.Forward, 75)
}

function car_forward() {
    mecanumRobot.Motor(LR.Upper_left, MD.Forward, 75)
    mecanumRobot.Motor(LR.Lower_left, MD.Forward, 75)
    mecanumRobot.Motor(LR.Upper_right, MD.Forward, 75)
    mecanumRobot.Motor(LR.Lower_right, MD.Forward, 75)
}

function car_right() {
    mecanumRobot.Motor(LR.Upper_left, MD.Forward, 75)
    mecanumRobot.Motor(LR.Lower_left, MD.Forward, 75)
    mecanumRobot.Motor(LR.Upper_right, MD.Back, 75)
    mecanumRobot.Motor(LR.Lower_right, MD.Back, 75)
}

irRemote.connectInfrared(DigitalPin.P9)
let val = 0
let val2 = 0
basic.forever(function on_forever() {
    
    val = irRemote.returnIrButton()
    basic.pause(1000)
    if (val != 0) {
        val2 = val
        if (val2 == 70) {
            car_forward()
        } else if (val2 == 68) {
            car_left()
        } else if (val2 == 67) {
            car_right()
        } else if (val2 == 21) {
            car_back()
        } else if (val2 == 64) {
            mecanumRobot.state(MotorState.stop)
        } else {
            
        }
        
    }
    
})
