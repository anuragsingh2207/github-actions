import os

var1 = os.environ.get('ENVIRONMENT')

print("Hello, World. Printing Environment Variable, set by GitHub Actions and provided by user: ",var1)
