# Building a Shooter Mechanism with WPILib

*A step‑by‑step curriculum for Java teams who want a reliable flywheel shooter*

---

### 📚  Roadmap

1. **Lesson 1 – Anatomy of a WPILib Subsystem**
   *Understand how the template fits into the command‑based ecosystem.*
2. **Lesson 2 – Keep the Shooter Turning on Startup**
   *Create a command that spins forever and schedule it safely.*
3. **Lesson 3 – Driver‑Controlled Speed**
   *Map your controller’s trigger to motor power and add soft caps.*
4. **Lesson 4 – Spin Exactly *N* Rotations**
   *Close the loop with encoders and Profiled PID.*

> Throughout the course you’ll see **⚙️ Lab Steps** (things to do in code), **🚀 Field Tests** (robot‑on‑carpet checks), and **🧠 Extra Credit** (stretch challenges).

---

## Lesson 1 – Anatomy of a WPILib Subsystem

### 1.1  Why Subsystems?

A **Subsystem** is a Java class that represents a slice of hardware on your robot—motors, sensors, pneumatics—plus the logic that keeps those parts healthy.  Commands then *ask* subsystems to do work.

```mermaid
flowchart LR
  DriverStation -->|buttons| Command
  Command -->|requires| Subsystem
  Subsystem -->|controls| Motor
```

### 1.2  Dissecting the Template

```java
public class ExampleSubsystem extends SubsystemBase {
  public ExampleSubsystem() { /* configure motors here */ }
  public Command exampleMethodCommand() { ... }

  @Override public void periodic() { /* 20 ms loop */ }
}
```

| Piece                  | Purpose                                                                     |
| ---------------------- | --------------------------------------------------------------------------- |
| `constructor`          | Hardware wiring & default settings                                          |
| `periodic()`           | Sensor polling and telemetry                                                |
| `simulationPeriodic()` | Called only in Glass / Sim                                                  |
| **Factory method**     | Returns a ready‑to‑go Command so other classes don’t need to know internals |

⚙️ **Lab Step**  – Rename everything to `ShooterSubsystem`, change the package to `frc.robot.subsystems.shooter`, and run **`./gradlew build`**. Fix any import warnings.

🧠 **Extra Credit** – Sketch a second class diagram showing how multiple subsystems (Drivetrain, Shooter, Intake) talk to a single Xbox controller.

---

## Lesson 2 – Keep the Shooter Turning on Startup

### 2.1  Choose Your Motor Controller

We’ll assume a **REV NEO + Spark MAX** combo over CAN (ID 5). If you use Talon FX or Falcon, translate the API names.

```java
private final CANSparkMax wheel = new CANSparkMax(5, MotorType.kBrushless);
```

*Factory Defaults* – Always call `restoreFactoryDefaults()` once so hidden settings don’t bite you later.

### 2.2  Write a `SpinForever` Command

```java
public class SpinForever extends Command {
  private final ShooterSubsystem shooter;
  public SpinForever(ShooterSubsystem shooter) {
    this.shooter = shooter;
    addRequirements(shooter);
  }
  @Override public void initialize() { shooter.setPercent(0.6); }
  @Override public boolean isFinished() { return false; }
  @Override public void end(boolean interrupted) { shooter.setPercent(0); }
}
```

Key takeaway: **never** leave the motor running in `end()` if the command is interrupted—field staff will thank you.

### 2.3  Schedule at Robot Boot

```java
public RobotContainer() {
  shooter = new ShooterSubsystem();
  new SpinForever(shooter).schedule();
}
```

🚀 **Field Test** – Deploy code, leave the robot disabled, flip the breaker. The wheel should spin instantly at 60 %. Cycle enable/disable. Does it coast to zero when disabled? Good.

🧠 **Extra Credit** – Create a Shuffleboard toggle that cancels and re‑schedules the command without re‑deploying.

---

## Lesson 3 – Driver‑Controlled Speed

### 3.1  Map a Trigger Axis

```java
shooter.setDefaultCommand(
  new RunCommand(
    () -> shooter.setPercent(0.7 * driver.getRightTriggerAxis()),
    shooter));
```

* `getRightTriggerAxis()` returns 0 → 1.  We scale to 70 % so brownouts don’t trip breakers.

### 3.2  Add RPM Telemetry

```java
SmartDashboard.putNumber("Shooter RPM", shooter.getRPM());
```

Expose this in `periodic()` so drive coaches see spin‑up time on the DS.

### 3.3  Safe Current Limits

REV lets you cap current in firmware:

```java
wheel.setSmartCurrentLimit(40);   // amps
wheel.setClosedLoopRampRate(0.5); // seconds 0→full
```

⚙️ **Lab Step** – Try ramp rates of 0.2 s vs 2 s and watch voltage spikes in the power distribution log.

🚀 **Field Test** – On carpet, rev the shooter while driving. Verify drivetrain voltage doesn’t sag below 7 V.

🧠 **Extra Credit** – Map the A‑button to toggle between two preset speeds (e.g., lay‑up vs far‑shot) using `InstantCommand`.

---

## Lesson 4 – Spin Exactly *N* Rotations

### 4.1  Read the Built‑In Encoder

```java
private final RelativeEncoder enc = wheel.getEncoder();
public double getRotations() { return enc.getPosition(); }
public void resetEncoder()  { enc.setPosition(0); }
```

REV NEO returns **rotations**, so 1.5 means 540°.

### 4.2  Profiled PID Command

```java
public class SpinNRotations extends ProfiledPIDCommand {
  private static final TrapezoidProfile.Constraints k =
      new TrapezoidProfile.Constraints(3000, 2000); // rpm & accel
  public SpinNRotations(ShooterSubsystem s, double rot) {
    super(new PIDController(0.6, 0, 0.05),
          s::getRotations, rot,
          out -> s.setPercent(out), k, s);
    s.resetEncoder();
  }
}
```

1. **Constraints** create an S‑curve so you don’t slam the gearbox.
2. `out` from the internal controller is already `-1 → 1` (percent output).

### 4.3  Button Binding

```java
new JoystickButton(driver, XboxController.Button.kX.value)
    .onTrue(new SpinNRotations(shooter, 3)); // three rotations
```

🚀 **Field Test** – Mark the flywheel with tape, video at 240 fps, count frames; should be within ±5°.

🧠 **Extra Credit** – Tune `kP` live with Shuffleboard sliders.

---

## Where to Go Next

* **Closed‑loop RPM** – Replace percent output with PID on velocity for tighter accuracy.
* **State Machine** – WPILib’s new `Subsystem` states can automate IDLE → SPIN‑UP → HOLD.
* **Vision Integration** – Use limelight distance to choose RPM setpoints dynamically.

Happy coding, and may your discs fly straight!

---

*Template style inspired by your Java basics notes* citeturn0file0
