%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:		ansi2html
Version:	0.5.1
Release:	1%{?dist}
Summary:	Python module that converts text with ANSI color to HTML

Group:		Development/Libraries
License:	GPLv3+
URL:		http://github.com/ralphbean/ansi2html
Source0:	http://pypi.python.org/packages/source/a/ansi2html/ansi2html-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

BuildRequires:	python,python-setuptools
Requires:	python,python-genshi

%description
The ansi2html module can convert text with ANSI color codes to HTML.


%prep
%setup -q -n %{name}-%{version}


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
%if 0%{?fedora} >= 9 || 0%{?rhel} >= 6
%dir %{python_sitelib}/%{name}*.egg-info
%{python_sitelib}/%{name}*.egg-info/*
%endif

%{python_sitelib}/%{name}/*.py*
%{python_sitelib}/%{name}/templates/*.html


%changelog
* Wed Sep 15 2010 Ralph Bean <ralph.bean@gmail.com> - 0.5.1-2
- Updated spec based on comments from Mark McKinstry
* Tue Sep 7 2010 Ralph Bean <ralph.bean@gmail.com> - 0.5.1-1
- Initial RPM packaging

