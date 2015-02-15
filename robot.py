#!/usr/bin/env python3

import wpilib as w
from time import sleep

class Sparky(w.IterativeRobot):

    def robotInit(self):

        # Motors to PWM channels
        l_motor = w.Talon(0)
        r_motor = w.Talon(1)
        self.lift_motor = w.PWM(2)

        # Drivetrain control
        self.drivetrain = w.RobotDrive(l_motor, r_motor)

        # Joystick
        self.joystick = w.Joystick(0)

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        self.drivetrain.drive(0, 0)

    def autonomousInit(self):
        self.move = self.drivetrain.drive
        self.moving = True
        self.i = 0
        self.cap = 100
        self.max_speed = 10

    def autonomousPeriodic(self):
        while self.moving:
            for x in range(self.max_speed):
                print(x)
                self.move(-x/10, -0.08)
                sleep(0.1)
                if x == (self.max_speed - 1):
                    self.moving = False

        if self.i < self.cap:
            self.move(-self.max_speed/10, -0.08)
            self.i += 1
        elif self.i == self.cap:
            for x in reversed(range(self.max_speed - 1)):
                print(x)
                self.move(-x/10, 0)
                sleep(0.1)
                if x == 1:
                    self.move(0, 0)
                    self.i += 1
        else:
            self.move(0, 0)

    def teleopInit(self):
        w.kDefaultSensitivity = 0.25

    def teleopPeriodic(self):
        while self.isOperatorControl() and self.isEnabled():
            self.drivetrain.arcadeDrive(self.joystick)

            if self.joystick.getRawButton(1):
                self.lift_motor.setBounds(10, 10, 5, 1, 1)
                self.lift_motor.setSpeed(1)
            elif self.joystick.getRawButton(2):
                self.lift_motor.setBounds(10, 10, 5, 1, 1)
                self.lift_motor.setSpeed(-1)
            else:
                self.lift_motor.setBounds(0, 0, 0, 0, 0)

if __name__ == "__main__":
    w.run(Sparky)
