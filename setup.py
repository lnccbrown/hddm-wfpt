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

# setup(
#     name="hddm-wfpt",
#     version="0.1.1",
#     author="Thomas V. Wiecki, Imri Sofer, Michael J. Frank, Mads Lund Pedersen, Alexander Fengler, Lakshmi Govindarajan, Krishn Bera",
#     author_email="thomas.wiecki@gmail.com",
#     url="http://github.com/hddm-devs/hddm",
#     packages=["hddm_wfpt"],  # 'hddm.cnn', 'hddm.cnn_models', 'hddm.keras_models',
#     description="HDDM is a python module that implements Hierarchical Bayesian estimation of Drift Diffusion Models.",
#     setup_requires=["numpy >= 1.23.4", "cython >= 0.29.32"],
#     install_requires=["numpy >=1.23.4", "scipy >= 1.9.1", "cython >= 0.29.32"],
#     include_dirs=[np.get_include()],
#     classifiers=[
#         "Development Status :: 5 - Production/Stable",
#         "Environment :: Console",
#         "Operating System :: OS Independent",
#         "Intended Audience :: Science/Research",
#         "License :: OSI Approved :: BSD License",
#         "Programming Language :: Python",
#         "Topic :: Scientific/Engineering",
#     ],
#     ext_modules=ext_modules,
# )

            # {name="Imri Sofer", email=""},
            # {name="Krishn Bera", email=""},
            # {name="Paul Xu", email=""},
            # {name="Thomas V. Wiecki", email=""},
            # {name="Michael J. Frank", email=""},

setup(
    packages=["hddm_wfpt"],
    #setup_requires=["numpy >= 1.23.4", "cython >= 0.29.32"],
    #install_requires=["numpy >=1.23.4", "scipy >= 1.9.1", "cython >= 0.29.32"],
    #dependencies = ["numpy >=1.23.4", "scipy >= 1.9.1", "cython >= 0.29.32"],
    include_dirs=[np.get_include()],
    ext_modules=ext_modules,
)


#  packages=['hddm', 'hddm.tests', 'hddm.models', 'hddm.examples', 'hddm.torch', 'hddm.torch_models', 'hddm.simulators'],