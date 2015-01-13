#!/usr/bin/env python3

import wpilib

class Robot(wpilib.IterativeRobot):

    def robotInit(self):

        # Motors to PWM channels
        fl_motor = wpilib.Talon(0) # Channel 0
        bl_motor = wpilib.Talon(1)
        fr_motor = wpilib.Talon(2)
        br_motor = wpilib.Talon(3)

        # Drivetrain control
        self.robot_drive = wpilib.RobotDrive(fl_motor, bl_motor, fr_motor, br_motor)

        # Joystick
        self.joystick = wpilib.Joystick(1)

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        self.robot_drive.drive(0, 0)

    def autonomousInit(self):
        self.counter = 0

    def autonomousPeriodic(self):
        if self.counter < 100:
            self.robot_drive.drive(-0.5, 0)
            self.counter +=1
        else:
            self.robot_drive.drive(0, 0)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.robot_drive.arcadeDrive(self.joystick)

if __name__ == "__main__":
    wpilib.run(Robot)
