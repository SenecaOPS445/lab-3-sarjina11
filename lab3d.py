#!/usr/bin/env python3
'''Lab 3 Inv 2 Running Linux commands with subprocess'''

import subprocess


def free_space():
    p = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['grep', '/$'], stdin=p.stdout, stdout=subprocess.PIPE)
    p3 = subprocess.Popen(['awk', '{print $4}'], stdin=p2.stdout, stdout=subprocess.PIPE)
    
    output = p3.communicate()[0]
    output_str = output.decode('utf-8').strip()
    
    return output_str

if __name__ == '__main__':
    print(free_space())
