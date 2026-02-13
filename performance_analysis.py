#!/usr/bin/env python3
import subprocess
import random
import sys
import math
import argparse

def run_analysis(n_elements, iterations):
    move_counts = []
    ko_count = 0
    error_count = 0

    print(f"--- Analyzing Push_Swap with {n_elements} elements ({iterations} iterations) ---")
    
    # Progress: one dot per successful run
    print("Progress: ", end="", flush=True)

    for i in range(iterations):
        nums = random.sample(range(-20000, 20000), n_elements)
        arg = " ".join(map(str, nums))
        
        try:
            # Run push_swap
            ps = subprocess.Popen(["./push_swap"] + [str(x) for x in nums], 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE,
                                text=True)
            stdout, stderr = ps.communicate()
            
            # Count moves (lines)
            moves = stdout.strip().split('\n')
            # Handle empty output case
            if len(moves) == 1 and moves[0] == '':
                count = 0
            else:
                count = len(moves)

            # verify with checker
            # pass args
            check_proc = subprocess.Popen(["./checker_linux"] + [str(x) for x in nums],
                                        stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        text=True)
            
            check_out, check_err = check_proc.communicate(input=stdout)
            
            result = check_out.strip()
            if result == "OK":
                move_counts.append(count)
                if (i + 1) % 10 == 0:
                   print(".", end="", flush=True)
            elif result == "KO":
                ko_count += 1
                print("X", end="", flush=True)
                # optionally save failing args
                with open("ko_cases.txt", "a") as f:
                    f.write(f"KO with {count} moves: {arg}\n")
            else:
                # Error
                error_count += 1
                print("?", end="", flush=True)

        except Exception as e:
            print(f"Error: {e}")
            error_count += 1

    print("\n")

    if not move_counts:
        print("No successful runs.")
        return

    n = len(move_counts)
    mean = sum(move_counts) / n
    variance = sum((x - mean) ** 2 for x in move_counts) / n
    std_dev = math.sqrt(variance)
    
    limit = 0
    limit_msg = ""
    if n_elements == 100:
        limit = 700
    elif n_elements == 500:
        limit = 5500
        
    if limit > 0:
        over_limit_count = sum(1 for x in move_counts if x > limit)
        percent_over = (over_limit_count / n) * 100
        limit_msg = f"\nRuns > {limit}:    {over_limit_count} ({percent_over:.2f}%)"

    msg = f"""
Results for {n_elements} numbers ({iterations} iterations):
----------------------------------------
Successful Runs (OK): {n}
Failed Runs (KO):     {ko_count}
Errors:               {error_count}
----------------------------------------
Min Moves:     {min(move_counts)}
Max Moves:     {max(move_counts)}{limit_msg}
Mean (Avg):    {mean:.2f}
Variance:      {variance:.2f}
Std Dev:       {std_dev:.2f}
----------------------------------------
"""
    print(msg)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        run_analysis(int(sys.argv[1]), int(sys.argv[2]))
    else:
        run_analysis(100, 100)
        run_analysis(500, 100)
