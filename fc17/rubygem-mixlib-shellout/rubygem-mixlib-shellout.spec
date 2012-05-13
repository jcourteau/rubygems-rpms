# Generated from mixlib-shellout-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mixlib-shellout
%global rubyabi 1.9.1

Summary: Run external commands on Unix or Windows
Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 1%{?dist}
Group: Development/Languages
License: Apache 2.0
URL: https://github.com/opscode/mixlib-shellout
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Tests for this package are not in the gem. To update:
# git clone https://github.com/opscode/mixlib-shellout.git && cd mixlib-shellout
# git checkout 1.0.0
# tar czvf rubygem-mixlib-shellout-1.0.0-specs.tgz spec/
Source1: rubygem-%{gem_name}-%{version}-specs.tgz
# One test doesn't take into account that /bin is a symlink in fc17
Patch0: rubygem-mixlib-shellout-1.0.0-fix_test.patch

Requires: ruby 
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
BuildRequires: ruby 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel 
BuildRequires: rubygem(rspec)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Run external commands on Unix or Windows

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

# Unpack our tests:
tar zxvf %{SOURCE1}
%patch0 -p2 -b .fix_tests

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
cp -pr spec/ %{buildroot}%{gem_instdir}
pushd %{buildroot}%{gem_instdir}
# One of the tests involves a fork that may not finish before mock
rspec -Ilib && sleep 10
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE
%{gem_instdir}/spec

%changelog
* Sat May 12 2012  Jonas Courteau <rpms@courteau.org> - 1.0.0-1
- Initial package
