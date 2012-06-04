# Generated from net-ssh-multi-1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name net-ssh-multi

%global rubyabi 1.9.1

Summary: Control multiple Net::SSH connections via a single interface
Name: rubygem-%{gem_name}
Version: 1.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/net-ssh/net-ssh-multi
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: rubygem(net-ssh) >= 2.1.4
Requires: rubygem(net-ssh-gateway) >= 0.99.0
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygem(net-ssh)
BuildRequires: rubygem(net-ssh-gateway)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Control multiple Net::SSH connections via a single interface.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local \
  --install-dir $(pwd)%{gem_dir} \
  --force --rdoc \
   %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd %{buildroot}%{gem_instdir}
ruby -Ilib -Itest -rrubygems test/test_all.rb
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.rdoc
%{gem_libdir}
%{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/test

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%{gem_instdir}/Rakefile

%changelog
* Sat Apr 14 2012  <rpms@courteau.org> - 1.1-1
- Initial package
