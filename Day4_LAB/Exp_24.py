#Write a program to find the CPU performance of a processor using any high level 
#language
print("Enter the instruction count of a program: ")
inst_count=int(input())
print("Enter the value of clock per instruction(CPI):")
CPI=float(input())
print("Enter the clock rate:")
clock_rate=float(input())
CPU_time=inst_count*CPI/clock_rate
print("CPU Time:")
print(CPU_time)