%global packname  timeDate
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          3010.98
Release:          1
Summary:          Rmetrics - Chronological and Calendarical Objects
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/timeDate_3010.98.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-graphics R-utils R-stats R-methods 
Requires:         R-RUnit 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-graphics R-utils R-stats R-methods
BuildRequires:    R-RUnit 

%description
Environment for teaching "Financial Engineering and Computational Finance"

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

#%check
#%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/COPYRIGHT.html
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/unitTests


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 2131.00-1
+ Revision: 775348
- Import R-timeDate
- Import R-timeDate


