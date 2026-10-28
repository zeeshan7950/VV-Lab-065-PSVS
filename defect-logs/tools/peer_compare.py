import sys
mine,peer,common=map(int,sys.argv[1:4])
union=mine+peer-common
print(f"Union of distinct defects: {union}")
print(f"My detection rate  : {mine}/{union} = {mine/union:.1%}")
print(f"Peer detection rate: {peer}/{union} = {peer/union:.1%}")
print(f"Missed by me: {union-mine}")
