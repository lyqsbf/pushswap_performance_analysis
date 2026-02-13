#!/usr/bin/env python3
import subprocess
import random
import sys

def run_test(n):
    nums = random.sample(range(10000), n)
    arg = " ".join(map(str, nums))
    
    # Run push_swap
    ps = subprocess.Popen(["./push_swap"] + [str(x) for x in nums], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = ps.communicate()
    
    ops = stdout.decode().strip()
    
    # Run checker
    checker = subprocess.Popen(["./checker_linux"] + [str(x) for x in nums], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    c_out, c_err = checker.communicate(input=stdout)
    
    res = c_out.decode().strip()
    movm = len(ops.split('\n')) if ops else 0
    if res != "OK":
        print(f"FAIL with {n} items: {res}")
        print(f"Args: {arg}")
        return False
    print(f"OK: {n} numbers ordered in {movm} steps.")
    return True

for i in range(20):
    if not run_test(100):
        sys.exit(1)
    if not run_test(500):
        sys.exit(1)
    if not run_test(random.randint(6, 100)):
        sys.exit(1)

print("All tests passed")
