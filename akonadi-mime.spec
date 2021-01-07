#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : akonadi-mime
Version  : 20.12.1
Release  : 29
URL      : https://download.kde.org/stable/release-service/20.12.1/src/akonadi-mime-20.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.12.1/src/akonadi-mime-20.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.12.1/src/akonadi-mime-20.12.1.tar.xz.sig
Summary  : Libraries and daemons to implement basic email handling
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1 LGPL-3.0
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
BuildRequires : kcodecs-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kitemmodels-dev
BuildRequires : kmime-dev
BuildRequires : kxmlgui-dev
BuildRequires : libxslt-dev
BuildRequires : qtbase-dev mesa-dev

%description
# Akonadi Mime #
Akonadi Mime is a library that effectively bridges the type-agnostic API of
the Akonadi client libraries and the domain-specific KMime library. It provides
jobs, models and other helpers to make working with emails through Akonadi easier.

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
%setup -q -n akonadi-mime-20.12.1
cd %{_builddir}/akonadi-mime-20.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610046082
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1610046082
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadi-mime
cp %{_builddir}/akonadi-mime-20.12.1/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-mime/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/akonadi-mime-20.12.1/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-mime/6f1f675aa5f6a2bbaa573b8343044b166be28399
cp %{_builddir}/akonadi-mime-20.12.1/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/akonadi-mime/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/akonadi-mime-20.12.1/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/akonadi-mime/e458941548e0864907e654fa2e192844ae90fc32
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
/usr/include/KF5/Akonadi/KMime/AddressAttribute
/usr/include/KF5/Akonadi/KMime/CommandBase
/usr/include/KF5/Akonadi/KMime/MarkAsCommand
/usr/include/KF5/Akonadi/KMime/MessageFlags
/usr/include/KF5/Akonadi/KMime/MessageFolderAttribute
/usr/include/KF5/Akonadi/KMime/MessageModel
/usr/include/KF5/Akonadi/KMime/MessageParts
/usr/include/KF5/Akonadi/KMime/MessageStatus
/usr/include/KF5/Akonadi/KMime/MoveCommand
/usr/include/KF5/Akonadi/KMime/NewMailNotifierAttribute
/usr/include/KF5/Akonadi/KMime/Pop3ResourceAttribute
/usr/include/KF5/Akonadi/KMime/RemoveDuplicatesJob
/usr/include/KF5/Akonadi/KMime/SpecialMailCollections
/usr/include/KF5/Akonadi/KMime/SpecialMailCollectionsDiscoveryJob
/usr/include/KF5/Akonadi/KMime/SpecialMailCollectionsRequestJob
/usr/include/KF5/Akonadi/KMime/StandardMailActionManager
/usr/include/KF5/akonadi-mime_version.h
/usr/include/KF5/akonadi/kmime/addressattribute.h
/usr/include/KF5/akonadi/kmime/akonadi-mime_export.h
/usr/include/KF5/akonadi/kmime/commandbase.h
/usr/include/KF5/akonadi/kmime/markascommand.h
/usr/include/KF5/akonadi/kmime/messageflags.h
/usr/include/KF5/akonadi/kmime/messagefolderattribute.h
/usr/include/KF5/akonadi/kmime/messagemodel.h
/usr/include/KF5/akonadi/kmime/messageparts.h
/usr/include/KF5/akonadi/kmime/messagestatus.h
/usr/include/KF5/akonadi/kmime/movecommand.h
/usr/include/KF5/akonadi/kmime/newmailnotifierattribute.h
/usr/include/KF5/akonadi/kmime/pop3resourceattribute.h
/usr/include/KF5/akonadi/kmime/removeduplicatesjob.h
/usr/include/KF5/akonadi/kmime/specialmailcollections.h
/usr/include/KF5/akonadi/kmime/specialmailcollectionsdiscoveryjob.h
/usr/include/KF5/akonadi/kmime/specialmailcollectionsrequestjob.h
/usr/include/KF5/akonadi/kmime/standardmailactionmanager.h
/usr/lib64/cmake/KF5AkonadiMime/KF5AkonadiMimeConfig.cmake
/usr/lib64/cmake/KF5AkonadiMime/KF5AkonadiMimeConfigVersion.cmake
/usr/lib64/cmake/KF5AkonadiMime/KF5AkonadiMimeTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5AkonadiMime/KF5AkonadiMimeTargets.cmake
/usr/lib64/libKF5AkonadiMime.so
/usr/lib64/qt5/mkspecs/modules/qt_AkonadiMime.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5AkonadiMime.so.5
/usr/lib64/libKF5AkonadiMime.so.5.16.1
/usr/lib64/qt5/plugins/akonadi_serializer_mail.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadi-mime/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/akonadi-mime/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/akonadi-mime/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f libakonadi-kmime5.lang
%defattr(-,root,root,-)

