padovan = lambda n: 1 if n <= 2 else padovan(n-2) + padovan(n-3)