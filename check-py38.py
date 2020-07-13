from conda.api import Solver
from conda.exceptions import UnsatisfiableError


deps = [
    'pytest',
    'pytest-cov',
    'nbval',
    'codecov',
    'coverage < 5.0',
    'numpy',
    'networkx',
    'ambertools',
    'packaging',
    'openmmforcefields >=0.7.2',
    'openmmtools',
    'openforcefields',
    'smirnoff99Frosst',
    'pyyaml',
    'toml',
    'bson',
    'msgpack-python',
    'xmltodict',
    'qcelemental',
    'qcportal',
    'qcengine',
]

failed = []
succeeded = []

for dep in deps:
    print(f"Trying dep {dep} ...")
    solver = Solver(
        prefix='/Users/mwt/software/miniconda3/bin/python',
        channels=['conda-forge', 'omnia', 'defaults'],
        specs_to_add=[dep, 'python=3.8'])
    try:
        solver.solve_final_state()
        succeeded.append(dep)
    except UnsatisfiableError:
        failed.append(dep)

print("The following packages are (probably) shipped with Python 3.8:")
print(succeeded)
print("The following packages are (probably) NOT shipped with Python 3.8:")
print(failed)
