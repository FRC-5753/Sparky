#!/usr/bin/env python3

import wpilib as w
from time import sleep

class Sparky(w.IterativeRobot):

    def robotInit(self):

        # Motors to PWM channels
        l_motor = w.Talon(0)
        r_motor = w.Talon(1)
        self.lift_motor = w.VictorSP(2)

        # Limit switches
        self.top_ls = w.DigitalInput(0)
        self.bot_ls = w.DigitalInput(1)

        # Drivetrain control
        self.drivetrain = w.RobotDrive(l_motor, r_motor)

        # Joystick
        self.js0 = w.Joystick(0) # Xbox controller
        self.js1 = w.Joystick(1) # Joystick

        # Disable motor safety
        self.drivetrain.setSafetyEnabled(False)

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        self.drivetrain.drive(0, 0)

    def autonomousInit(self):
        self.move = self.drivetrain.drive
        self.moving = True
        self.i = 0

        self.length = 100 # How long the robot will run at max speed (100 ~= 2 sec)
        self.max_speed = 5 # Maximum speed (1-10)

    def autonomousPeriodic(self):
        while self.moving:
            for x in range(self.max_speed):
                self.move(-x/10, -0.08)
                sleep(0.1)
                if x == (self.max_speed - 1):
                    self.moving = False

        if self.i < self.length:
            self.move(-self.max_speed/10, -0.08)
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
        self.up = True
        self.down = True

    def teleopPeriodic(self):
        self.drivetrain.arcadeDrive(self.js0, squaredInputs=True)

        if self.top_ls.get() == 1:
            self.up = False
        elif self.bot_ls.get() == 1:
            self.down = False
        else:
            self.up = True
            self.down = True

        if self.js0.getRawButton(1) and self.up: # Button B
            self.lift_motor.set(0.3)
        elif self.js0.getRawButton(2) and self.down: # Button A
            self.lift_motor.set(-0.3)
        else:
            self.lift_motor.set(0)

if __name__ == "__main__":
    w.run(Sparky)
