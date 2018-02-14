#!usr/bin/env python
from config import get

print("Start")
print("\n<a.b>: ", get("a.b."))
print("\n<a.b.c>: ", get("a.b.c"))
print("\n<a.b.d>: ", get("a.b.d"))
print("\n<a.c>: ", get("a.c"))
print("\n<a.c.d>: ", get("a.c.d."))
print("\n<a.c.f>: ", get("a.c.f"))
print("\n<b.c>: ", get("b.c"))
print("\n<c.f>: ", get("c.f"))
