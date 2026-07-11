%global tl_name multienv
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Multiple environments using a key=value syntax
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/multienv
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multienv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multienv.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multienv.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a multienv environment which permits easy addition
of multiple environments using a key=value syntax. Macros to define
environments using this syntax are also provided.

