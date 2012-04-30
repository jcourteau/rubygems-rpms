# Generated from highline-1.6.11.gem by gem2rpm -*- rpm-spec -*-
%global gem_name highline
%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}

%global rubyabi 1.8

Summary: HighLine is a high-level command-line IO library
Name: rubygem-%{gem_name}
Version: 1.6.11
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://highline.rubyforge.org
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems)
Requires: ruby
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A high-level IO library that provides validation, type conversion, and more
for command-line interfaces. HighLine also includes a complete menu system
that can crank out anything from simple list selection to complete shells
with just minutes of work.

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

# Fix the shebang.
find %{buildroot}%{gem_instdir}/{examples,lib,test}/ -type f -name '*.rb' -exec \
    sed -i -e 's|/usr/local/bin/ruby|/usr/bin/ruby|' '{}' \;
# Remove cvs files.
find %{buildroot}%{gem_instdir}/ -type f -iname '.*' -exec rm -f '{}' \;


%check
pushd %{buildroot}%{gem_instdir}
ruby -rrubygems -S testrb -Ilib test/ts_all.rb
popd

%files
%defattr(-, root, root, -)
%dir %{gem_instdir}
%{gem_instdir}/lib
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/README
%doc %{gem_instdir}/INSTALL
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/LICENSE
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%defattr(-, root, root, -)
%{gem_dir}/doc/%{gem_name}-%{version}
%{gem_instdir}/TODO
%{gem_instdir}/AUTHORS
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/setup.rb
%{gem_instdir}/site
%{gem_instdir}/test

%changelog
* Sat Apr 21 2012 Jonas Courteau <rpms@courteau.org> - 1.6.11-2
- port to el6

* Mon Feb 27 2012 Jamie Nguyen <jamie@tomoyolinux.co.uk>  - 1.6.11-1
- update to upstream release 1.6.11

* Wed Feb 22 2012 Jamie Nguyen <jamie@tomoyolinux.co.uk> - 1.5.2-1
- update to upstream release 1.5.2
- remove obsolete BuildRoot tag, %%clean section and %%defattr

* Thu Feb 02 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.5.1-4
- Rebuilt for Ruby 1.9.3.
- Introduced -doc subpackage.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 22 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.5.1-1
- New upstream version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 1.5.0-1
- New upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 08 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.4.0-2
- Add ruby(abi) = 1.8 requires

* Sun Jul 13 2008 root <root@oss1-repo.usersys.redhat.com> - 1.4.0-1
- Initial package
