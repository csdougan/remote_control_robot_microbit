def car_back():
    mecanumRobot.motor(LR.UPPER_LEFT, MD.BACK, 75)
    mecanumRobot.motor(LR.LOWER_LEFT, MD.BACK, 75)
    mecanumRobot.motor(LR.UPPER_RIGHT, MD.BACK, 75)
    mecanumRobot.motor(LR.LOWER_RIGHT, MD.BACK, 75)
def car_left():
    mecanumRobot.motor(LR.UPPER_LEFT, MD.BACK, 75)
    mecanumRobot.motor(LR.LOWER_LEFT, MD.BACK, 75)
    mecanumRobot.motor(LR.UPPER_RIGHT, MD.FORWARD, 75)
    mecanumRobot.motor(LR.LOWER_RIGHT, MD.FORWARD, 75)
def car_forward():
    mecanumRobot.motor(LR.UPPER_LEFT, MD.FORWARD, 75)
    mecanumRobot.motor(LR.LOWER_LEFT, MD.FORWARD, 75)
    mecanumRobot.motor(LR.UPPER_RIGHT, MD.FORWARD, 75)
    mecanumRobot.motor(LR.LOWER_RIGHT, MD.FORWARD, 75)
def car_right():
    mecanumRobot.motor(LR.UPPER_LEFT, MD.FORWARD, 75)
    mecanumRobot.motor(LR.LOWER_LEFT, MD.FORWARD, 75)
    mecanumRobot.motor(LR.UPPER_RIGHT, MD.BACK, 75)
    mecanumRobot.motor(LR.LOWER_RIGHT, MD.BACK, 75)
irRemote.connect_infrared(DigitalPin.P9)
val = 0
val2 = 0

def on_forever():
    global val, val2
    val = irRemote.return_ir_button()
    basic.pause(1000)
    if val != 0:
        val2 = val
        if val2 == 70:
            car_forward()
        elif val2 == 68:
            car_left()
        elif val2 == 67:
            car_right()
        elif val2 == 21:
            car_back()
        elif val2 == 64:
            mecanumRobot.state(MotorState.STOP)
        else:
            pass
basic.forever(on_forever)
