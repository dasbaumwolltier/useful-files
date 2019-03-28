set ccacheSize = "100G"

# set ccache varibles
setenv PATH "/usr/local/libexec/ccache:$PATH"
setenv CCACHE_PATH "/usr/bin:/usr/local/bin"
setenv CCACHE_DIR "/var/tmp/ccache"
setenv CCACHE_LOGFILE "/var/log/ccache.log"

# set ccache temp size to 512MB (default 1GB)
if test -x /usr/local/bin/ccache
    /usr/local/bin/ccache -M $ccacheSize >/dev/null
end