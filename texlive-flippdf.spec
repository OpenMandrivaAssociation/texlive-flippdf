# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/flippdf
# catalog-date 2007-02-27 14:19:10 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-flippdf
Version:	1.0
Release:	7
Summary:	Horizontal flipping of pages with pdfLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/flippdf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flippdf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flippdf.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flippdf.source.tar.xz
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
%{_texmfdistdir}/tex/latex/flippdf/flippdf.sty
%doc %{_texmfdistdir}/doc/latex/flippdf/README
%doc %{_texmfdistdir}/doc/latex/flippdf/flippdf.pdf
#- source
%doc %{_texmfdistdir}/source/latex/flippdf/flippdf.dtx
%doc %{_texmfdistdir}/source/latex/flippdf/flippdf.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 751924
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718460
- texlive-flippdf
- texlive-flippdf
- texlive-flippdf
- texlive-flippdf

