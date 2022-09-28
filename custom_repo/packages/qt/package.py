# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
#import itertools
#import os
#import sys

#import llnl.util.tty as tty

from spack import *
#from spack.operating_systems.mac_os import macos_version



class Qt(Package):
    """Qt is a comprehensive cross-platform C++ application framework."""
    homepage = 'https://qt.io'

    # Supported releases: 'https://download.qt.io/official_releases/qt/'
    # Older archives: 'https://download.qt.io/new_archive/qt/'
    #url  = 'https://download.qt.io/archive/qt/5.14/5.14.2/single/qt-everywhere-src-5.14.2.tar.xz'
    url      = 'https://download.qt.io/official_releases/qt/5.15/5.15.5/single/qt-everywhere-opensource-src-5.15.5.tar.xz'
    #url      = 'https://download.qt.io/archive/qt/5.15/5.15.2/single/qt-everywhere-src-5.15.2.tar.xz'
    list_url = 'https://download.qt.io/archive/qt/'
    list_depth = 3
    maintainers = ['Yathu']

    phases = ['configure', 'build', 'install']
    version('5.15.5', sha256='5a97827bdf9fd515f43bc7651defaf64fecb7a55e051c79b8f80510d0e990f06')
    version('5.15.2', sha256='3a530d1b243b5dec00bc54937455471aaa3e56849d2593edb8ded07228202240')
    version('5.14.2', sha256='c6fcd53c744df89e7d3223c02838a33309bd1c291fcb6f9341505fe99f7f19fa')
    version('5.14.1', sha256='6f17f488f512b39c2feb57d83a5e0a13dcef32999bea2e2a8f832f54a29badb8', deprecated=True)
    version('5.14.0', sha256='be9a77cd4e1f9d70b58621d0753be19ea498e6b0da0398753e5038426f76a8ba', deprecated=True)
    version('5.13.1', sha256='adf00266dc38352a166a9739f1a24a1e36f1be9c04bf72e16e142a256436974e', deprecated=True)
    version('5.12.10', sha256='3e0ee1e57f5cf3eeb038d0b4b22c7eb442285c62639290756b39dc93a1d0e14f')
    version('5.12.7', sha256='873783a0302129d98a8f63de9afe4520fb5f8d5316be8ad7b760c59875cd8a8d', deprecated=True)
    version('5.12.5', sha256='a2299e21db7767caf98242767bffb18a2a88a42fee2d6a393bedd234f8c91298', deprecated=True)
    version('5.12.2', sha256='59b8cb4e728450b21224dcaaa40eb25bafc5196b6988f2225c394c6b7f881ff5', deprecated=True)
    version('5.11.3', sha256='859417642713cee2493ee3646a7fee782c9f1db39e41d7bb1322bba0c5f0ff4d', deprecated=True)
    version('5.11.2', sha256='c6104b840b6caee596fa9a35bc5f57f67ed5a99d6a36497b6fe66f990a53ca81', deprecated=True)
    version('5.10.0', sha256='936d4cf5d577298f4f9fdb220e85b008ae321554a5fcd38072dc327a7296230e', deprecated=True)
    version('5.9.9',  sha256='5ce285209290a157d7f42ec8eb22bf3f1d76f2e03a95fc0b99b553391be01642')
    version('5.9.1',  sha256='7b41a37d4fe5e120cdb7114862c0153f86c07abbec8db71500443d2ce0c89795', deprecated=True)
    version('5.9.0',  sha256='f70b5c66161191489fc13c7b7eb69bf9df3881596b183e7f6d94305a39837517', deprecated=True)
    version('5.8.0', sha256='0f4c54386d3dbac0606a936a7145cebb7b94b0ca2d29bc001ea49642984824b6', deprecated=True)
    version('5.7.1', sha256='46ebca977deb629c5e69c2545bc5fe13f7e40012e5e2e451695c583bd33502fa', deprecated=True)
    version('5.7.0', sha256='a6a2632de7e44bbb790bc3b563f143702c610464a7f537d02036749041fd1800', deprecated=True)
    version('5.6.3',  sha256='2fa0cf2e5e8841b29a4be62062c1a65c4f6f2cf1beaf61a5fd661f520cd776d0')
    version('5.5.1',  sha256='c7fad41a009af1996b62ec494e438aedcb072b3234b2ad3eeea6e6b1f64be3b3', deprecated=True)
    version('5.4.2',  sha256='cfc768c55f0a0cd232bed914a9022528f8f2e50cb010bf0e4f3f62db3dfa17bd', deprecated=True)
    version('5.4.0',  sha256='1739633424bde3d89164ae6ff1c5c913be38b9997e451558ef873aac4bbc408a', deprecated=True)
    version('5.3.2',  sha256='c8d3fd2ead30705c6673c5e4af6c6f3973346b4fb2bd6079c7be0943a5b0282d')
    version('5.2.1',  sha256='84e924181d4ad6db00239d87250cc89868484a14841f77fb85ab1f1dbdcd7da1')
    version('4.8.7',  sha256='e2882295097e47fe089f8ac741a95fef47e0a73a3f3cdf21b56990638f626ea0')
    version('4.8.6',  sha256='8b14dd91b52862e09b8e6a963507b74bc2580787d171feda197badfa7034032c')
    version('4.8.5',  sha256='eb728f8268831dc4373be6403b7dd5d5dde03c169ad6882f9a8cb560df6aa138')
    version('3.3.8b', sha256='1b7a1ff62ec5a9cb7a388e2ba28fda6f960b27f27999482ebeceeadb72ac9f6e')

    variant('debug',      default=False,
            description="Build debug version.")
    variant('dbus',       default=False,
            description="Build with D-Bus support.")
    variant('doc',      default=False,
            description="Build QDoc and documentation.")
    variant('examples',   default=False,
            description="Build examples.")
    variant('gtk',        default=False,
            description="Build with gtkplus.")
    variant('gui', default=False,
            description='Build the Qt GUI module and dependencies')
    variant('opengl',     default=False,
            description="Build with OpenGL support.")
    variant('phonon',     default=False,
            description="Build with phonon support.")
    variant('shared',     default=False,
            description='Build shared libraries.')
    variant('sql',        default=False,
            description="Build with SQL support.")
    variant('ssl',    default=False,
            description="Build with OpenSSL support.")
    variant('tools',      default=False,
            description="Build tools, including Qt Designer.")
    variant('webkit',     default=False,
            description="Build the Webkit extension")

    # Mapping for compilers/systems in the QT 'mkspecs'
    compiler_mapping = {'intel': ('icc',),
                        'apple-clang': ('clang-libc++', 'clang'),
                        'clang': ('clang-libc++', 'clang'),
                        'gcc': ('g++',)}
    platform_mapping = {'darwin': ('macx'), 'cray': ('linux')}

    depends_on("libx11")
    depends_on("libxcb")
    depends_on("xcb-util-image")
    depends_on("xcb-util-keysyms")
    depends_on("xcb-util-renderutil")
    depends_on("xcb-util-wm")
    depends_on("libxkbcommon")
    depends_on("libxcb")
    depends_on("fontconfig")
    depends_on("libsm")
    depends_on("libxext")
    depends_on("libxrender")

    @when('@5')
    def configure(self, spec, prefix):
        #config_args = self.common_config_args
        # incomplete list is here https://doc.qt.io/qt-5/configure-options.html
        config_args = [
            '-prefix', self.prefix,
            '-v',
            '-opensource',
            '-opengl',
            '-release',
            '-confirm-license',
            '-system-zlib',
            '-system-libpng',
            '-system-libjpeg',
            '-shared',
            '-xcb' ,
#            '-xcb-xlib' ,
#            '-bundled-xcb-xinput' ,
        ]

# ./configure -prefix /software/projects/pawsey0003/ysivarajah/setonix/manual/qt/qt-everywhere-src-5.15.5/install -confirm-license -opensource -release -shared -system-zlib -system-libpng -system-libjpeg -opengl -verbose -system-xcb


        version = self.version
        if version == Version('5.15.2'):
            config_args.append('')
#                config_args.append('-system-xcb')
#                config_args.extend(['-skip', 'webengine'])
 #               config_args.append('-xcb-xlib')
        if version == Version('5.14.2'):
                config_args.append('-qt-xcb')
        configure(*config_args)

    def build(self, spec, prefix):
        make()

    def install(self, spec, prefix):
        make("install")


