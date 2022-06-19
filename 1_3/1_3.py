import sys
import os

def main(argc: int, argv: list) -> None:
    """
    Driver function for ftoc conversion
    @param1: argc: int: argument count
    @param2: argv: list: argument vector
    @return: None
    """
    if argc < 4:
        print("Usage Error: Correct Usage: %s <lower> <upper> <step>" %argv[0])
        sys.exit(-1)

    lower = int(argv[1])
    upper = int(argv[2])
    step  = int(argv[3])
    
    fahr = lower
    celsius = 0

    print("Celsius\t\tFahrenheit")
    print("=======\t\t==========")
    while fahr <= upper:
        celsius = ((5.0/9.0)*(fahr - 32.0))
        print("%3.0f\t\t%6.1f" %(fahr, celsius))
        fahr = fahr + step



main(len(sys.argv), sys.argv)
