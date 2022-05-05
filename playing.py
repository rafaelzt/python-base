#!/usr/bin/env python

fruit = "🍉"
print(fruit)

# Serialização
print(fruit.encode())
print(fruit.encode().decode())
print(list(bytes(fruit, "utf-8")))


