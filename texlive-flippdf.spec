Name:		texlive-flippdf
Version:	56782
Release:	2
Summary:	Horizontal flipping of pages with pdfLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/flippdf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flippdf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flippdf.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flippdf.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the production of a document with pages
"mirrored". This is sometimes required by publishers who want
camera-ready documents to be printed on transparent film (to be
viewed from the "wrong" side). The package requires everypage,
and only works with pdfLaTeX in PDF mode.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/flippdf
%doc %{_texmfdistdir}/doc/latex/flippdf
#- source
%doc %{_texmfdistdir}/source/latex/flippdf

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
