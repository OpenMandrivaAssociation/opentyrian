%define debug_package %{nil}

Name:		opentyrian
Version:	2.1.20130907
Release:	1
Summary:	Classic shoot-em-up arcade port
License:	GPLv2
Group:		Games/Arcade
Url:		https://bitbucket.org/opentyrian/opentyrian/
Source:		http://www.camanis.net/opentyrian/releases/%{name}-%{version}-src.tar.gz
# script to download game data
# Google doesn't allow easy direct downloads so use MIB hosting
Source1:	%{name}-installer
Source2:	%{name}.png
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_net)
Requires:	unzip
Requires:	Xdialog

%description
OpenTyrian is a port of the DOS shoot-em-up Tyrian.
Jason Emery generously gave the OpenTyrian developers a copy of
the Tyrian 2.1 source code, which has since been ported from Turbo Pascal to C.
The port uses SDL, making it easily cross-platform.
Tyrian is an arcade-style vertical scrolling shooter. The story is set
in 20,031 where you play as Trent Hawkins, a skilled fighter-pilot employed
to fight Microsol and save the galaxy.

%prep
%setup -q

%build
%make release

%install
%__install -Dpm 755 %{name} %{buildroot}%{_bindir}/%{name}
%__install -Dpm 755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}-installer

%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__install -m644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop  <<EOF
[Desktop Entry]
Name=OpenTyrian
Comment=%{summary}
Exec=%{name}-installer
Icon=%{name}
Type=Application
Terminal=false
Categories=Game;ArcadeGame;
EOF

%files
%doc COPYING README CREDITS NEWS
%{_bindir}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop


