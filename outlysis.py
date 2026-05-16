# Output Analysis Methods in Simulation
# Coffee Shop, Restaurant, and 100 Observation Examples

import numpy as np
import matplotlib.pyplot as plt

# =====================================================
# SAMPLE SIMULATION DATA
# =====================================================
np.random.seed(1)

# =====================================================
# 1. WELCH METHOD
# Coffee Shop Waiting Time Example
# =====================================================
print("\n===== WELCH METHOD =====")
print("Coffee Shop Waiting Time Simulation\n")

# Waiting times of customers in a coffee shop
waiting_times = np.array([
    70, 65, 60, 58, 55, 52, 51, 50, 50
])

# Moving average to find warm-up period
window_size = 3
moving_avg = np.convolve(
    waiting_times,
    np.ones(window_size)/window_size,
    mode='valid'
)

print("Original Waiting Times:")
print(waiting_times)

print("\nMoving Averages:")
print(np.round(moving_avg, 2))

print("\nThe graph helps determine where the simulation stabilizes.")
print("That stable point is considered the warm-up period.")
print(f"\n→ Stabilizes at: {moving_avg[-1]:.2f} seconds")

# =====================================================
# 2. REPLICATION-DELETION METHOD
# Restaurant Simulation Example
# =====================================================
print("\n===== REPLICATION-DELETION METHOD =====")
print("Restaurant Waiting Time Simulation\n")

replications = 5
warmup = 10
means = []

for i in range(replications):

    # Generate restaurant waiting time data
    sim_data = np.random.normal(
        loc=50,
        scale=5,
        size=100
    )

    # Delete warm-up observations
    steady_state = sim_data[warmup:]

    # Compute mean
    mean_value = np.mean(steady_state)
    means.append(mean_value)

    print(f"Replication {i+1} Mean: {mean_value:.2f}")

overall_mean = np.mean(means)

print(f"\nOverall Mean after deletion: {overall_mean:.2f} seconds")
print(f"→ Discard first {warmup} observations to reach steady state")

# =====================================================
# 3. BATCH MEAN METHOD
# 100 Observation Example
# =====================================================
print("\n===== BATCH MEAN METHOD =====")
print("100 Observation Simulation Example\n")

# Generate 100 observations
observations = np.random.normal(
    loc=50,
    scale=5,
    size=100
)

batch_size = 10
num_batches = len(observations) // batch_size

batch_means = []

for i in range(num_batches):

    start = i * batch_size
    end = start + batch_size

    batch = observations[start:end]
    batch_mean = np.mean(batch)

    batch_means.append(batch_mean)

    print(f"Batch {i+1} Mean: {batch_mean:.2f}")

overall_batch_mean = np.mean(batch_means)

print(f"\nOverall Batch Mean: {overall_batch_mean:.2f} seconds")
print(f"→ Data divided into {num_batches} batches of {batch_size} observations each")

# =====================================================
# VISUALIZATION - ALL METHODS IN ONE WINDOW
# =====================================================
fig, axes = plt.subplots(3, 1, figsize=(10, 8))

# Welch Method Plot
axes[0].plot(moving_avg, marker='o', linewidth=2, markersize=6, color='#2E86AB')
axes[0].set_title("Welch Method - Coffee Shop Waiting Time\n(Identifying Warm-up Period)", fontsize=11, fontweight='bold')
axes[0].set_xlabel("Customer Number")
axes[0].set_ylabel("Average Waiting Time (seconds)")
axes[0].grid(True, alpha=0.3)
axes[0].axhline(y=moving_avg[-1], color='red', linestyle='--', alpha=0.5, label=f'Stabilized at {moving_avg[-1]:.1f}s')
axes[0].legend()

# Replication-Deletion Method Plot
axes[1].plot(means, marker='s', linewidth=2, markersize=8, color='#A23B72')
axes[1].set_title(f"Replication-Deletion Method - Restaurant Simulation\n(5 Replications, Warmup: {warmup} observations)", fontsize=11, fontweight='bold')
axes[1].set_xlabel("Replication Number")
axes[1].set_ylabel("Mean Waiting Time (seconds)")
axes[1].grid(True, alpha=0.3)
axes[1].axhline(y=overall_mean, color='red', linestyle='--', alpha=0.5, label=f'Overall Mean: {overall_mean:.1f}s')
axes[1].legend()

# Batch Mean Method Plot
axes[2].plot(batch_means, marker='^', linewidth=2, markersize=7, color='#F18F01')
axes[2].set_title(f"Batch Mean Method - 100 Observations\n({num_batches} Batches of {batch_size} observations)", fontsize=11, fontweight='bold')
axes[2].set_xlabel("Batch Number")
axes[2].set_ylabel("Batch Mean Waiting Time (seconds)")
axes[2].grid(True, alpha=0.3)
axes[2].axhline(y=overall_batch_mean, color='red', linestyle='--', alpha=0.5, label=f'Overall Mean: {overall_batch_mean:.1f}s')
axes[2].legend()

plt.tight_layout()
plt.show()