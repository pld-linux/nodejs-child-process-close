%define		pkg	child-process-close
Summary:	Makes child process objects emit the close event
Name:		nodejs-%{pkg}
Version:	0.1.1
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/piscisaureus/child-process-close
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	873271c55c02f4745aa0ef36ac119c44
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module makes child process objects, (created with `spawn`,
`fork`, `exec` or `execFile`) emit the `close` event in node v0.6 like
they do in node v0.8. This makes it easier to write code that works
correctly on both version of node.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr index.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
