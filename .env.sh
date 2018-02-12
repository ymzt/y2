
case "$(uname -o)" in
	[aA]ndroid )
		: ;;
	* )
		return
esac

function __export_ps1__ () {
	begin='\[\e[1;32m\]' end='\[\e[00m\]'
	export PS1="${begin}\n$(uname):\w:\!>${end} "
};

__export_ps1__

alias h=history
alias ll='ls -l -F --color'

if type -t termux-clipboard-set > /dev/null 2>&1; then
	alias pbcopy=termux-clipboard-set
	alias pbpaste=termux-clipboard-get
fi

function y2_update_termux_env () {
	(cd ~/bin/y2; git pull)
}
