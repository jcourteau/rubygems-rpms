# Generated from net-ssh-2.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name net-ssh

%global rubyabi 1.9.1

Summary: Net::SSH: a pure-Ruby implementation of the SSH2 client protocol
Name: rubygem-%{gem_name}
Version: 2.2.2
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/net-ssh/net-ssh
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems-devel
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Net::SSH: a pure-Ruby implementation of the SSH2 client protocol.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: rubygem(mocha)
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

            
# file-not-utf8 correction
pushd %{buildroot}%{gem_instdir}
iconv --from=ISO-8859-1 --to=UTF-8 THANKS.rdoc > THANKS.rdoc.new && \
touch -r THANKS.rdoc THANKS.rdoc.new && \
mv THANKS.rdoc.new THANKS.rdoc            
popd

# remove gem "test-unit" line
sed -i -e '/test-unit/, 1d' %{buildroot}%{gem_instdir}/test/common.rb

%check

pushd %{buildroot}%{gem_instdir}
ruby -Ilib -Itest test/test_all.rb
popd


%files
%defattr(-, root, root, -)
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/support
%exclude %{gem_instdir}/setup.rb
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/THANKS.rdoc
%doc %{gem_instdir}/CHANGELOG.rdoc
%{gem_cache}
%{gem_spec}

%files doc
%defattr(-, root, root, -)
%{gem_docdir}
%{gem_instdir}/Manifest
%{gem_instdir}/Rakefile
%{gem_instdir}/Rudyfile
%{gem_instdir}/test
# Required to run tests
%{gem_instdir}/net-ssh.gemspec

%changelog
* Sat May 12 2012 Jonas Courteau <rpms@courteau.org> - 2.2.2-1
- Updated to net-ssh 2.2.2

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.2.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 04 2011 Shreyank Gupta <sgupta@redhat.com> - 2.2.1-1
- Updated to version 2.2.1-1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 24 2010 Adam Tkac <atkac redhat com> - 2.0.23-5
- rebuild to ensure F14 has higher NVR than F13

* Fri Jun 11 2010 Shreyank Gupta <sgupta@redhat.com> - 2.0.23-4
- Bring back the BR: rubygem(rake) and rake test

* Thu Jun 10 2010 Shreyank Gupta <sgupta@redhat.com> - 2.0.23-3
- test command from test/README.txt
- Remove gem "test-unit" line
- Removed Requires rubygem(rake)
- BuildRequires/Requires: rubygem(mocha) for tests

* Thu Jun 10 2010 Shreyank Gupta <sgupta@redhat.com> - 2.0.23-2
- Using %%exclude for setup.rb
- Keeping net-ssh.gemspec for tests
- Moved file-not-utf8 correction to before %%check section

* Wed Jun 09 2010 Shreyank Gupta <sgupta@redhat.com> - 2.0.23-1
- Initial package
