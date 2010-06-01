
Summary:	Ruby Interpreter
Name:		rubinius
Version:	1.0.0
Release:	1
License:	BSD
Group:		Libraries
URL:		http://rubini.us/
Source0:	http://asset.rubini.us/%{name}-%{version}-20100514.tar.gz
# Source0-md5:	b05f4e791d3712c5a50b3d210dac6eb0
%if "%{pld_release}" == "ac"
BuildRequires:	gcc >= 5:4.0
%else
BuildRequires:	gcc >= 6:4.0
%endif
BuildRequires:	llvm-devel
BuildRequires:	rake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An environment for Ruby, the programming language that provides
performance balanced with accessibility, focusing on improving
programming productivity

%prep
%setup -q
RELEASE=true \
	./configure --prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--includedir=%{_includedir}/%{name}/1.0 \
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
%{_includedir}/rubinius/1.0
%dir %{_libdir}/rubinius
%dir %{_libdir}/rubinius/1.0
%{_libdir}/rubinius/1.0/lib
%{_libdir}/rubinius/1.0/runtime
%{_libdir}/rubinius/preinstalled
