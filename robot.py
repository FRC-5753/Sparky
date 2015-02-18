#!/usr/bin/env python3

import wpilib as w
from time import sleep

class Sparky(w.IterativeRobot):

    def robotInit(self):

        # Motors to PWM channels
        l_motor = w.Talon(0)
        r_motor = w.Talon(1)
        self.lift_motor = w.VictorSP(2)

        # Drivetrain control
        self.drivetrain = w.RobotDrive(l_motor, r_motor)

        # Joystick
        self.js0 = w.Joystick(0) # Xbox controller
        self.js1 = w.Joystick(1) # Joystick

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        self.drivetrain.drive(0, 0)

    def autonomousInit(self):
        self.move = self.drivetrain.drive
        self.moving = True
        self.i = 0

        self.length = 130 # How long the robot will run at max speed (100 ~= 2 sec)
        self.max_speed = 5 # Maximum speed (1-10)

    def autonomousPeriodic(self):
        while self.moving:
            for x in range(self.max_speed):
                self.move(-x/10, 0)
                sleep(0.1)
                if x == (self.max_speed - 1):
                    self.moving = False

        if self.i < self.length:
            self.move(-self.max_speed/10, 0)
            self.i += 1
        elif self.i == self.length:
            for x in reversed(range(self.max_speed - 1)):
                self.move(-x/10, 0)
                sleep(0.1)
                if x == 1:
                    self.move(0, 0)
                    self.i += 1
        else:
            self.move(0, 0)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        while self.isOperatorControl() and self.isEnabled():
            self.drivetrain.arcadeDrive(self.js0)

            if self.js1.getRawButton(3) or self.js0.getRawButton(2):
                self.lift_motor.set(-0.8)
            elif self.js1.getRawButton(4) or self.js0.getRawButton(1):
                self.lift_motor.set(0.6)
            else:
                self.lift_motor.set(0)

if __name__ == "__main__":
    w.run(Sparky)
