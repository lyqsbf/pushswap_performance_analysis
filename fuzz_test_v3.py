#!/usr/bin/env python3
import subprocess
import random
import sys

def run_test_nums(nums):
    arg = " ".join(map(str, nums))
    ps = subprocess.Popen(["./push_swap"] + [str(x) for x in nums], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = ps.communicate()
    
    checker = subprocess.Popen(["./checker_linux"] + [str(x) for x in nums], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    c_out, c_err = checker.communicate(input=stdout)
    
    res = c_out.decode().strip()
    if res != "OK":
        print(f"FAIL: {res}")
        print(f"Args: {arg}")
        return False
    return True

print("Running reverse sorted tests...")
for n in range(6, 101):
    nums = list(range(n))
    nums.reverse()
    if not run_test_nums(nums):
        sys.exit(1)

print("Running almost sorted tests...")
for n in range(6, 101):
    nums = list(range(n))
    # Swap two elements
    i, j = random.sample(range(n), 2)
    nums[i], nums[j] = nums[j], nums[i]
    if not run_test_nums(nums):
        sys.exit(1)

print("Passed")
