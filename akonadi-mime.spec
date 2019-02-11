#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : akonadi-mime
Version  : 18.12.2
Release  : 4
URL      : https://download.kde.org/stable/applications/18.12.2/src/akonadi-mime-18.12.2.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.2/src/akonadi-mime-18.12.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0 LGPL-2.1
Requires: akonadi-mime-bin = %{version}-%{release}
Requires: akonadi-mime-data = %{version}-%{release}
Requires: akonadi-mime-lib = %{version}-%{release}
Requires: akonadi-mime-license = %{version}-%{release}
Requires: akonadi-mime-locales = %{version}-%{release}
BuildRequires : akonadi-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : kmime-dev
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
%setup -q -n akonadi-mime-18.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549857432
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549857432
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadi-mime
cp COPYING %{buildroot}/usr/share/package-licenses/akonadi-mime/COPYING
cp COPYING.BSD %{buildroot}/usr/share/package-licenses/akonadi-mime/COPYING.BSD
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/akonadi-mime/COPYING.LIB
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
/usr/share/xdg/akonadi-mime.categories

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
/usr/lib64/libKF5AkonadiMime.so.5.10.2
/usr/lib64/qt5/plugins/akonadi_serializer_mail.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadi-mime/COPYING
/usr/share/package-licenses/akonadi-mime/COPYING.BSD
/usr/share/package-licenses/akonadi-mime/COPYING.LIB

%files locales -f libakonadi-kmime5.lang
%defattr(-,root,root,-)

