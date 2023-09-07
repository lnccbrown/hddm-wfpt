import platform
from setuptools import setup, Extension

import numpy as np

try:
    from Cython.Build import cythonize

    if platform.system() == "Darwin":
        ext1 = Extension(
            "wfpt",
            ["./hddm_wfpt/wfpt.pyx"],
            language="c++",
            include_dirs=[np.get_include()],
            extra_compile_args=["-stdlib=libc++"],
            extra_link_args=["-stdlib=libc++", "-mmacosx-version-min=10.9"],
        )
    else:
        ext1 = Extension("wfpt", ["./hddm_wfpt/wfpt.pyx"],
                         include_dirs=[np.get_include()],
                         language="c++")

    ext_modules = cythonize(
        [
            ext1,
            Extension(
                "cdfdif_wrapper",
                ["./hddm_wfpt/cdfdif_wrapper.pyx", "./hddm_wfpt/cdfdif.c"],
                include_dirs=[np.get_include()],
            ),
        ],
        compiler_directives={"language_level": "3", "linetrace": True},
    )

except ImportError:

    ext_modules = [
        Extension("wfpt", ["./hddm_wfpt/wfpt.cpp"], language="c++",
                  include_dirs=[np.get_include()]),
        Extension("cdfdif_wrapper", ["./hddm_wfpt/cdfdif_wrapper.c", "./hddm_wfpt/cdfdif.c"],
                  include_dirs=[np.get_include()]),
    ]

setup(
    packages=["hddm_wfpt"],
    include_dirs=[np.get_include()],
    ext_modules=ext_modules,
)