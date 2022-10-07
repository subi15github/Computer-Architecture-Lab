#Write a program to find the Hit ratio for the given number of Hits and Misses in Cache 
#memory using any high level language.
print("Enter the number of Cache Hits:")
hit=int(input())
miss=int(input("Enter the number of Cache Miss:"))
hit_ratio=hit/(hit+miss)
print("Hit-Ratio=",round(hit_ratio,2))