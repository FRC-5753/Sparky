#!/usr/bin/env python3

import wpilib as w

class Sparky(w.IterativeRobot):

    def robotInit(self):

        # Motors to PWM channels
        l_motor = w.Talon(0)
        r_motor = w.Talon(1)

        # Drivetrain control
        self.drivetrain = w.RobotDrive(r_motor, l_motor)

        # Joystick
        self.joystick = w.Joystick(0)

    def move(self, speed, curve):
        self.drivetrain.drive(speed, curve)

    def stop(self):
        self.drivetrain.drive(0, 0)

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        self.stop() # Stop the robot

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass

if __name__ == "__main__":
    w.run(Sparky)
