
Summary:	Ruby Interpreter
Name:		rubinius
Version:	1.2.0
Release:	1
License:	BSD
Group:		Development/Languages
URL:		http://rubini.us/
Source0:	http://asset.rubini.us/%{name}-%{version}-20101221.tar.gz
# Source0-md5:	4284c2660f1f648942de35d4fc871f70
%if "%{pld_release}" == "ac"
BuildRequires:	gcc >= 5:4.0
%else
BuildRequires:	gcc >= 6:4.0
%endif
BuildRequires:	llvm-devel
BuildRequires:	ruby-rake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An environment for Ruby, the programming language that provides
performance balanced with accessibility, focusing on improving
programming productivity

%package ruby
Summary:	Rubinius as "ruby"
Group:		Development/Languages
Requires:	%{name} = %{version}
Provides:	ruby

%description ruby
"gem", "irb", "rake", "rdoc", "ri" and "ruby" executables that invoke
the Rubinius runtime.

%prep
%setup -q
RELEASE=true \
	./configure --prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--includedir=%{_includedir}/%{name}/1.2 \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--gemsdir=%{_libdir}

%build
rake build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
FAKEROOT=$RPM_BUILD_ROOT \
	rake install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rbx
%dir %{_includedir}/rubinius
%{_includedir}/rubinius/1.2
%dir %{_libdir}/rubinius
%dir %{_libdir}/rubinius/1.2
%{_libdir}/rubinius/1.2/lib
%{_libdir}/rubinius/1.2/runtime
%{_libdir}/rubinius/preinstalled

%files ruby
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gem
%attr(755,root,root) %{_bindir}/irb
%attr(755,root,root) %{_bindir}/rake
%attr(755,root,root) %{_bindir}/rdoc
%attr(755,root,root) %{_bindir}/ri
%attr(755,root,root) %{_bindir}/ruby
%{_libdir}/bin/rake
%{_libdir}/bin/rdoc
%{_libdir}/bin/ri
