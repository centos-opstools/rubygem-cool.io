# Generated from cool.io-1.2.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name cool.io
%global optflags -O2 -g -fno-strict-aliasing

Name: rubygem-%{gem_name}
Version: 1.5.1
Release: 1%{?dist}
Summary: A cool framework for doing high performance I/O in Ruby
License: MIT
URL: http://coolio.github.com
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: rubygem(rspec) >= 3.5.0
Provides: rubygem(%{gem_name}) = %{version}

%description
Cool.io provides a high performance event framework for Ruby which uses the
libev C library.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%if 0%{?fedora}
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
%endif

%if 0%{?rhel}
mkdir -p %{buildroot}%{gem_extdir_mri}/lib
cp -ar .%{gem_instdir}/lib/*.so %{buildroot}%{gem_extdir_mri}/lib
%endif

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

rm -f %{buildroot}%{gem_instdir}/{.gitignore,.travis.yml,.rspec}


# Run the test suite
%check
pushd .%{gem_instdir}
# Disable this test that requires networking
rm -f spec/dns_spec.rb
rspec -Ilib -I%{buildroot}%{gem_extdir_mri} spec
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/CHANGES.md
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Gemfile
%{gem_instdir}/appveyor.yml
%{gem_instdir}/libev_ruby_gil.diff
%{gem_instdir}/libev_win_select.diff

%files doc
%doc %{gem_docdir}
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/spec
%{gem_instdir}/Rakefile
%{gem_instdir}/examples

%changelog
* Thu Aug 17 2017 Richard Megginson <rmeggins@localhost.localdomain> - 1.5.1-1
- Update to 1.5.1

* Thu Jun 29 2017 Rich Megginson <rmeggins@redhat.com> - 1.5.0-1
- Update to 1.5.0

* Thu Jan 19 2017 Sandro Bonazzola <sbonazzo@redhat.com> - 1.4.5-2
- Rebuilding adding ppc64le arch

* Thu Aug 25 2016 Rich Megginson <rmeggins@redhat.com> - 1.4.5-1
- Update to 1.4.5

* Wed Jul 29 2015 Graeme Gillies <ggillies@redhat.com> - 1.2.4-2
- Corrected C extension compiler flags to remove strict-aliasing warnings

* Tue Jan 06 2015 Graeme Gillies <ggillies@redhat.com> - 1.2.4-1
- Initial package
