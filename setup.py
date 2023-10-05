#python3 setup.py install
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import os
from distutils.sysconfig import get_config_vars

(opt,) = get_config_vars('OPT')
os.environ['OPT'] = " ".join(
    flag for flag in opt.split() if flag != '-Wstrict-prototypes'
)

setup(
    name='sptr',
    version='0.1.0',
    author='dvlab-research',
    ext_modules=[
        CUDAExtension(
            name='sptr_cuda', 
            sources=[
                'src/sptr/pointops_api.cpp',
                'src/sptr/attention/attention_cuda.cpp',
                'src/sptr/attention/attention_cuda_kernel.cu',
                'src/sptr/precompute/precompute.cpp',
                'src/sptr/precompute/precompute_cuda_kernel.cu',
                'src/sptr/rpe/relative_pos_encoding_cuda.cpp',
                'src/sptr/rpe/relative_pos_encoding_cuda_kernel.cu',
            ],
            extra_compile_args={'cxx': ['-O2'], 'nvcc': ['-O2']},
            include_dirs=[
                '/usr/include',
                '/usr/local/include',
                '/usr/local/cuda/include',
            ]
        )
    ],
    cmdclass={'build_ext': BuildExtension}
)
