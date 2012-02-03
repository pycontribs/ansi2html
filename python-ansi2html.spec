%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

%global srcname ansi2html

Name:		python-ansi2html
Version:	0.8.2
Release:	1%{?dist}
Summary:	Python module that converts text with ANSI color to HTML

Group:		Development/Libraries
License:	GPLv3+
URL:		http://github.com/ralphbean/ansi2html
Source0:	http://pypi.python.org/packages/source/a/ansi2html/ansi2html-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{srcname}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

BuildRequires:	python,python-setuptools,python-nose
Requires:	python

%description
The ansi2html module can convert text with ANSI color codes to HTML.


%prep
%setup -q -n %{srcname}-%{version}


%check
%{__python} setup.py test


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSE README.rst
%{python_sitelib}/*
%{_bindir}/ansi2html


%changelog
* Mon Jan 30 2012 Ralph Bean <rbean@redhat.com> - 0.8.2-1
- Updated ansi2html version to latest 0.8.2.
- Added _bindir entry for the ansi2html console-script.
- Removed dependency on genshi.
- Removed references to now EOL fedora 12.
* Wed Sep 15 2010 Ralph Bean <ralph.bean@gmail.com> - 0.5.2-1
- Updated spec based on comments from Mark McKinstry
* Tue Sep 7 2010 Ralph Bean <ralph.bean@gmail.com> - 0.5.1-1
- Initial RPM packaging

