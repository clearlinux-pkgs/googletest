#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : googletest
Version  : d225acc90bc3a8c420a9bcd1f033033c1ccd7fe0
Release  : 3
URL      : https://github.com/google/googletest/archive/d225acc90bc3a8c420a9bcd1f033033c1ccd7fe0.tar.gz
Source0  : https://github.com/google/googletest/archive/d225acc90bc3a8c420a9bcd1f033033c1ccd7fe0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
BuildRequires : cmake

%description
The Google Mock class generator is an application that is part of cppclean.
visit http://code.google.com/p/cppclean/

%package dev
Summary: dev components for the googletest package.
Group: Development
Provides: googletest-devel

%description dev
dev components for the googletest package.


%prep
%setup -q -n googletest-d225acc90bc3a8c420a9bcd1f033033c1ccd7fe0

%build
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir} -DBUILD_GMOCK=1 -DGTEST_CREATE_SHARED_LIBRARY=1 -DGTEST_LINKED_AS_SHARED_LIBRARY=1 -Dgtest_build_samples=ON
make V=1  %{?_smp_mflags}
popd

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd clr-build ; make test ; popd

%install
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
## make_install_append content
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
## make_install_append end

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/gmock/gmock-actions.h
/usr/include/gmock/gmock-cardinalities.h
/usr/include/gmock/gmock-generated-actions.h
/usr/include/gmock/gmock-generated-actions.h.pump
/usr/include/gmock/gmock-generated-function-mockers.h
/usr/include/gmock/gmock-generated-function-mockers.h.pump
/usr/include/gmock/gmock-generated-matchers.h
/usr/include/gmock/gmock-generated-matchers.h.pump
/usr/include/gmock/gmock-generated-nice-strict.h
/usr/include/gmock/gmock-generated-nice-strict.h.pump
/usr/include/gmock/gmock-matchers.h
/usr/include/gmock/gmock-more-actions.h
/usr/include/gmock/gmock-more-matchers.h
/usr/include/gmock/gmock-spec-builders.h
/usr/include/gmock/gmock.h
/usr/include/gmock/internal/custom/gmock-generated-actions.h
/usr/include/gmock/internal/custom/gmock-generated-actions.h.pump
/usr/include/gmock/internal/custom/gmock-matchers.h
/usr/include/gmock/internal/custom/gmock-port.h
/usr/include/gmock/internal/gmock-generated-internal-utils.h
/usr/include/gmock/internal/gmock-generated-internal-utils.h.pump
/usr/include/gmock/internal/gmock-internal-utils.h
/usr/include/gmock/internal/gmock-port.h
/usr/include/gtest/gtest-death-test.h
/usr/include/gtest/gtest-message.h
/usr/include/gtest/gtest-param-test.h
/usr/include/gtest/gtest-param-test.h.pump
/usr/include/gtest/gtest-printers.h
/usr/include/gtest/gtest-spi.h
/usr/include/gtest/gtest-test-part.h
/usr/include/gtest/gtest-typed-test.h
/usr/include/gtest/gtest.h
/usr/include/gtest/gtest_pred_impl.h
/usr/include/gtest/gtest_prod.h
/usr/include/gtest/internal/custom/gtest-port.h
/usr/include/gtest/internal/custom/gtest-printers.h
/usr/include/gtest/internal/custom/gtest.h
/usr/include/gtest/internal/gtest-death-test-internal.h
/usr/include/gtest/internal/gtest-filepath.h
/usr/include/gtest/internal/gtest-internal.h
/usr/include/gtest/internal/gtest-linked_ptr.h
/usr/include/gtest/internal/gtest-param-util-generated.h
/usr/include/gtest/internal/gtest-param-util-generated.h.pump
/usr/include/gtest/internal/gtest-param-util.h
/usr/include/gtest/internal/gtest-port-arch.h
/usr/include/gtest/internal/gtest-port.h
/usr/include/gtest/internal/gtest-string.h
/usr/include/gtest/internal/gtest-tuple.h
/usr/include/gtest/internal/gtest-tuple.h.pump
/usr/include/gtest/internal/gtest-type-util.h
/usr/include/gtest/internal/gtest-type-util.h.pump
/usr/lib64/*.so
