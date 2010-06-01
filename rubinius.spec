
Summary:	Ruby Interpreter
Name:		rubinius
Version:	1.0.0
Release:	1
License:	BSD
Group:		Libraries
URL:		http://rubini.us/
Source0:	http://asset.rubini.us/rubinius-1.0.0-20100514.tar.gz
# Source0-md5:	b05f4e791d3712c5a50b3d210dac6eb0
%if "%{pld_release}" == "ac"
BuildRequires:	gcc >= 5:4.0
%else
BuildRequires:	gcc >= 6:4.0
%endif
BuildRequires:	llvm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An environment for Ruby, the programming language that provides performance
balanced with accessibility, focusing on improving programming productivity

%prep
%setup -q
./configure --prefix=/usr

%build
rake

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
