import subprocess

# shell, capture_output og text eru til að fá svarið í terminalinu, eins og kæmi í cmd
result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
print(result.stdout)

# til að keyra python scripts
pyth = subprocess.run(["python", "slóð/að/pythonfæl.py"], capture_output=True, text=True)
# print(result.stdout)


