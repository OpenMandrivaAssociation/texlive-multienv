Name:		texlive-multienv
Version:	1.0
Release:	2
Summary:	TeXLive multienv package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multienv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multienv.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multienv.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive multienv package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/multienv
%doc %{_texmfdistdir}/doc/latex/multienv
#- source
%doc %{_texmfdistdir}/source/latex/multienv

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
