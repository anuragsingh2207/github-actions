import os

var1 = os.environ.get('ENVIRONMENT')

print("Printing Environment Variable, set by GitHub Actions and provided by user: ",var1)
