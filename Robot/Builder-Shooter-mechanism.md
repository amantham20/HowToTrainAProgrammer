# Building a Shooter Mechanism with WPILib

Welcome to the **Shooter Series**!  In these lessons you will gradually evolve the blank `ExampleSubsystem` you saw earlier into a fully‑featured shooter that can:

1. **Spin the wheel as soon as the robot powers on.**
2. **Change speed on the fly from the driver station.**
3. **Rotate an exact number of turns for repeatable shots.**

The format mirrors the Java chapters you have already read — short explanations, live‐coded examples, and quick challenges to cement each new idea.

---

## Lesson 1 – Anatomy of a WPILib Subsystem

### 1.1  Recap the Template

```java
package frc.robot.subsystems;

import edu.wpi.first.wpilibj2.command.Command;
import edu.wpi.first.wpilibj2.command.SubsystemBase;

public class ExampleSubsystem extends SubsystemBase {
  public ExampleSubsystem() {}

  public Command exampleMethodCommand() {
    return runOnce(() -> { /* one‑time action */ });
  }

  public boolean exampleCondition() {
    return false;
  }

  @Override
  public void periodic() {}
  @Override
  public void simulationPeriodic() {}
}
```

* **Class & package** – organise code just like chapters in a book.
* **Constructor** – place to configure hardware (motors, sensors).
* **Factory methods** – quick ways to build Commands tied to this Subsystem.
* **periodic()** – runs every 20 ms on the roboRIO.

> **Try it ▶** Rename the file and class to `ShooterSubsystem`.  Re‑build the project; make sure Gradle doesn’t complain.

### 1.2  Wire Up a Motor Controller

Add a `CANSparkMax` so the subsystem represents real hardware:

```java
import com.revrobotics.CANSparkMax;
import com.revrobotics.CANSparkMaxLowLevel.MotorType;

public class ShooterSubsystem extends SubsystemBase {
  private final CANSparkMax shooterMotor = new CANSparkMax(5, MotorType.kBrushless);
  public ShooterSubsystem() {
    shooterMotor.restoreFactoryDefaults();
  }
  public void setPercent(double pct) {
    shooterMotor.set(pct);
  }
}
```

*Use the CAN ID from your wiring diagram.*

> **Checkpoint**: Flash code with the robot disabled.  In the RioLog you should see the motor initialize without fault codes.

---

## Lesson 2 – Keep the Shooter Turning on Startup

### 2.1  A Simple Run‑Forever Command

```java
import edu.wpi.first.wpilibj2.command.Command;

public class SpinForever extends Command {
  private final ShooterSubsystem shooter;
  public SpinForever(ShooterSubsystem shooter) {
    this.shooter = shooter;
    addRequirements(shooter);
  }
  @Override public void initialize() { shooter.setPercent(0.6); }
  @Override public boolean isFinished() { return false; }
}
```

* `initialize()` runs once; `execute()` isn’t needed for a constant speed.
* Returning **false** keeps the command scheduled indefinitely.

### 2.2  Schedule at Robot Startup

In **RobotContainer.java**:

```java
public RobotContainer() {
  // … other setup …
  new SpinForever(shooterSubsystem).schedule();
}
```

> **Quick Quiz**: What happens if you call `schedule()` inside the Subsystem constructor instead?  Explain why that is considered a bad practice.

---

## Lesson 3 – Let the Driver Change Speed

### 3.1  Reading a Trigger Axis

```java
import edu.wpi.first.wpilibj2.command.RunCommand;
import edu.wpi.first.wpilibj.XboxController;

public class RobotContainer {
  private final XboxController driver = new XboxController(0);
  public RobotContainer() {
    shooterSubsystem.setDefaultCommand(
      new RunCommand(() -> shooterSubsystem.setPercent(driver.getRightTriggerAxis()), shooterSubsystem));
  }
}
```

* `RunCommand` is a one‑liner replacement for making a whole new class.
* **Default commands** run whenever nothing else has the subsystem.

> **Mini‑Mission**: Cap the trigger value so the motor never exceeds 70 %.

---

## Lesson 4 – Spin Exactly *N* Rotations

### 4.1  Measuring the Motor Position

```java
import com.revrobotics.RelativeEncoder;

public class ShooterSubsystem extends SubsystemBase {
  private final RelativeEncoder encoder = shooterMotor.getEncoder();
  public double getRotations() { return encoder.getPosition(); }
  public void resetEncoder()   { encoder.setPosition(0); }
}
```

The NEO’s built‑in encoder returns revolutions out‑of‑the‑box—perfect for our goal.

### 4.2  A "Spin N" Command with PID

```java
import edu.wpi.first.math.controller.PIDController;
import edu.wpi.first.wpilibj2.command.ProfiledPIDCommand;
import edu.wpi.first.math.trajectory.TrapezoidProfile;

public class SpinNRotations extends ProfiledPIDCommand {
  private static final double kP = 0.6, kI = 0, kD = 0.05;
  private static final TrapezoidProfile.Constraints kConstraints =
      new TrapezoidProfile.Constraints(3000, 2000); // rpm & accel limits

  public SpinNRotations(ShooterSubsystem shooter, double rotations) {
    super(new PIDController(kP, kI, kD),
          shooter::getRotations,               // measurement
          rotations,                           // goal (setpoint)
          output -> shooter.setPercent(output),// useOutput
          kConstraints,
          shooter);
    shooter.resetEncoder();
  }
}
```

* `ProfiledPIDCommand` handles motion profiling **and** PID closed‑loop.
* `resetEncoder()` zeroes the reference frame each use.

> **Challenge**: Make a SmartDashboard entry where the coach types a distance (rotations) and presses a button to execute `SpinNRotations`.

---

## Next Steps

* Add **flywheel RPM feedback** instead of open‑loop percent output.
* Layer **states** (IDLE, SPIN‑UP, HOLD) using the WPILib **StateMachine** helper.
* Integrate with your **vision pipeline** for auto‑aiming.

Happy coding & good luck at your next regional!
