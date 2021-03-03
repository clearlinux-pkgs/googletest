#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : googletest
Version  : 1.10.0
Release  : 12
URL      : https://github.com/google/googletest/archive/release-1.10.0/googletest-1.10.0.tar.gz
Source0  : https://github.com/google/googletest/archive/release-1.10.0/googletest-1.10.0.tar.gz
Summary  : GoogleTest (with main() function)
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: googletest-lib = %{version}-%{release}
Requires: googletest-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : python3
Patch1: 0001-Enforce-ABI-versioning-similar-to-Fedora-patch.patch

%description
The Google Mock class generator is an application that is part of cppclean.
For more information about cppclean, visit http://code.google.com/p/cppclean/

%package dev
Summary: dev components for the googletest package.
Group: Development
Requires: googletest-lib = %{version}-%{release}
Provides: googletest-devel = %{version}-%{release}
Requires: googletest = %{version}-%{release}

%description dev
dev components for the googletest package.


%package lib
Summary: lib components for the googletest package.
Group: Libraries
Requires: googletest-license = %{version}-%{release}

%description lib
lib components for the googletest package.


%package license
Summary: license components for the googletest package.
Group: Default

%description license
license components for the googletest package.


%prep
%setup -q -n googletest-release-1.10.0
cd %{_builddir}/googletest-release-1.10.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1614800099
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DBUILD_GMOCK=1 -DGTEST_CREATE_SHARED_LIBRARY=1 -DGTEST_LINKED_AS_SHARED_LIBRARY=1 -Dgtest_build_samples=ON
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1614800099
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/googletest
cp %{_builddir}/googletest-release-1.10.0/LICENSE %{buildroot}/usr/share/package-licenses/googletest/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/googletest-release-1.10.0/googlemock/LICENSE %{buildroot}/usr/share/package-licenses/googletest/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/googletest-release-1.10.0/googlemock/scripts/generator/LICENSE %{buildroot}/usr/share/package-licenses/googletest/1d4719e04eaa4909ab5a59ef5cb04d2a5517716e
cp %{_builddir}/googletest-release-1.10.0/googletest/LICENSE %{buildroot}/usr/share/package-licenses/googletest/5a2314153eadadc69258a9429104cd11804ea304
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/gmock/gmock-actions.h
/usr/include/gmock/gmock-cardinalities.h
/usr/include/gmock/gmock-function-mocker.h
/usr/include/gmock/gmock-generated-actions.h
/usr/include/gmock/gmock-generated-actions.h.pump
/usr/include/gmock/gmock-generated-function-mockers.h
/usr/include/gmock/gmock-generated-function-mockers.h.pump
/usr/include/gmock/gmock-generated-matchers.h
/usr/include/gmock/gmock-generated-matchers.h.pump
/usr/include/gmock/gmock-matchers.h
/usr/include/gmock/gmock-more-actions.h
/usr/include/gmock/gmock-more-matchers.h
/usr/include/gmock/gmock-nice-strict.h
/usr/include/gmock/gmock-spec-builders.h
/usr/include/gmock/gmock.h
/usr/include/gmock/internal/custom/README.md
/usr/include/gmock/internal/custom/gmock-generated-actions.h
/usr/include/gmock/internal/custom/gmock-generated-actions.h.pump
/usr/include/gmock/internal/custom/gmock-matchers.h
/usr/include/gmock/internal/custom/gmock-port.h
/usr/include/gmock/internal/gmock-internal-utils.h
/usr/include/gmock/internal/gmock-port.h
/usr/include/gmock/internal/gmock-pp.h
/usr/include/gtest/gtest-death-test.h
/usr/include/gtest/gtest-matchers.h
/usr/include/gtest/gtest-message.h
/usr/include/gtest/gtest-param-test.h
/usr/include/gtest/gtest-printers.h
/usr/include/gtest/gtest-spi.h
/usr/include/gtest/gtest-test-part.h
/usr/include/gtest/gtest-typed-test.h
/usr/include/gtest/gtest.h
/usr/include/gtest/gtest_pred_impl.h
/usr/include/gtest/gtest_prod.h
/usr/include/gtest/internal/custom/README.md
/usr/include/gtest/internal/custom/gtest-port.h
/usr/include/gtest/internal/custom/gtest-printers.h
/usr/include/gtest/internal/custom/gtest.h
/usr/include/gtest/internal/gtest-death-test-internal.h
/usr/include/gtest/internal/gtest-filepath.h
/usr/include/gtest/internal/gtest-internal.h
/usr/include/gtest/internal/gtest-param-util.h
/usr/include/gtest/internal/gtest-port-arch.h
/usr/include/gtest/internal/gtest-port.h
/usr/include/gtest/internal/gtest-string.h
/usr/include/gtest/internal/gtest-type-util.h
/usr/include/gtest/internal/gtest-type-util.h.pump
/usr/lib64/cmake/GTest/GTestConfig.cmake
/usr/lib64/cmake/GTest/GTestConfigVersion.cmake
/usr/lib64/cmake/GTest/GTestTargets-relwithdebinfo.cmake
/usr/lib64/cmake/GTest/GTestTargets.cmake
/usr/lib64/libgmock.so
/usr/lib64/libgmock_main.so
/usr/lib64/libgtest.so
/usr/lib64/libgtest_main.so
/usr/lib64/pkgconfig/gmock.pc
/usr/lib64/pkgconfig/gmock_main.pc
/usr/lib64/pkgconfig/gtest.pc
/usr/lib64/pkgconfig/gtest_main.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgtest.so.0
/usr/lib64/libgtest.so.0.0.0
/usr/lib64/libgtest_main.so.0
/usr/lib64/libgtest_main.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/googletest/1d4719e04eaa4909ab5a59ef5cb04d2a5517716e
/usr/share/package-licenses/googletest/5a2314153eadadc69258a9429104cd11804ea304
