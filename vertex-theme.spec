%define _gtk3 3.22
%define sourcename vertex
%define theme_name Vertex


Summary:    A theme for GTK
Name:       vertex-theme
Version:    20170128
Release:    %mkrel 4
URL:        https://github.com/horst3180/vertex-theme
License:    GPLv3
Group:      Graphical desktop/GNOME
Source0:    https://github.com/horst3180/%{name}/archive/%{version}.tar.gz
Buildarch:  noarch

%description
Vertex is a theme for GTK 3, GTK 2, Gnome-Shell and Cinnamon. It supports
GTK 3 and GTK 2 based desktop environments like Gnome, Cinnamon, Mate, XFCE,
Budgie, Pantheon, etc. Themes for the Browsers Chrome/Chromium and Firefox
are included, too.

The theme comes with three variants to choose from. The default variant with
dark header-bars, a light variant, and a dark variant.

#-----------------------------------------------------
%package        common
Summary:        Files common to %{theme_name} themes
Group:          Graphical desktop/Other
Requires:       adwaita-icon-theme

%description    common
Files which are common to all %{theme_name} themes.

#-----------------------------------------------------
%package -n     %{sourcename}-gtk2-theme
Summary:        %{theme_name} GTK+2 themes
Group:          Graphical desktop/Other
Requires:       %{name}-common = %{version}-%{release}
Requires:       gtk2-murrine-engine

%description -n %{sourcename}-gtk2-theme
Themes for GTK+2 as part of the %{theme_name} theme.

#-----------------------------------------------------
%package -n     %{sourcename}-dark-gtk2-theme
Summary:        %{theme_name} GTK+2 themes
Group:          Graphical desktop/Other
Requires:       %{name}-common = %{version}-%{release}
Requires:       gtk2-murrine-engine

%description -n %{sourcename}-dark-gtk2-theme
Themes for GTK+2 as part of the %{theme_name} theme.
This package contains dark variant.

#-----------------------------------------------------
%package -n     %{sourcename}-light-gtk2-theme
Summary:        %{theme_name} GTK+2 themes
Group:          Graphical desktop/Other
Requires:       %{name}-common = %{version}-%{release}
Requires:       gtk2-murrine-engine

%description -n %{sourcename}-light-gtk2-theme
Themes for GTK+2 as part of the %{theme_name} theme.
This package contains light variant.

#-----------------------------------------------------
%package -n     %{sourcename}-gtk3-theme
Summary:        %{theme_name} GTK+3 themes
Group:          Graphical desktop/GNOME
Requires:       %{name}-common = %{version}-%{release}
Requires:       gnome-themes-extra

%description -n %{sourcename}-gtk3-theme
Themes for GTK+3 as part of the %{theme_name} theme.

#-----------------------------------------------------
%package -n     %{sourcename}-dark-gtk3-theme
Summary:        %{theme_name} GTK+3 themes
Group:          Graphical desktop/GNOME
Requires:       %{name}-common = %{version}-%{release}
Requires:       gnome-themes-extra

%description -n %{sourcename}-dark-gtk3-theme
Themes for GTK+3 as part of the %{theme_name} theme.
This package contains dark variant.

#-----------------------------------------------------
%package -n     %{sourcename}-light-gtk3-theme
Summary:        %{theme_name} GTK+3 themes
Group:          Graphical desktop/GNOME
Requires:       %{name}-common = %{version}-%{release}
Requires:       gnome-themes-extra

%description -n %{sourcename}-light-gtk3-theme
Themes for GTK+3 as part of the %{theme_name} theme.
This package contains light variant.

#-----------------------------------------------------
%package -n     %{sourcename}-metacity-theme
Summary:        %{theme_name} Metacity themes
Group:          Graphical desktop/GNOME
Requires:       %{name}-common = %{version}-%{release} 

%description -n %{sourcename}-metacity-theme
Themes for Metacity as part of the %{theme_name} theme.

#-----------------------------------------------------
%package -n     %{sourcename}-dark-metacity-theme
Summary:        %{theme_name} Metacity themes
Group:          Graphical desktop/GNOME
Requires:       %{name}-common = %{version}-%{release} 

%description -n %{sourcename}-dark-metacity-theme
Themes for Metacity as part of the %{theme_name} theme.
This package contains dark variant.

#-----------------------------------------------------
%package -n     %{sourcename}-light-metacity-theme
Summary:        %{theme_name} Metacity themes
Group:          Graphical desktop/GNOME
Requires:       %{name}-common = %{version}-%{release} 

%description -n %{sourcename}-light-metacity-theme
Themes for Metacity as part of the %{theme_name} theme.
This package contains light variant.

#-----------------------------------------------------
%package -n     %{sourcename}-alt-metacity-theme
Summary:        %{theme_name} Metacity themes
Group:          Graphical desktop/GNOME
Requires:       %{name}-common = %{version}-%{release} 

%description -n %{sourcename}-alt-metacity-theme
Themes for Metacity as part of the %{theme_name} theme.

#-----------------------------------------------------
%package -n     gnome-shell-theme-%{sourcename}
Summary:        %{theme_name} GNOME Shell theme
Group:          Graphical desktop/GNOME
Requires:       %{name}-common = %{version}-%{release}
Requires:       gnome-shell-extensions-user-theme >= 3.20

%description -n gnome-shell-theme-%{sourcename}
%{theme_name} GNOME Shell theme.

#-----------------------------------------------------
%package -n     cinnamon-theme-%{sourcename}
Summary:        %{theme_name} Cinnamon theme
Group:          Graphical desktop/Cinnamon
Requires:       %{name}-common = %{version}-%{release}
Requires:       cinnamon-desktop

%description -n cinnamon-theme-%{sourcename}
%{theme_name} Cinnamon theme.

#-----------------------------------------------------
%package -n     %{sourcename}-xfwm4-theme
Summary:        %{theme_name} Xfwm4 themes
Group:          Graphical desktop/Xfce
Requires:       %{name}-common = %{version}-%{release}
Requires:       xfwm4

%description -n %{sourcename}-xfwm4-theme
Themes for Xfwm4 as part of the %{theme_name} theme.

#-----------------------------------------------------
%package -n     %{sourcename}-dark-xfwm4-theme
Summary:        %{theme_name} Xfwm4 themes
Group:          Graphical desktop/Xfce
Requires:       %{name}-common = %{version}-%{release}
Requires:       xfwm4

%description -n %{sourcename}-dark-xfwm4-theme
Themes for Xfwm4 as part of the %{theme_name} theme.
This package contains dark variant.

#-----------------------------------------------------
%package -n     %{sourcename}-light-xfwm4-theme
Summary:        %{theme_name} Xfwm4 themes
Group:          Graphical desktop/Xfce
Requires:       %{name}-common = %{version}-%{release}
Requires:       xfwm4

%description -n %{sourcename}-light-xfwm4-theme
Themes for Xfwm4 as part of the %{theme_name} theme.
This package contains light variant.

#-----------------------------------------------------

#-----------------------------------------------------
%package -n     %{sourcename}-plank-theme
Summary:        %{theme_name} Plank themes
Group:          Graphical desktop/GNOME
Requires:       %{name}-common = %{version}-%{release}
Requires:       plank

%description -n %{sourcename}-plank-theme
Themes for Plank dock as part of the %{theme_name} theme.
#-----------------------------------------------------

%prep
%autosetup -n %{name}-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure --with-gnome=%{_gtk3} --disable-unity

%make_build

%install
%make_install

# Install extra stuff
pushd extra/
    find "Vertex-Plank" -type f -not -name *~ -exec install -Dm644 '{}' "%{buildroot}%{_datadir}/plank/themes/{}" \;
    find "Vertex_alt_metacity" -type f -not -name *~ -exec install -Dm644 '{}' "%{buildroot}%{_datadir}/themes/{}" \;
popd

# Fix required icon theme:
for i in "%{theme_name}" "%{theme_name}-Light" "%{theme_name}-Dark"; do
    sed -i "s|IconTheme=gnome|IconTheme=Adwaita|g" %{buildroot}%{_datadir}/themes/$i/index.theme
done

%files common
%doc AUTHORS NEWS ChangeLog README.md
%license COPYING
%dir %{_datadir}/themes/%{theme_name}/
%{_datadir}/themes/%{theme_name}/index.theme
%dir %{_datadir}/themes/%{theme_name}-Light/
%{_datadir}/themes/%{theme_name}-Light/index.theme
%dir %{_datadir}/themes/%{theme_name}-Dark/
%{_datadir}/themes/%{theme_name}-Dark/index.theme

%files -n %{sourcename}-gtk2-theme
%{_datadir}/themes/%{theme_name}/gtk-2.0/

%files -n %{sourcename}-light-gtk2-theme
%{_datadir}/themes/%{theme_name}-Light/gtk-2.0/

%files -n %{sourcename}-dark-gtk2-theme
%{_datadir}/themes/%{theme_name}-Dark/gtk-2.0/

%files -n %{sourcename}-gtk3-theme
%{_datadir}/themes/%{theme_name}/gtk-3.0/

%files -n %{sourcename}-light-gtk3-theme
%{_datadir}/themes/%{theme_name}-Light/gtk-3.0/

%files -n %{sourcename}-dark-gtk3-theme
%{_datadir}/themes/%{theme_name}-Dark/gtk-3.0/

%files -n %{sourcename}-metacity-theme
%{_datadir}/themes/%{theme_name}/metacity-1/

%files -n %{sourcename}-light-metacity-theme
%{_datadir}/themes/%{theme_name}-Light/metacity-1/

%files -n %{sourcename}-dark-metacity-theme
%{_datadir}/themes/%{theme_name}-Dark/metacity-1/

%files -n %{sourcename}-alt-metacity-theme
%{_datadir}/themes/%{theme_name}_alt_metacity/metacity-1/

%files -n gnome-shell-theme-%{sourcename}
%{_datadir}/themes/%{theme_name}/gnome-shell/

%files -n cinnamon-theme-%{sourcename}
%{_datadir}/themes/%{theme_name}/cinnamon/

%files -n %{sourcename}-xfwm4-theme
%{_datadir}/themes/%{theme_name}/xfwm4/

%files -n %{sourcename}-light-xfwm4-theme
%{_datadir}/themes/%{theme_name}-Light/xfwm4/

%files -n %{sourcename}-dark-xfwm4-theme
%{_datadir}/themes/%{theme_name}-Dark/xfwm4/

%files -n %{sourcename}-plank-theme
%{_datadir}/plank/themes
