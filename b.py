item = (
    "string", 
    {"entities": [
        (1, 2, "pos"),
        (1, 2, "pos")
        ]
    }
)

a = [
    ("Pedro nasceu em Lisboa.", {"entities": [(0, 5, "PER"), (16, 22, "LOC")]}),
    ("Maria trabalha na Google em Belo Horizonte.", {"entities": [(0, 5, "PER"), (18, 24, "ORG"), (28, 42, "LOC")]})
    ]
for b, c in a:
    print(b)
    print(c)

g = ["a", 'garota']
print(" ".join(g))