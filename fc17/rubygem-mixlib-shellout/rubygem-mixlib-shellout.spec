# Generated from mixlib-shellout-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mixlib-shellout
%global rubyabi 1.9.1

Summary: Run external commands on Unix or Windows
Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 3%{?dist}
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/opscode/mixlib-shellout
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# See http://tickets.opscode.com/browse/CHEF-3168
# Tests for this package are not in the gem. To update:
# git clone https://github.com/opscode/mixlib-shellout.git && cd mixlib-shellout
# git checkout 1.0.0
# tar czvf rubygem-mixlib-shellout-1.0.0-specs.tgz spec/
Source1: rubygem-%{gem_name}-%{version}-specs.tgz
# One test doesn't take into account that /bin is a symlink in fc17
# See http://tickets.opscode.com/browse/CHEF-3107
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

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
tar zxvf %{SOURCE1}
cat %{PATCH0} | patch -p2
# One of the tests involves a fork && sleep 10 that may not finish before mock
rspec -Ilib && sleep 10
popd

%files
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/spec

%files doc
%doc %{gem_docdir}

%changelog
* Sun Jun 17 2012 Jonas Courteau <rpms@courteau.org> - 1.0.0-3
- move all test-related operations into %check
- excluding gem_cache

* Sun Jun 3 2012 Jonas Courteau <rpms@courteau.org> - 1.0.0-2
- exclude specs from final package
- link to upstream bug reports for missing specs, broken test

* Sat May 12 2012  Jonas Courteau <rpms@courteau.org> - 1.0.0-1
- Initial package
