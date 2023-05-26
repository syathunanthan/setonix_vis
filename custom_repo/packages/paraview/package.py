# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Paraview(CMakePackage):
    """ParaView is an open-source, multi-platform data analysis and
    visualization application. This package includes the Catalyst
    in-situ library for versions 5.7 and greater, othewise use the
    catalyst package.

    """

    homepage = 'https://www.paraview.org'
    url      = "https://www.paraview.org/files/v5.7/ParaView-v5.7.0.tar.xz"
    list_url = "https://www.paraview.org/files"
    list_depth = 1
    git      = "https://gitlab.kitware.com/paraview/paraview.git"
    maintainers = ['syathunanthan']

    version("5.11.0", sha256="9a0b8fe8b1a2cdfd0ace9a87fa87e0ec21ee0f6f0bcb1fdde050f4f585a25165", preferred=True)
    version('5.10.1', sha256='520e3cdfba4f8592be477314c2f6c37ec73fb1d5b25ac30bdbd1c5214758b9c2')
    version('5.10.0', sha256='86d85fcbec395cdbc8e1301208d7c76d8f48b15dc6b967ffbbaeee31242343a5')
    version('5.9.1', sha256='0d486cb6fbf55e428845c9650486f87466efcb3155e40489182a7ea85dfd4c8d')
    version('5.9.0', sha256='b03258b7cddb77f0ee142e3e77b377e5b1f503bcabc02bfa578298c99a06980d')
    version('5.8.1', sha256='7653950392a0d7c0287c26f1d3a25cdbaa11baa7524b0af0e6a1a0d7d487d034')
    version('5.8.0', sha256='219e4107abf40317ce054408e9c3b22fb935d464238c1c00c0161f1c8697a3f9')
    version('5.7.0', sha256='e41e597e1be462974a03031380d9e5ba9a7efcdb22e4ca2f3fec50361f310874')
    version('5.6.2', sha256='1f3710b77c58a46891808dbe23dc59a1259d9c6b7bb123aaaeaa6ddf2be882ea')
    version('5.6.0', sha256='cb8c4d752ad9805c74b4a08f8ae6e83402c3f11e38b274dba171b99bb6ac2460')
    version('5.5.2', sha256='64561f34c4402b88f3cb20a956842394dde5838efd7ebb301157a837114a0e2d')
    version('5.5.1', sha256='a6e67a95a7a5711a2b5f95f38ccbff4912262b3e1b1af7d6b9afe8185aa85c0d')
    version('5.5.0', sha256='1b619e326ff574de808732ca9a7447e4cd14e94ae6568f55b6581896cd569dff')
    version('5.4.1', sha256='390d0f5dc66bf432e202a39b1f34193af4bf8aad2355338fa5e2778ea07a80e4')
    version('5.4.0', sha256='f488d84a53b1286d2ee1967e386626c8ad05a6fe4e6cbdaa8d5e042f519f94a9')
    version('5.3.0', sha256='046631bbf00775edc927314a3db207509666c9c6aadc7079e5159440fd2f88a0')
    version('5.2.0', sha256='894e42ef8475bb49e4e7e64f4ee2c37c714facd18bfbb1d6de7f69676b062c96')
    version('5.1.2', sha256='ff02b7307a256b7c6e8ad900dee5796297494df7f9a0804fe801eb2f66e6a187')
    version('5.0.1', sha256='caddec83ec284162a2cbc46877b0e5a9d2cca59fb4ab0ea35b0948d2492950bb')

    

    # This package will only work with libjpeg-turbo, not other jpeg providers    
#    depends_on("qt+opengl")
    depends_on("qt")
    depends_on("python@3.9.9")
    depends_on('cmake@3.3:', type='build')
    depends_on("protobuf")
    depends_on('ffmpeg')
    depends_on('boost') # this is needed for visit bridge silo reader
    depends_on('silo') # modified recepie
    depends_on('py-numpy')

    def cmake_args(self):
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        args = [
#            '-DBUILD_EXAMPLES:BOOL=ON' ,
            '-DPARAVIEW_USE_MPI:BOOL=ON' ,
            '-DCATALYST_BUILD_TOOLS:BOOL=ON' ,
            '-DVTK_USE_X:BOOL=ON' ,
            '-DVTK_MODULE_USE_EXTERNAL_ParaView_protobuf:BOOL=ON' ,
#            '-DCMAKE_C_FLAGS="-fPIC"' ,
            '-DCMAKE_BUILD_TYPE:STRING=Debug' ,
#            '-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo' ,
            '-DOPENGL_opengl_LIBRARY=/usr/lib64/libOpenGL.so' ,
            '-DPARAVIEW_BUILD_SHARED_LIBS:BOOL=ON' ,
            '-DPARAVIEW_USE_QT=ON' ,
            '-DPARAVIEW_USE_PYTHON:BOOL=ON' ,
            '-DPARAVIEW_ENABLE_FFMPEG:BOOL=ON' ,
            '-DPARAVIEW_ENABLE_VISITBRIDGE:BOOL=ON' ,
            '-DVISIT_BUILD_READER_Silo:BOOL=ON']
        return args

# ccmake .. -DVTK_USE_X:BOOL=ON -DCMAKE_BUILD_TYPE:STRING=Debug -DOPENGL_opengl_LIBRARY=/usr/lib64/libOpenGL.so -DPARAVIEW_BUILD_SHARED_LIBS:BOOL=ON -DPARAVIEW_USE_QT:BOOL=ON -DPARAVIEW_USE_PYTHON:BOOL=ON -DPARAVIEW_USE_MPI:BOOL=ON -DVTK_MODULE_USE_EXTERNAL_ParaView_protobuf:BOOL=ON -DCATALYST_BUILD_TOOLS:BOOL=ON -DCMAKE_INSTALL_PREFIX:PATH=/software/projects/pawsey0003/ysivarajah/setonix/manual/paraview/ParaView-v5.10.1/install

