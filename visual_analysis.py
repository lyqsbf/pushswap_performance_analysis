#!/usr/bin/env python3
import subprocess
import random
import sys
import argparse
import statistics

# Check for matplotlib
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Error: This script requires 'matplotlib'.")
    print("Please install it running: pip install matplotlib")
    sys.exit(1)

def run_push_swap(nums):
    """Runs push_swap and returns the move count. Returns -1 on error/KO."""
    try:
        # Run push_swap
        ps = subprocess.Popen(["./push_swap"] + [str(x) for x in nums], 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE,
                            text=True)
        stdout, stderr = ps.communicate()
        
        # Count moves
        moves = stdout.strip().split('\n')
        if len(moves) == 1 and moves[0] == '':
            count = 0
        else:
            count = len(moves)

        # Verify with checker
        checker = subprocess.Popen(["./checker_linux"] + [str(x) for x in nums],
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    text=True)
        c_out, c_err = checker.communicate(input=stdout)
        
        if c_out.strip() == "OK":
            return count
        else:
            return -1 # KO
    except Exception as e:
        print(f"Exception: {e}")
        return -1

def main():
    parser = argparse.ArgumentParser(description="Detailed visual performance analysis for push_swap")
    parser.add_argument("--min", type=int, default=10, help="Minimum number of elements")
    parser.add_argument("--max", type=int, default=500, help="Maximum number of elements")
    parser.add_argument("--step", type=int, default=50, help="Step size for number of elements")
    parser.add_argument("--samples", type=int, default=10, help="Number of samples (iterations) per step")
    args = parser.parse_args()

    x_values = []      # Amount of numbers
    y_avg = []         # Average moves
    y_min = []         # Min moves
    y_max = []         # Max moves

    print(f"Starting analysis from {args.min} to {args.max} (step {args.step}), {args.samples} samples each.")

    # Generate range of sizes to test
    sizes = list(range(args.min, args.max + 1, args.step))
    if args.max not in sizes:
        sizes.append(args.max)

    for n in sizes:
        print(f"Testing size {n}...", end=" ", flush=True)
        results = []
        for _ in range(args.samples):
            nums = random.sample(range(-20000, 20000), n)
            moves = run_push_swap(nums)
            if moves != -1:
                results.append(moves)
            else:
                print("x", end="", flush=True)

        if results:
            avg_val = statistics.mean(results)
            min_val = min(results)
            max_val = max(results)
            
            x_values.append(n)
            y_avg.append(avg_val)
            y_min.append(min_val)
            y_max.append(max_val)
            print(f"Avg: {avg_val:.1f}")
        else:
            print("Failed all samples for this size.")

    # Plotting
    plt.figure(figsize=(10, 6))
    
    # Plot Average
    plt.plot(x_values, y_avg, label='Average Moves', color='blue', marker='o')
    
    # Plot Min/Max area
    plt.fill_between(x_values, y_min, y_max, color='blue', alpha=0.2, label='Min/Max Range')
    
    # Reference lines (Complexity approximations or hard limits)
    # y = n * log2(n) is often O(n log n), let's just plot points
    
    plt.title(f'Push_swap Performance Analysis (Samples: {args.samples})')
    plt.xlabel('Number of Elements (Stack Size)')
    plt.ylabel('Number of Instructions')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    
    output_file = "performance_graph.png"
    plt.savefig(output_file)
    print(f"\nGraph saved to {output_file}")
    print(f"To view the graph, run: code {output_file} (VS Code) or xdg-open {output_file} (Linux)")
    print("Optimization complete.")

if __name__ == "__main__":
    main()
