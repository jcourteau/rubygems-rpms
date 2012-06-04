# This RPM will possibly fail on PowerPCs, but I am ignoring this.
Summary: A toolkit for developing constraint-based systems and applications.
Name: gecode
Version: 3.7.3
Release: 1%{?dist}
License:  MIT
URL: http://gecode.org/
Source: http://www.gecode.org/download/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Group: Development/Libraries
BuildRequires: gcc >= 4.2
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: flex
BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: tex(latex)
BuildRequires: tex(dvips)

%package devel
Summary: Development files for gecode
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description
Gecode is a toolkit for developing constraint-based systems and applications. Gecode provides a constraint solver with state-of-the-art performance while being modular and extensible.

%description devel
This package contains gecode and the appropriate header files.

%package doc
Summary: Documentation for gecode
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
%configure --disable-examples --with-boost-include=%{_includedir}/boost

make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" 
make doc
make ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall sharedlibdir=${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_defaultdocdir}/%{name}-doc-%{version}
mv doc/html ${RPM_BUILD_ROOT}%{_defaultdocdir}/%{name}-doc-%{version}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_bindir}/fz
%{_bindir}/mzn-gecode
%{_datadir}/%{name}/mznlib
%{_includedir}/%{name}
%{_includedir}/examples/scowl.hpp
%{_libdir}/*.so

%files doc
%defattr(-,root,root,-)
%{_defaultdocdir}/%{name}-doc-%{version}/html

%changelog
* Sat May 5 2012 Jonas Courteau <rpms@courteau.org> - 3.7.3-1
- Initial packaging
