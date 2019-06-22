import logging

import pascua as psc

logging.basicConfig(level=logging.DEBUG)


def main():
    context = {
        'size': 100,
    }

    source_code = [
        'import numpy as np',
        'random_numbers = np.random.uniform(size=size)',
        'numbers = list(map(lambda x: f"number {x}", range(size)))',
    ]

    env = psc.PythonEnvironment(
        version='3.7.3',
        pip_dependencies=[
            'numpy>=1.14.0',
        ]
    )

    result = env.exec(source_code, context)
    print(result)


if __name__ == '__main__':
    main()
