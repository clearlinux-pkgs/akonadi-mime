#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3A6A4DB839EAA6D7 (aacid@kde.org)
#
Name     : akonadi-mime
Version  : 22.12.1
Release  : 50
URL      : https://download.kde.org/stable/release-service/22.12.1/src/akonadi-mime-22.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.12.1/src/akonadi-mime-22.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.12.1/src/akonadi-mime-22.12.1.tar.xz.sig
Summary  : Libraries and daemons to implement basic email handling
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: akonadi-mime-bin = %{version}-%{release}
Requires: akonadi-mime-data = %{version}-%{release}
Requires: akonadi-mime-lib = %{version}-%{release}
Requires: akonadi-mime-license = %{version}-%{release}
Requires: akonadi-mime-locales = %{version}-%{release}
BuildRequires : akonadi-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : extra-cmake-modules-data
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kitemmodels-dev
BuildRequires : kmime-dev
BuildRequires : kxmlgui-dev
BuildRequires : libxslt-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SPDX-License-Identifier: CC0-1.0

%package bin
Summary: bin components for the akonadi-mime package.
Group: Binaries
Requires: akonadi-mime-data = %{version}-%{release}
Requires: akonadi-mime-license = %{version}-%{release}

%description bin
bin components for the akonadi-mime package.


%package data
Summary: data components for the akonadi-mime package.
Group: Data

%description data
data components for the akonadi-mime package.


%package dev
Summary: dev components for the akonadi-mime package.
Group: Development
Requires: akonadi-mime-lib = %{version}-%{release}
Requires: akonadi-mime-bin = %{version}-%{release}
Requires: akonadi-mime-data = %{version}-%{release}
Provides: akonadi-mime-devel = %{version}-%{release}
Requires: akonadi-mime = %{version}-%{release}

%description dev
dev components for the akonadi-mime package.


%package lib
Summary: lib components for the akonadi-mime package.
Group: Libraries
Requires: akonadi-mime-data = %{version}-%{release}
Requires: akonadi-mime-license = %{version}-%{release}

%description lib
lib components for the akonadi-mime package.


%package license
Summary: license components for the akonadi-mime package.
Group: Default

%description license
license components for the akonadi-mime package.


%package locales
Summary: locales components for the akonadi-mime package.
Group: Default

%description locales
locales components for the akonadi-mime package.


%prep
%setup -q -n akonadi-mime-22.12.1
cd %{_builddir}/akonadi-mime-22.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673301367
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1673301367
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadi-mime
cp %{_builddir}/akonadi-mime-%{version}/.codespellrc.license %{buildroot}/usr/share/package-licenses/akonadi-mime/c011fda7746c087a127999da1c4044854ee42238 || :
cp %{_builddir}/akonadi-mime-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/akonadi-mime/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9 || :
cp %{_builddir}/akonadi-mime-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/akonadi-mime/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/akonadi-mime-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/akonadi-mime/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/akonadi-mime-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/akonadi-mime/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/akonadi-mime-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/akonadi-mime/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/akonadi-mime-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-mime/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/akonadi-mime-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-mime/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/akonadi-mime-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/akonadi-mime/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/akonadi-mime-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/akonadi-mime/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/akonadi-mime-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/akonadi-mime/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/akonadi-mime-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/akonadi-mime/cadc9e08cb956c041f87922de84b9206d9bbffb2 || :
cp %{_builddir}/akonadi-mime-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/akonadi-mime/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/akonadi-mime-%{version}/serializers/akonadi_serializer_mail.desktop.license %{buildroot}/usr/share/package-licenses/akonadi-mime/864bc0eb28c73bd997ac19ff91935ab771846615 || :
pushd clr-build
%make_install
popd
%find_lang libakonadi-kmime5

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/akonadi_benchmarker

%files data
%defattr(-,root,root,-)
/usr/share/akonadi/plugins/serializer/akonadi_serializer_mail.desktop
/usr/share/config.kcfg/specialmailcollections.kcfg
/usr/share/mime-packages/x-vnd.kde.contactgroup.xml
/usr/share/qlogging-categories5/akonadi-mime.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/AkonadiMime/Akonadi/AddressAttribute
/usr/include/KF5/AkonadiMime/Akonadi/CommandBase
/usr/include/KF5/AkonadiMime/Akonadi/MDNStateAttribute
/usr/include/KF5/AkonadiMime/Akonadi/MarkAsCommand
/usr/include/KF5/AkonadiMime/Akonadi/MessageFlags
/usr/include/KF5/AkonadiMime/Akonadi/MessageFolderAttribute
/usr/include/KF5/AkonadiMime/Akonadi/MessageModel
/usr/include/KF5/AkonadiMime/Akonadi/MessageParts
/usr/include/KF5/AkonadiMime/Akonadi/MessageStatus
/usr/include/KF5/AkonadiMime/Akonadi/MoveCommand
/usr/include/KF5/AkonadiMime/Akonadi/NewMailNotifierAttribute
/usr/include/KF5/AkonadiMime/Akonadi/Pop3ResourceAttribute
/usr/include/KF5/AkonadiMime/Akonadi/RemoveDuplicatesJob
/usr/include/KF5/AkonadiMime/Akonadi/SpecialMailCollections
/usr/include/KF5/AkonadiMime/Akonadi/SpecialMailCollectionsDiscoveryJob
/usr/include/KF5/AkonadiMime/Akonadi/SpecialMailCollectionsRequestJob
/usr/include/KF5/AkonadiMime/Akonadi/StandardMailActionManager
/usr/include/KF5/AkonadiMime/akonadi-mime_version.h
/usr/include/KF5/AkonadiMime/akonadi/addressattribute.h
/usr/include/KF5/AkonadiMime/akonadi/akonadi-mime_export.h
/usr/include/KF5/AkonadiMime/akonadi/commandbase.h
/usr/include/KF5/AkonadiMime/akonadi/markascommand.h
/usr/include/KF5/AkonadiMime/akonadi/mdnstateattribute.h
/usr/include/KF5/AkonadiMime/akonadi/messageflags.h
/usr/include/KF5/AkonadiMime/akonadi/messagefolderattribute.h
/usr/include/KF5/AkonadiMime/akonadi/messagemodel.h
/usr/include/KF5/AkonadiMime/akonadi/messageparts.h
/usr/include/KF5/AkonadiMime/akonadi/messagestatus.h
/usr/include/KF5/AkonadiMime/akonadi/movecommand.h
/usr/include/KF5/AkonadiMime/akonadi/newmailnotifierattribute.h
/usr/include/KF5/AkonadiMime/akonadi/pop3resourceattribute.h
/usr/include/KF5/AkonadiMime/akonadi/removeduplicatesjob.h
/usr/include/KF5/AkonadiMime/akonadi/specialmailcollections.h
/usr/include/KF5/AkonadiMime/akonadi/specialmailcollectionsdiscoveryjob.h
/usr/include/KF5/AkonadiMime/akonadi/specialmailcollectionsrequestjob.h
/usr/include/KF5/AkonadiMime/akonadi/standardmailactionmanager.h
/usr/lib64/cmake/KF5AkonadiMime/KF5AkonadiMimeConfig.cmake
/usr/lib64/cmake/KF5AkonadiMime/KF5AkonadiMimeConfigVersion.cmake
/usr/lib64/cmake/KF5AkonadiMime/KF5AkonadiMimeTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5AkonadiMime/KF5AkonadiMimeTargets.cmake
/usr/lib64/libKF5AkonadiMime.so
/usr/lib64/qt5/mkspecs/modules/qt_AkonadiMime.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5AkonadiMime.so.5
/usr/lib64/libKF5AkonadiMime.so.5.22.1
/usr/lib64/qt5/plugins/akonadi_serializer_mail.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadi-mime/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/akonadi-mime/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/akonadi-mime/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/akonadi-mime/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/akonadi-mime/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/akonadi-mime/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/akonadi-mime/864bc0eb28c73bd997ac19ff91935ab771846615
/usr/share/package-licenses/akonadi-mime/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/akonadi-mime/c011fda7746c087a127999da1c4044854ee42238
/usr/share/package-licenses/akonadi-mime/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
/usr/share/package-licenses/akonadi-mime/cadc9e08cb956c041f87922de84b9206d9bbffb2
/usr/share/package-licenses/akonadi-mime/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f libakonadi-kmime5.lang
%defattr(-,root,root,-)

