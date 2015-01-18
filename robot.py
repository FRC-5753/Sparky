#!/usr/bin/env python3

import wpilib

class Robot(wpilib.IterativeRobot):

    def robotInit(self):

        # Motors to PWM channels
        l_motor = wpilib.Talon(0) # Channel 0
        r_motor = wpilib.Talon(1) # Channel 1

        # Drivetrain control
        self.robot_drive = wpilib.RobotDrive(r_motor, l_motor)

        # Joystick
        self.joystick = wpilib.Joystick(0)

    def disabledInit(self):
        print("-- DISABLED --")

    def disabledPeriodic(self):
        self.robot_drive.drive(0, 0) # Stop the robot

    def autonomousInit(self):
        print("-- AUTONOMOUS --")

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        print("-- TELEOP --")

    def teleopPeriodic(self):
        self.robot_drive.arcadeDrive(self.joystick)

if __name__ == "__main__":
    wpilib.run(Robot)
