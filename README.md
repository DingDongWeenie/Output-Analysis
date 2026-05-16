# Output Analysis - Simulation Methods

## The Three Methods

### 1. Welch Method
Identifies the warm-up period of a simulation by calculating a moving average and detecting when the data stabilizes. Ignores the initial unstable phase to focus on steady-state behavior.

### 2. Replication-Deletion Method
Runs multiple replications of the simulation, removes warm-up observations from each run, and then averages the results. Provides a more reliable estimate by reducing variance from a single run.

### 3. Batch Means Method
Divides collected observations into equal-sized batches and calculates the mean for each batch. Detects if the system remains stable throughout the entire observation period.

---

## Running the Code

```bash
python outlysis.py
```

The script generates a visualization showing all three methods side-by-side with reference lines indicating stabilized or mean values.
