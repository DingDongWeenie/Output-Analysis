# Output Analysis - Simulation Methods

## What's This About?

When you run a computer simulation, you get a bunch of data. But here's the problem: **the beginning is always messy**. 

Imagine opening a restaurant. The first hour is chaos—staff is still figuring things out, customers are confused, everything takes longer. Then things settle down and work normally. If you average everything together (messy startup + normal operations), you get a wrong answer.

These three methods solve that problem. They clean up your simulation data and give you the *real* answer.

---

## The Three Methods Explained

### 1️⃣ **Welch Method** (Find the Warm-Up Period)

**The idea:** Just like a restaurant needs time to warm up, simulations do too.

**How it works:**
- Calculate a moving average (smoothing out the bumps)
- Watch when the line flattens out (that's when it stabilizes)
- That flat part is your "good data"
- Ignore everything before that

**In real terms:** It's like watching water boil—first it's quiet, then bubbles start, then it's full boil. You only want to measure after it reaches full boil.

**When to use it:** Quick check to see if your data settles down to a stable level.

---

### 2️⃣ **Replication-Deletion Method** (Run It Multiple Times)

**The idea:** Running something once can be misleading. Run it multiple times and average.

**How it works:**
1. Run the simulation 5 times
2. For each run, throw away the first 10 observations (the warm-up)
3. Calculate the average for each run
4. Average all 5 results together

**In real terms:** It's like flipping a coin once (you get heads or tails—no middle ground). But flip it 100 times and count heads—now you know the real probability is 50%.

**When to use it:** When you want a solid, reliable answer. Multiple runs smooth out random weirdness.

---

### 3️⃣ **Batch Means Method** (Check Consistency)

**The idea:** Divide your data into chunks and see if they're all similar.

**How it works:**
1. Collect 100 observations
2. Split into 10 batches of 10
3. Calculate the average for each batch
4. Plot them—are they all close? Or bouncing around?

**In real terms:** If you test every 10 customers and get: 50 sec, 50 sec, 51 sec, 49 sec, 50 sec... ✓ Consistent!
But if you get: 50 sec, 80 sec, 40 sec, 100 sec... ❌ Something's wrong!

**When to use it:** To spot problems. If batch means jump around, your system isn't stable.

---

## The Graph

All three methods are visualized together:
- **Left graph (Welch):** Shows the warm-up period smoothing out
- **Middle graph (Replication-Deletion):** Shows consistency across 5 runs
- **Right graph (Batch Means):** Shows if data stays stable throughout

The red dashed lines show the "settled" values—this is the number you can trust.

---

## Quick Tips

✅ **Use all three** to be thorough  
✅ **Look at the red lines** in the graphs—that's your answer  
✅ **If batch means bounce around**, something's wrong with your simulation  
✅ **Throw away the warm-up period**—it's not real data  

---

## Running the Code

```bash
python outlysis.py
```

You'll see:
- Console output with the numbers
- A graph with all 3 methods side-by-side
- Red reference lines showing the stable/mean values

---

## The Bottom Line

**Problem:** Simulations start messy, so you can't trust the average of all data.

**Solution:** These three methods clean up the mess and give you the real answer.

**Result:** Reliable data you can actually use for decisions.

That's it. Go simulate! 🚀
