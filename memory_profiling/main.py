#!/usr/bin/env python
"""Python Memory Profiling"""
from memory_profiler import profile

mem_logs = open('mem_profile.log', 'a')

@profile(stream=mem_logs)
def process_strs(reps=10**6):
    """generate super long string"""
    str1 = 'python' * reps
    str2 = 'programmer' * reps
    str3 = str1 + str2
    del str2
    return str3


process_strs(reps=10**7)

