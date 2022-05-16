#!/usr/bin/env python3

try:
    1 / 0
except ZeroDivisionError as e:
    print(f"[Erro] Deu erro {str(e)}", file=open("log2.txt", "a"))
    # stdout
